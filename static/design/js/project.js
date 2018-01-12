$(function(){
    var slideshows;
    function initCycle(){
        var carouselOffset = ($(window).width()+17)/2-$('.slide-show .carousel-item').eq(0).find('.item').width()/2-2*parseFloat($('.slide-show .carousel-item').eq(0).css('marginLeft'));
        slideshows = $('.slide-show').cycle({
            carouselOffset: carouselOffset
        });
        //$('.slide-page div').css('width',carouselOffset);
    }
    function reInitCycle() {
        $('.slide-show').cycle('destroy');
        initCycle();
    }
    var reInitTimer;
    $(window).resize(function () {
        clearTimeout(reInitTimer);
        reInitTimer = setTimeout(reInitCycle, 100);
    });
    initCycle();
    $('.slide-show .carousel-item').click(function(){
        var index = $('.slide-show').data('cycle.API').getSlideIndex(this);
        var total = $('.slide-show').find('.carousel-item').length;
        var goCur = 0;
        if(index >= total/5*2){
            if((index-total/5*2) >= total/5){
                goCur = 0;
            } else {
                goCur = index-total/5*2;
            }
        } else {
            goCur = total/5 - 1;
        }
        slideshows.not(this).cycle('goto', goCur);
    });
});
