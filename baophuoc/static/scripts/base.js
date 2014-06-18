/* marquee */
function textMarquee(s) {
    $(s).marquee({
        //speed in milliseconds of the marquee
        duration: 5000,
        //gap in pixels between the tickers
        gap: 0,
        //time in milliseconds before the marquee will start animating
        delayBeforeStart: 0,
        //'left' or 'right' - 'up' or 'down'
        direction: 'up',
        //true or false - should the marquee be duplicated to show an effect of continues flow
        duplicated: true
    });
    $(s).hover(function () {
        $(this).marquee('pause');
    }, function () {
        $(this).marquee('resume');
    });
}

/* stripped */
function stripped() {
    $('.title-list tr:odd').addClass('stripped');
}

$(document).ready(function () {
    verticalDropdown('.nav-vertical-dropdown', '.nav-vertical-dropdown-list', 'fast');
    horizontalDropdown('.nav-horizontal-dropdown', '.nav-horizontal-dropdown-list');
    horizontalDropdown('.nav-horizontal-dropdown-level-2', '.nav-horizontal-dropdown-level-2-list');
    addIconToVerticalDropdown('ul.nav-vertical-dropdown-list li', 'alone');
    stripped();
    textMarquee('.top-news-content');
});