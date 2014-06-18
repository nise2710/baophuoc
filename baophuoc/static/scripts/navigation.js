function verticalDropdown(li, ul, speed) {
    $(ul).hide();
    $(li).hover(
        function () {
            $(this).find(ul).slideDown(speed);
        },
        function () {
            $(this).find(ul).hide();
        }
    );
}

/* dropdown sidebar script */
function horizontalDropdown(li, ul) {
    var imgArrow = '<img src="media/images/sidebar_left_arrow_2.png" class="nav-left-arrow"/>';
    $(ul).hide();
    $(li).hover(
	function () { 
            $(ul).hide();
            $(this).find(ul).before(imgArrow);
            $(this).find(ul).fadeIn(300);
        },
        function () { 
            $('.nav-left-arrow').remove();
            $(this).find(ul).hide();
        }
    );
}

function addIconToVerticalDropdown(li, className) {
    var imgSrc = '<img src="media/images/wheel.gif" class="nav-wheel-icon" />';
    $(li).hover(function () {
        if($(this).hasClass(className)) {
            $(this).find('a').after(imgSrc);
        }
    }, function () {
        $('.nav-wheel-icon').remove();
    });
}
