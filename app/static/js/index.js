!function () {
    "use strict";

    window.onload = function () {
        handleLoading();
        handleMenu();
        handleEarthquake();
    };
}();

handleLoading = function () {
    var loading = document.getElementById("loading");
    var timer = setInterval(function () {
        loading.classList.toggle("hidden");
        clearInterval(timer);
    }, 1000);
}

handleMenu = function () {
    var button = document.getElementById("menu-button");
    button.onclick = function () {
        var menu = document.getElementById("menu");
        menu.classList.toggle("hidden");
    };
}

handleEarthquake = function () {
    var button = document.getElementById("earthquake-submit");
    button.onclick = function () {
        var dayCountInput = document.getElementById("day-count");
        var dayCount = dayCountInput.value;
        window.location.href = "/earthquake?last_day=" + dayCount;
    };
}
