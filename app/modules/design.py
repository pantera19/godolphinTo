# -*- coding:utf8 -*-

import base

i18n = {'ch': {'home'    : u'首 页',
               'projects': u'项 目',
               'about'   : u'关 于',
               'blog'    : u'新 闻',
               'contact' : u'联 系 我 们',
               'search'  : u'搜 索',
               'wwd'     : u'公司历程',
               'wwa'     : u'关于我们',
               'back'    : u'返回',
               'name'    : u'姓名',
               'email'   : u'邮箱',
               'subject' : u'主题',
               'message' : u'信息',
               'send'    : u'发送'
               },
        'en': {'home'    : u'HOME',
               'projects': u'PROJECTS',
               'about'   : u'ABOUT',
               'blog'    : u'BLOG',
               'contact' : u'CONTACT',
               'search'  : u'SEARCH',
               'wwd'     : u'What We Do',
               'wwa'     : u'Who We Are',
               'back'    : u'back',
               'name'    : u'Name',
               'email'   : u'Email',
               'subject' : u'Subject',
               'message' : u'Message',
               'send'    : u'Send'
               }
        }


class DesignBaseHandler(base.BaseHandler):
    pass


class DesignIndex(DesignBaseHandler):
    def get(self, language):
        carousel = self.application.db.query('select * from designcarousel where state=1 order by sort')
        self.render('design/index.html', i18n=i18n, carousel=carousel, language=language, theme=self.theme)


class DesignProjects(DesignBaseHandler):
    def get(self, language):
        projects = self.application.db.query('select * from designproject where state=1 order by create_time desc')
        self.render('design/projects.html', i18n=i18n, projects=projects, language=language, theme=self.theme)


class DesignProject(DesignBaseHandler):
    def get(self, language, id):
        project = self.application.db.get('select * from designproject where state=1 and id=%s', id)
        pictures = []
        if project:
            if project.pictures:
                pictures = eval(project.pictures)
            self.render('design/project.html', i18n=i18n, project=project, pictures=pictures, language=language,
                        theme=self.theme)
        else:
            self.redirect('/design/' + language)


class DesignAbout1(DesignBaseHandler):
    def get(self, language):
        rows = self.application.db.query('select * from appleother where state=1 and style=2 order by sort asc')
        for row in rows:
            row.ch_content = row.ch_content.replace('\r\n', '<br/>').replace('\n', '<br/>')
            row.en_content = row.en_content.replace('\r\n', '<br/>').replace('\n', '<br/>')
        self.render('design/about1.html', i18n=i18n, rows=rows, language=language, theme=self.theme)


class DesignAbout2(DesignBaseHandler):
    def get(self, language):
        rows = self.application.db.query('select * from appleother where state=1 and style=3 order by sort asc')
        for row in rows:
            row.ch_content = row.ch_content.replace('\r\n', '<br/>').replace('\n', '<br/>')
            row.en_content = row.en_content.replace('\r\n', '<br/>').replace('\n', '<br/>')
        self.render('design/about2.html', i18n=i18n, rows=rows, language=language, theme=self.theme)


class DesignBlogs(DesignBaseHandler):
    def get(self, language):
        news = self.application.db.query('select * from DesignNews where state=1 order by id desc')
        self.render('design/blog.html', i18n=i18n, news=news, language=language, theme=self.theme)


class DesignBlog(DesignBaseHandler):
    def get(self, language, id):
        news = self.application.db.get('select * from DesignNews where id=%s', id)
        self.render('design/blogd.html', i18n=i18n, news=news, language=language, theme=self.theme)


class DesignContact(DesignBaseHandler):
    def get(self, language):
        rows = self.application.db.query('select * from appleother where state=1 and style=4 order by sort asc')
        for row in rows:
            row.ch_content = row.ch_content.replace('\r\n', '<br/>').replace('\n', '<br/>')
            row.en_content = row.en_content.replace('\r\n', '<br/>').replace('\n', '<br/>')
        self.render('design/contact.html', i18n=i18n, rows=rows, language=language, theme=self.theme)


class DesignSearch(DesignBaseHandler):
    def get(self, language):
        self.render('design/search.html', i18n=i18n, language=language, theme=self.theme)
