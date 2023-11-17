function setSite(color, font) {
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
            document.querySelector('[data-clickout-type="native_table_box_processed"]').remove(); // lower advert
        } catch (err) {
        }

        try {
            document.querySelector(".container-fluid").remove(); // Guides front page
        } catch (err) {
        }

        try {
            document.querySelector("#style-css-css").remove(); // their's style.css
        } catch (err) {
        }

        try {
            document.querySelector(".container.pb-20.pt-sm-60").remove(); // newsletter
        } catch (err) {
        }

        try {
            document.querySelector(".newsletter.home-newsletter.single").remove(); // newsletter
        } catch (err) {
        }

        try {
            document.querySelector("#widget_container").remove(); // widget Buy/Sell at the best rates
        } catch (err) {
        }

        try {
            document.querySelectorAll(".socials").forEach((e) => { // twitter and others
                e.remove();
            });
        } catch (err) {
        }

        try {
            document.querySelectorAll(".modal").forEach((e) => {
                e.remove();
            });
        } catch (err) {
        }

        try {
            document.querySelectorAll(".article-tag-box").forEach((e) => { // tags
                e.remove();
            });
        } catch (err) {
        }

        try {
            $("a").remove(":contains('Twitter')");
        } catch (err) {
        }

        try {
            $("section").remove(":contains('Videos')");
        } catch (err) {
        }

        try {
            document.querySelector("body > div.main > main > section:nth-child(5)").remove(); // Buy/Sell at the best rates (front page)
        } catch (err) {
        }

        $("head").prepend("<link href=\"/assets/images/favicon.png\" rel=\"shortcut icon\"/>" +
            "<link href=\"https://cdn.jsdelivr.net/gh/orestbida/cookieconsent@v2.9.2/dist/cookieconsent.css\" rel=\"stylesheet\"/>" +
            "<script defer=\"\" src=\"/assets/js/cookieconsent.js\"></script>" +
            "<script defer=\"\" src=\"/assets/js/cookieconsent-init.js\"></script>");

        $("#menu-header > li:nth-child(10) > ul").load("/kak-index.html #menu-header > li:nth-child(9) > ul > li"); // fix recommended
        $("#menu-item-119744 > ul").load("/kak-index.html #menu-item-119744 > ul > li"); // fix recommended footer

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

        if (hostname === 'da-1.com' || hostname === 'intspeed.com' || hostname === 'hindex.amkamdam.com' || hostname === 'xxx.xx') {
            setSite('green', 'Kanit')
        }

        if (hostname === 'huy.com' || hostname === 'xxx.xx' || hostname === 'xxx.xx') {
            setSite('pink', 'Oswald')
        }

        if (hostname === 'huy-1.com' || hostname === 'xxx.xx' || hostname === 'xxx.xx') {
            setSite('red', 'Playfair Display')
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
