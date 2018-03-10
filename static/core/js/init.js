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
}

$(function () {
    "use strict";

    initialize();
    window.initJsScript && $.KittenTeach[window.initJsScript].init();
});
