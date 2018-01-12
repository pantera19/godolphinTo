var ajaxSearch;
function showSearch(keywords, langCode){
    if(ajaxSearch){
        ajaxSearch.abort();
    }
    ajaxSearch = $.ajax({
        url: "/api/main_search",
        data: {kw: keywords, lang_code: langCode},
        type: 'get',
        dataType: 'json',
        success: function (json) {
            var resultdata = '';
            if(json.ret && json.ret.length > 0){
                for(var m = 0; m < json.ret.length; m++) {
                    resultdata += '<li><a href="' + json.ret[m].url + '">' + json.ret[m].type + ' | ' + json.ret[m].title + '</a></li>';
                }
                $('.search-result').removeClass('no-dis').html(resultdata);
            } else {
                $('.search-result').addClass('no-dis').html('');
            }
        }
    });
}

function OnInputSearch(event) {
    var keywords = event.target.value;
    if(keywords.length>0){
        $('.search-box .close').removeClass('no-dis');
        showSearch(keywords, $('#langCode').val());
    } else {
        $('.search-result').addClass('no-dis').html('');
    }
}

function OnPropSearchChanged(event) {
    var keywords = event.propertyName.toLowerCase();
    console.log(keywords);
}

$(function () {
    $('.search-box .close').on('click', function () {
        $(this).addClass('no-dis').prev('input').val('');
        $('.search-result').addClass('no-dis').html('');
    });

    $('.search-hot span').on('click', function () {
        $('.search-box .close').removeClass('no-dis');
        $('.search-box input').val($(this).text());
        showSearch($(this).text(), $('#langCode').val());
    });
});

