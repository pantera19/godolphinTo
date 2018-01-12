# -*- coding:utf8 -*-

import tornado
import tornado.escape
import json
import time
from datetime import date, datetime
import decimal


class Events(tornado.web.RequestHandler):
    def post(self):
        event_id = int(self.get_argument('event_id', 0))
        name = self.get_argument('name', '')
        phone = self.get_argument('phone', '')
        email = self.get_argument('email', '')
        create_time = datetime.now()

        sql = '''insert into eventmember (event_id,name,phone,email,create_time) values (%s,%s,%s,%s,%s)'''
        ret = self.application.db.execute(sql, event_id, name, phone, email, create_time)

        code = 0 if ret > 0 else 1
        self.write(json.dumps({'code': code}, default=CJsonEncoder.default))


class Contact(tornado.web.RequestHandler):
    def post(self):
        print 123
        source = self.get_argument('source', 'main')
        name = self.get_argument('name', '')
        subject = self.get_argument('subject', '')
        email = self.get_argument('email', '')
        message = self.get_argument('message', '')
        create_time = datetime.now()

        sql = '''insert into contact (source,name,subject,email,message,create_time) values (%s,%s,%s,%s,%s,%s)'''
        ret = self.application.db.execute(sql, source, name, subject, email, message, create_time)

        code = 0 if ret > 0 else 1
        self.write(json.dumps({'code': code}, default=CJsonEncoder.default))


class DesignSearch(tornado.web.RequestHandler):
    def get(self):
        kw = self.get_argument('kw', '')
        lang_code = self.get_argument('lang_code', 'ch')

        ret = []

        designs = self.application.db.query(
            'select * from DesignProject where state=1 and (ch_title like %s or en_title like %s) limit 5',
            '%' + kw + '%', '%' + kw + '%')

        for design in designs:
            ret.append(
                {'id'   : design.id,
                 'title': design.ch_title if lang_code == 'ch' else design.en_title,
                 'type' : 'project',
                 'url'  : '/design/%s/project/%s' % (lang_code, design.id)
                 })

        news = self.application.db.query(
            'select * from DesignNews where state=1 and (ch_title like %s or en_title like %s) limit 5',
            '%' + kw + '%', '%' + kw + '%')

        for new in news:
            ret.append(
                {'id'   : new.id,
                 'title': new.ch_title if lang_code == 'ch' else new.en_title,
                 'type' : 'news',
                 'url'  : '/design/%s/blog/%s' % (lang_code, new.id)
                 })

        self.write(json.dumps({'ret': ret}, default=CJsonEncoder.default))


class MainSearch(tornado.web.RequestHandler):
    def get(self):
        kw = self.get_argument('kw', '')
        lang_code = self.get_argument('lang_code', 'ch')

        ret = []

        designs = self.application.db.query(
            'select * from DesignProject where state=1 and (ch_title like %s or en_title like %s) limit 5',
            '%' + kw + '%', '%' + kw + '%')

        for design in designs:
            ret.append(
                {'id'   : design.id,
                 'title': design.ch_title if lang_code == 'ch' else design.en_title,
                 'type' : 'project',
                 'url'  : '/design/%s/project/%s' % (lang_code, design.id)
                 })

        news = self.application.db.query(
            'select * from DesignNews where state=1 and (ch_title like %s or en_title like %s) limit 5',
            '%' + kw + '%', '%' + kw + '%')

        for new in news:
            ret.append(
                {'id'   : new.id,
                 'title': new.ch_title if lang_code == 'ch' else new.en_title,
                 'type' : 'news',
                 'url'  : '/design/%s/blog/%s' % (lang_code, new.id)
                 })

        events = self.application.db.query(
            'select * from Events where state=1 and (ch_title like %s or en_title like %s) limit 5',
            '%' + kw + '%', '%' + kw + '%')

        for event in events:
            ret.append(
                {'id'   : event.id,
                 'title': event.ch_title if lang_code == 'ch' else event.en_title,
                 'type' : 'event',
                 'url'  : '/%s/event/%s' % (lang_code, event.id)
                 })

        self.write(json.dumps({'ret': ret}, default=CJsonEncoder.default))


class CJsonEncoder:
    @classmethod
    def default(ss, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            raise TypeError('%r is not JSON serializable' % obj)

    @classmethod
    def timestamp(ss, obj):
        if isinstance(obj, datetime):
            return time.mktime(obj.timetuple())
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            raise TypeError('%r is not JSON serializable' % obj)
