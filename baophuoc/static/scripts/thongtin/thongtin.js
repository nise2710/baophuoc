/* dropdown sidebar script */
$(document).ready(function () {
	$('.dropdown').hover(
		function () { $(this).find('.sub-menu').fadeIn(500);},
		function () { $(this).find('.sub-menu').hide();}
	);
});
/* end sidebar script */