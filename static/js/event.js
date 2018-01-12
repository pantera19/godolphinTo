$(function () {
    var isEventLock = false;
    $('#btnSend').on('click', function () {
        var $userName = $('#userName');
        var $userPhone = $('#userPhone');
        var $userEmail = $('#userEmail');
        if ($.trim($userName.val()) == '') {
            $.alert('请输入您的姓名');
            return false;
        }
        if ($.trim($userPhone.val()) == '') {
            $.alert('请输入您的手机号');
            return false;
        } else {
            var rePhone = /^1[3|4|5|7|8][0-9]\d{4,8}$/;
            if (!rePhone.test($.trim($userPhone.val()))) {
                $.alert('手机号格式不正确');
                return false;
            }
        }
        if ($.trim($userEmail.val()) == '') {
            $.alert('请输入您的邮箱');
            return false;
        } else {
            var reMail = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
            if (!reMail.test($.trim($userEmail.val()))) {
                $.alert('邮箱格式不正确');
                return false;
            }
        }
        if (isEventLock) {
            return false;
        }
        isEventLock = true;
        $.post('/api/events', {
            event_id: $('#eventID').val(),
            name: $userName.val(),
            phone: $userPhone.val(),
            email: $userEmail.val()
        }, function (data) {
            isEventLock = false;
            data = eval('(' +data+ ')')
            if(data.code == 0){
                $.alert('报名成功');
                $userName.val('');
                $userPhone.val('');
                $userEmail.val('');
            } else {
                $.alert('系统错误');
            }
        });
    });
});
