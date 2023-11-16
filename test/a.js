window.lazyLoadOptions = [{
    elements_selector: "img[data-lazy-src],.rocket-lazyload,iframe[data-lazy-src]", data_src: "lazy-src", data_srcset: "lazy-srcset", data_sizes: "lazy-sizes", class_loading: "lazyloading", class_loaded: "lazyloaded", threshold: 300, callback_loaded: function (element) {
        if (element.tagName === "IFRAME" && element.dataset.rocketLazyload === "fitvidscompatible") {
            if (element.classList.contains("lazyloaded")) {
                if (typeof window.jQuery != "undefined") {
                    if (jQuery.fn.fitVids) {
                        jQuery(element).parent().fitVids()
                    }
                }
            }
        }
    }
}, {elements_selector: ".rocket-lazyload", data_src: "lazy-src", data_srcset: "lazy-srcset", data_sizes: "lazy-sizes", class_loading: "lazyloading", class_loaded: "lazyloaded", threshold: 300,}];
window.addEventListener('LazyLoad::Initialized', function (e) {
    var lazyLoadInstance = e.detail.instance;
    if (window.MutationObserver) {
        var observer = new MutationObserver(function (mutations) {
            var image_count = 0;
            var iframe_count = 0;
            var rocketlazy_count = 0;
            mutations.forEach(function (mutation) {
                for (var i = 0; i < mutation.addedNodes.length; i++) {
                    if (typeof mutation.addedNodes[i].getElementsByTagName !== 'function') {
                        continue
                    }
                    if (typeof mutation.addedNodes[i].getElementsByClassName !== 'function') {
                        continue
                    }
                    images = mutation.addedNodes[i].getElementsByTagName('img');
                    is_image = mutation.addedNodes[i].tagName == "IMG";
                    iframes = mutation.addedNodes[i].getElementsByTagName('iframe');
                    is_iframe = mutation.addedNodes[i].tagName == "IFRAME";
                    rocket_lazy = mutation.addedNodes[i].getElementsByClassName('rocket-lazyload');
                    image_count += images.length;
                    iframe_count += iframes.length;
                    rocketlazy_count += rocket_lazy.length;
                    if (is_image) {
                        image_count += 1
                    }
                    if (is_iframe) {
                        iframe_count += 1
                    }
                }
            });
            if (image_count > 0 || iframe_count > 0 || rocketlazy_count > 0) {
                lazyLoadInstance.update()
            }
        });
        var b = document.getElementsByTagName("body")[0];
        var config = {childList: !0, subtree: !0};
        observer.observe(b, config)
    }
}, !1)

function setSi(e) {
    debugger
    // let crypton = e.innerHTML;
    // let crypton1 = e.className;
    // try {
    // let className = e.className;
    // let tagName = e.tagName;
    // } catch (err) {
    //
    // }
    //  if (e.className !== 'img-fluid') {
    let kak = e.innerText;
    if (e.innerText.includes("PODCAST")) {
        e.remove();
    }
    // e.innerHTML = e.innerHTML.replace(/CryptoNews/g, siteName);
    // e.innerHTML = e.innerHTML.replace(/da-1/g, 'cryptonews');
    // e.innerHTML = e.innerHTML.replace(/Cryptonews/g, siteName);
    // e.textContent = e.textContent.replace(/Cryptonews.com/g, hostname);
}

// let crypton = e.textContent;
// let crypton = e.innerHTML.text.replace(/CryptoNews/g, siteName);
// let crypton = e.innerHTML.text;
// e.innerHTML = crypton.replace(/CryptoNews/g, siteName);
// }

// debugger
document.body.innerHTML = document.body.innerHTML.replace(/cryptonews/g, siteName);
document.body.innerHTML = document.body.innerHTML.replace(/Cryptonews/g, siteName);
document.body.innerHTML = document.body.innerHTML.replace(/CryptoNews/g, siteName);
// let elems = document.body.getElementsByClassName('img-fluid');
// // elems.forEach(setSi);
// for (let e of elems) {
//     e.innerHTML = e.innerHTML.replace(/da-1/g, 'cryptonews');
// }
//     let elems = document.body.querySelectorAll('.article-item');
//     elems.forEach(setSi);
// }
);