var initMessage = "" +
    "==============================\n" +
    "|      KittenTeach init      |\n" +
    "==============================\n\n" +
    "            |\\___/|\n" +
    "            )     (\n" +
    "           =\\     /=\n" +
    "             )===(\n" +
    "            /     \\\n" +
    "            |     |\n" +
    "           /       \\\n" +
    "           \\       /\n" +
    "            \\__  _/\n" +
    "              ( (\n" +
    "               ) )\n" +
    "              (_(";

function initialize() {
    console.log(initMessage);

    // init header
    var quickSearch = $('#quick-search');
    var quickSearchInput = quickSearch.find('.header-search__input');

    quickSearch.on('click', function (e) {
        var $target = $(e.target);

        if ($target.is('.header-search__image') || $target.parents('.header-search__image').length > 0) {
            quickSearch.toggleClass('header-controls__search--active');
            quickSearchInput.focus();
        }
    });

    quickSearchInput.on('input focusout', function (e) {
        if (e.type === 'input') {
            // todo quick search
        } else if (e.type === 'focusout') {
            quickSearch.removeClass('header-controls__search--active');
        }
    });
}

$(function () {
    "use strict";

    initialize();
    window.initJsScript && $.KittenTeach[window.initJsScript].init();
});
