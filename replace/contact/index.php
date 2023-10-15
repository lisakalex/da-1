<?php
require '../vendor/autoload.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

$url = $_SERVER['REQUEST_SCHEME'] . '://' . $_SERVER['HTTP_HOST'] . '/assets/a.json';

$curl = curl_init();
curl_setopt_array($curl, [
    CURLOPT_URL => $url,
    CURLOPT_HTTPHEADER => [
        'Content-Type: application/json',
    ],
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_FOLLOWLOCATION => 1,
    CURLOPT_CONNECTTIMEOUT => 10,
    CURLOPT_TIMEOUT => 30,
]);

$curl_error = curl_error($curl);
$contents = json_decode(curl_exec($curl));
curl_close($curl);

function turnstile($response)
{
    global $contents;
    $url = 'https://challenges.cloudflare.com/turnstile/v0/siteverify';
    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_HTTPHEADER => [
            'Content-Type: application/json',
        ],
        CURLOPT_CUSTOMREQUEST => 'POST',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => 1,
        CURLOPT_CONNECTTIMEOUT => 10,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_POSTFIELDS => json_encode([
            'secret' => $contents->secret,
            'response' => $response
        ]),
    ]);

    $result = curl_exec($curl);
    curl_close($curl);

    $return_result = false;

    if ($json = json_decode($result)) {
        if ($json->success) {
            $return_result = true;
        } else {
            $return_result = false;
        }
    }

    return $return_result;
}

$mail = new PHPMailer(true);

if (filter_input(INPUT_POST, 'send-message', FILTER_SANITIZE_SPECIAL_CHARS) === 'da-send-message') {
    $response = $_POST['cf-turnstile-response'];
    $subject = $_POST['subject'];
    $name = $_POST['first_name'];
    $last_name = $_POST['last_name'];
    $email = $_POST['email_address'];
    $phone = $_POST['phone'];
    $user_message = $_POST['form_message'];

    if (turnstile($response)) {
        $message = /** @lang text */
            "<!DOCTYPE HTML>
            <html lang=\"en\">
            <head>
                <style>
                    .ka {
                        padding: 100px 0 0 0;
                    }
            
                    .ka1 {
                        color: #20bea8;
                    }
            
                    .ka2 {
                        padding: 2% 25% 2% 25%;
                        color: #606662;
                        text-align: left;
            
                    }
            
                    .ka3 {
                        /*background-color: #20bea8;*/
                        /*padding: 10px;*/
                        /*margin: 30px;*/
                        text-decoration: none;
                        color: #fff;
                        font-weight: 700;
                        font-size: 1.3em;
                        /*text-align: left;*/
            
                    }
            
                    .ka4 {
                        background-color: #20bea8;
                        padding: 10px;
                        margin: 30px 25% 30px 25%;
                        text-decoration: none;
                        color: #fff;
                        text-align: center;
                        border-radius: 5px;
            
                    }
            
                    .ku {
                        background-color: #e4edef;
                        padding: 50px 0 50px 0;
                        box-sizing: border-box;
                        display: block;
                        font-family: \"Open Sans\", sans-serif;
                        font-size: 14px;
                        line-height: 20px;
                        color: #8d9a9d;
                        /*text-align: center;*/
            
                    }
            
                    .main-container {
                        background-color: #F6F8F9;
                        /*height: 500px;*/
                        /*padding: 50px;*/
                        text-align: center;
                    }
            
                </style>
            </head>
            <body class=\"\">
            <div class=\"main-container\">
                <div class=\"ka\">
                    <img src=\"https://www.amkamdam.com/assets/images/logo-3.png\" alt=\"\" height=\"50\">
                </div>
                <div class=\"ka1\">
                    A prepaid credit card for the crypto community
                </div>
                <br>
                <div class=\"ka2\">
                    <h3>$name $last_name</h3>
                    <p>$user_message</p>
                    <p>Instant Messenger: $phone</p>
                    <br>
                </div>
                <div class=\"ku\">
                    <img src=\"https://kumpenot.com/media/img/foot.png\" alt=\"\">
                    <p class=\"footer-text\">No. 5, 17/F Bonham Trade Centre, 50 Bonham Strand, Sheung Wan, Hong Kong</p>
                    <p class=\"footer-text\">52-60 Tabernacle Street, London, United Kingdom, EC2A 4NJ</p>
                    <p class=\"footer-copyright\">© 2018-2019 <a href=\"index.htm\">kumpenot Ltd </a></p>
                </div>
            </div>
            </body>
            </html>
            ";

        try {

            //Server settings
            $mail->SMTPDebug = SMTP::DEBUG_OFF;                      //Enable verbose debug output: DEBUG_SERVER
            $mail->isSMTP();                                            //Send using SMTP
            $mail->Host = $contents->Host;                     //Set the SMTP server to send through
            $mail->SMTPAuth = true;                                   //Enable SMTP authentication
            $mail->Username = $contents->Username;                     //SMTP username
            $mail->Password = $contents->Password;                               //SMTP password
            $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;            //Enable implicit TLS encryption
            $mail->Port = 587;                                    //TCP port to connect to; use 587 if you have set `SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS`

            //Recipients
            $mail->setFrom($email, $name);
            $mail->addAddress($contents->Username);     //Add a recipient
//    $mail->addAddress('ellen@example.com');               //Name is optional
//        $mail->addReplyTo('support@amkamdam.com', 'support');
//        $mail->addCC('alexlisak@hotmail.com');
//    $mail->addBCC('bcc@example.com');

            //Attachments
//        $mail->addAttachment('../assets/images/125.png');         //Add attachments
//    $mail->addAttachment('/tmp/image.jpg', 'new.jpg');    //Optional name

            //Content
            $mail->isHTML(true);                                  //Set email format to HTML
            $mail->Subject = $subject;
            $mail->Body = $message;
//        $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

            $mail->send();
//            echo 'Message has been sent huy';
        } catch (Exception $e) {
//            echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
        }
        $err = urlencode("You have sent message successfully.");
        header("Location: /contact/?err=$err");
        exit ();
    } else {
        $err = urlencode("Try again.");
        header("Location: /contact/?err=$err");
        exit ();
    }
}

?>
