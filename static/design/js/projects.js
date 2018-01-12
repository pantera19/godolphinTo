$(function(){
    $('.gridalicious .item').hover(function(){
        $(this).find('.mask').css('display','block');
    },function () {
        $(this).find('.mask').css('display','none');
    });
    $('.gridalicious').gridalicious({
        gutter: 0,
        width: 167,
        animate: true,
        animationOptions: {
            speed: 150,
            duration: 400,
            complete:function(data){
            }
        }
    });
});