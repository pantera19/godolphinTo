# -*- coding:utf8 -*-

import base

i18n = {'ch': {'home'       : u'首页',
               'events'     : u'活动入口',
               'about'      : u'关于',
               'contact'    : u'联系我们',
               'wow'        : u'WOW',
               'news'       : u'新闻',
               'search'     : u'搜索',
               'title1'     : u'葡萄酒空间设计',
               'title2'     : u'葡萄酒教育',
               'title3'     : u'葡萄酒传媒',
               'event_state': {0: u'隐藏', 1: u'进行中', 2: u'已结束'},
               'name'       : u'姓名',
               'email'      : u'邮箱',
               'subject'    : u'主题',
               'message'    : u'信息',
               'send'       : u'发送'
               },
        'en': {'home'       : 'HOME',
               'events'     : 'EVENTS',
               'about'      : 'ABOUT',
               'contact'    : 'CONTACT',
               'wow'        : 'WOW',
               'news'       : 'NEWS',
               'search'     : 'SEARCH',
               'title1'     : 'FABRICATION',
               'title2'     : 'EDUCATION',
               'title3'     : 'COMMUNICATION',
               'event_state': {0: u'hide', 1: u'OPEN', 2: u'CLOSE'},
               'name'       : u'Name',
               'email'      : u'Email',
               'subject'    : u'Subject',
               'message'    : u'Message',
               'send'       : u'Send'
               }
        }


class HomeBaseHandler(base.BaseHandler):
    pass


class HomeIndex(HomeBaseHandler):
    def get(self, language='ch'):
        carousel = self.application.db.query('select * from MainCarousel where state=1 order by sort')
        entrance = self.application.db.query('select * from MainEntrance where state=1 order by id')
        self.render('home/index.html', i18n=i18n, carousel=carousel, entrance=entrance, language=language,
                    theme=self.theme)


class HomeEvents(HomeBaseHandler):
    def get(self, language='ch'):
        events = self.application.db.query('select * from events where state>0 order by state asc,id desc')
        self.render('home/event.html', i18n=i18n, events=events, language=language,
                    theme=self.theme)


class HomeEvent(HomeBaseHandler):
    def get(self, language, id):
        events = self.application.db.get('select * from events where state>0 and id=%s', id)
        self.render('home/event_d.html', i18n=i18n, events=events, language=language,
                    theme=self.theme)


class HomeAbout(HomeBaseHandler):
    def get(self, language='ch'):
        rows = self.application.db.query('select * from appleother where state=1 and style=0 order by sort asc')
        for row in rows:
            row.ch_content = row.ch_content.replace('\r\n', '<br/>').replace('\n', '<br/>')
            row.en_content = row.en_content.replace('\r\n', '<br/>').replace('\n', '<br/>')
        self.render('home/about-us.html', i18n=i18n, rows=rows, language=language, theme=self.theme)


class HomeContact(HomeBaseHandler):
    def get(self, language='ch'):
        rows = self.application.db.query('select * from appleother where state=1 and style=1 order by sort asc')
        for row in rows:
            row.ch_content = row.ch_content.replace('\r\n', '<br/>').replace('\n', '<br/>')
            row.en_content = row.en_content.replace('\r\n', '<br/>').replace('\n', '<br/>')
        self.render('home/contact.html', i18n=i18n, rows=rows, language=language, theme=self.theme)


class HomeWOW(HomeBaseHandler):
    def get(self, language='ch'):
        projects = self.application.db.query('select * from DesignProject where state=1 order by create_time desc')
        china_data = {}
        world_data = {}
        for project in projects:
            area = project.en_author.split(',')
            ch_area = project.ch_author.split(' ')
            if area[-1] == 'China':
                if china_data.has_key(ch_area[1]):
                    china_data[ch_area[1]] += 1
                else:
                    china_data[ch_area[1]] = 1

            if world_data.has_key(area[-1]):
                world_data[area[-1]] += 1
            else:
                world_data[area[-1]] = 1

        new_china_data = []
        new_world_data = []

        for k, v in china_data.iteritems():
            new_china_data.append({'name': k, 'value': v})

        for k, v in world_data.iteritems():
            new_world_data.append({'name': k, 'value': v})

        self.render('home/wow.html', i18n=i18n, projects=projects, cd=new_china_data, wd=new_world_data,
                    language=language, theme=self.theme)


class HomeNews(HomeBaseHandler):
    def get(self, language='ch'):
        news = self.application.db.query('select * from MainNews where state=1 order by id desc')

        self.render('home/news.html', i18n=i18n, news=news, language=language, theme=self.theme)


class HomeNewsd(HomeBaseHandler):
    def get(self, language, id):
        news = self.application.db.get('select * from MainNews where state=1 and id=%s', id)
        self.render('home/newsd.html', i18n=i18n, news=news, language=language, theme=self.theme)


class HomeSearch(HomeBaseHandler):
    def get(self, language='ch'):
        hotword = self.application.db.query('select * from HotWord where state=1 order by id desc')
        self.render('home/search.html', i18n=i18n, hotword=hotword, language=language, theme=self.theme)
