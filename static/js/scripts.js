// Sets padding of main section
$(document).ready(function(){
    function setPaddingMain() {
        main = $('#main');
        main.css('margin-top', $('#top-nav').height());
    }
    setPaddingMain();
})