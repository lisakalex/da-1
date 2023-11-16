function setSite(color, font, site, firstLine, city, country, postCode) {
    document.documentElement.style.setProperty('--me-color', color);
    document.documentElement.style.setProperty('--me-font-family', font);
    // document.querySelector('.me-address').outerHTML = '<div class="d-inline-block">' + site + '<br>' + firstLine + '<br>' + city + '<br>' + country + '<br>' + postCode + '<br></div>';
}

$(function () {

        let href = location.href
        let origin = location.origin
        let pathname = location.pathname
        let hostname = location.hostname;
        let siteName = location.hostname.split('.')[0];
        document.title = siteName;

        try {
            document.querySelector('[data-clickout-type="native_table_box_processed"]').remove();
        } catch (err) {
        }

        try {
            document.querySelector(".container-fluid").remove();
        } catch (err) {
        }

        try {
            document.querySelector("#style-css-css").remove();
        } catch (err) {
        }

        $("head").prepend("<link href=\"/assets/images/favicon.png\" rel=\"shortcut icon\"/>" +
            "<link href=\"https://cdn.jsdelivr.net/gh/orestbida/cookieconsent@v2.9.2/dist/cookieconsent.css\" rel=\"stylesheet\"/>" +
            "<script defer=\"\" src=\"https://cdn.jsdelivr.net/gh/orestbida/cookieconsent@v2.9.2/dist/cookieconsent.js\"></script>" +
            "<script defer=\"\" src=\"/assets/js/cookieconsent-init.js\"></script>");

        // $(".body").prepend("<div class=\"se-pre-con\"></div>");
        // $(".header").load("/me-index.html .header > *");
        // $(".footer").load("/me-index.html .footer > *");


        if (location.pathname === '/exclusives/') {
            $("body > div.main > main > div:nth-child(2)").load("/exclusives/features/ .pt-20");
            $("body > div.main > main > section").load("/exclusives/features/ .mb-80");
        }

        try {
            document.querySelector(".breadcrumbs").children[0].textContent = siteName
        } catch (err) {

        }

        try {
            document.querySelector("#copyright").textContent = '© 2023 ' + siteName + '. All rights reserved';
        } catch (err) {

        }

        try {
            document.querySelectorAll('.me-mailto').forEach((e) => {
                e.outerHTML = '<a href="mailto:support@' + hostname + '" class="d-inline-block" style="color:#fff">support@' + hostname + '</a>';
            });
        } catch (err) {
        }

        try {
            document.querySelector(".header__logo > img").src = "/assets/images/" + hostname + ".svg";
        } catch (err) {
        }

        if (hostname === 'da-1.com' || hostname === 'intspeed.com' || hostname === 'xxx.xx') {
            setSite('green', 'Kanit', siteName, '52-60 Tabernacle Street', 'London', 'United Kingdom', 'EC2A 4NJ')
        }

        if (hostname === 'huy.com' || hostname === 'xxx.xx' || hostname === 'xxx.xx') {
            setSite('pink', 'Oswald', siteName, '1 Ku Tabernacle Street', 'London', 'United Kingdom', 'EC2A 4NJ')
        }

        if (hostname === 'huy-1.com' || hostname === 'xxx.xx' || hostname === 'xxx.xx') {
            setSite('red', 'Playfair Display', siteName, '23 Lady Gaga Street', 'London', 'United Kingdom', 'EC2A 4NJ')
        }

        function setSi(e) {
            e.innerHTML = e.innerHTML.replace(/cryptonews/g, siteName);
            e.innerHTML = e.innerHTML.replace(/Cryptonews/g, siteName);
            e.innerHTML = e.innerHTML.replace(/CryptoNews/g, siteName);
        }

        try {
            document.body.querySelectorAll('.layout-size').forEach(setSi);
        } catch (err) {
        }
    }
);

$(window).load(function () {
    // Animate loader off screen
    $(".se-pre-con").fadeOut("slow");
});
