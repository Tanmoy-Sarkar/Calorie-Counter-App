$(window).scroll(function() {
    if($(this).scrollTop()>5) {
        $( ".navbar-me" ).addClass("fixed-me");
    } else {
        $( ".navbar-me" ).removeClass("fixed-me");
    }
});