$(function () {
    var isContactLock = false;
    $('#btnSend').on('click', function () {
        var $userName = $('#userName');
        var $userEmail = $('#userEmail');
        var $userSubject = $('#userSubject');
        var $userMessage = $('#userMessage');
        if ($.trim($userName.val()) == '') {
            $.alert('Please enter your name');
            return false;
        }
        if ($.trim($userEmail.val()) == '') {
            $.alert('Please enter your email address');
            return false;
        } else {
            var reMail = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
            if (!reMail.test($.trim($userEmail.val()))) {
                $.alert('Incorrect mailbox format');
                return false;
            }
        }
        if (isContactLock) {
            return false;
        }
        isContactLock = true;
        $.post('/api/a_contact', {
            source: 'main',
            name: $userName.val(),
            email: $userEmail.val(),
            subject: $userSubject.val(),
            message: $userMessage.val()
        }, function (data) {
            isContactLock = false;
            data = eval('(' + data + ')')
            if (data.code == 0) {
                $.alert('Message success');
                $userName.val('');
                $userEmail.val('');
                $userSubject.val('');
                $userMessage.val('');
            } else {
                $.alert('System error');
            }
        });
    });
});
