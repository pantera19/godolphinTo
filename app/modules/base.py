# -*- coding:utf8 -*-


import tornado.web
import re

touch_re = re.compile(
    r'.*(iOS|iPhone|Android|Windows Phone|webOS|BlackBerry|Symbian|Opera Mobi|UCBrowser|MQQBrowser|Mobile|Touch).*',
    re.I)


class BaseHandler(tornado.web.RequestHandler):
    @property
    def theme(self):
        '''获取访问类型 '''
        try:
            ua = self.request.headers.get("User-Agent", "")
            theme = True if touch_re.match(ua) else False
        except Exception as e:
            theme = False

        return theme
