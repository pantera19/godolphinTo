function checkMobile(){
    var isiPad = navigator.userAgent.match(/iPad/i) != null;
    if(isiPad){
        return false;
    }
    var isMobile=navigator.userAgent.match(
    /iphone|android|ipad|phone|mobile|wap|netfront|x11|java|operamobi|operamini|ucweb|windowsce|symbian|symbianos|series|webos|sony|blackberry|dopod|nokia|samsung|palmsource|xda|pieplus|meizu|midp|cldc|motorola|foma|docomo|up.browser|up.link|blazer|helio|hosin|huawei|novarra|coolpad|webos|techfaith|palmsource|alcatel|amoi|ktouch|nexian|ericsson|philips|sagem|wellcom|bunjalloo|maui|smartphone|iemobile|spice|bird|zte-|longcos|pantech|gionee|portalmmm|jig browser|hiptop|benq|haier|^lct|320x320|240x320|176x220/i)!= null;
    if(isMobile){
        return true;
    }
    return false;
}

$(function(){
    var swiper = new Swiper('.swiper-container', {
        autoplay: 3000,
        spaceBetween: 30,
        effect: 'fade'
    });

    if (checkMobile()){
        $('.swiper-wrapper').css('height',$(window).width()*250/400);
    }
});
