# -*- coding:utf8 -*-


import base
import tornado.web
from werkzeug.security import generate_password_hash, check_password_hash


class ManageBaseHandler(base.BaseHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

    def _hash_password(self, password):
        return generate_password_hash(password)


class MIndex(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('admin/index.html', user=self.current_user)


class LoginHandler(ManageBaseHandler):
    def get(self):
        self.render('admin/login.html')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        user = self.application.db.get('select * from users where username=%s', username)

        if user and check_password_hash(user['password_hash'], password):
            self.set_secure_cookie("username", self.get_argument("username"))
            self.redirect("/manage/index")
        else:
            self.redirect("/manage/login")


class LogoutHandler(ManageBaseHandler):
    def get(self):
        self.clear_cookie("username")
        self.redirect("/manage/login")


class ChangePasswordHandler(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('admin/change_password.html', user=self.current_user)

    def post(self):
        old_password = self.get_argument("old_password")
        password = self.get_argument("password")

        user = self.application.db.get('select * from users where username=%s', self.current_user)
        if user and check_password_hash(user['password_hash'], old_password):
            ret = self.application.db.execute('update users set password_hash=%s where id=%s',
                                              generate_password_hash(password), user['id'])
            self.redirect("/manage/login")
        else:
            self.redirect("/manage/change_password")


class main_carousel(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        carousels = self.application.db.query('select * from MainCarousel  order by sort asc')

        self.render('admin/main_carousel.html', carousels=carousels)


class main_carousel_detail(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = int(self.get_argument("id", 0))
        slider = self.application.db.get('select * from MainCarousel where id=%s', id)
        self.render('admin/main_carousel_detail.html', slider=slider)

    @tornado.web.authenticated
    def post(self):
        id = int(self.get_argument("id", 0))
        ch_title = self.get_argument("ch_title")
        en_title = self.get_argument("en_title")
        web_cover = self.get_argument("web_cover")
        wap_cover = self.get_argument("wap_cover")

        ret = self.application.db.execute(
            'update MainCarousel set ch_title=%s,en_title=%s,web_cover=%s,wap_cover=%s where id=%s', ch_title, en_title,
            web_cover, wap_cover, id)

        self.redirect('/manage/main_carousel')


class main_carousel_state(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id, state):
        ret = self.application.db.execute('update MainCarousel set state=%s where id=%s', state, id)
        self.redirect('/manage/main_carousel')


class main_carousel_sort(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id, move):
        slider = self.application.db.get('select * from MainCarousel where id=%s', id)

        if (slider.sort == 1 and move == 'up') or (slider.sort == 4 and move == 'down'):
            pass
        else:
            if move == 'up':
                tmp_s = self.application.db.get('select * from MainCarousel where sort=%s', slider.sort - 1)
                self.application.db.execute('update MainCarousel set sort=%s where id=%s', slider.sort - 1, slider.id)
                self.application.db.execute('update MainCarousel set sort=%s where id=%s', tmp_s.sort + 1, tmp_s.id)
            else:
                tmp_s = self.application.db.get('select * from MainCarousel where sort=%s', slider.sort + 1)
                self.application.db.execute('update MainCarousel set sort=%s where id=%s', slider.sort + 1, slider.id)
                self.application.db.execute('update MainCarousel set sort=%s where id=%s', tmp_s.sort - 1, tmp_s.id)
        self.redirect('/manage/main_carousel')


class main_entrance(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        entrance = self.application.db.query('select * from MainEntrance order by  id asc')
        self.render('admin/main_entrance.html', entrance=entrance)


class main_entrance_detail(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = int(self.get_argument("id", 0))
        slider = self.application.db.get('select * from MainEntrance where  id=%s', id)
        self.render('admin/main_entrance_detail.html', slider=slider)

    def post(self):
        id = int(self.get_argument("id", 0))
        ch_title = self.get_argument("ch_title")
        en_title = self.get_argument("en_title")
        ch_url = self.get_argument("ch_url")
        en_url = self.get_argument("en_url")
        ch_summary = self.get_argument("ch_summary")
        en_summary = self.get_argument("en_summary")
        cover = self.get_argument('cover', '')

        ret = self.application.db.execute(
            'update MainEntrance set ch_title=%s,en_title=%s,ch_url=%s,en_url=%s,ch_summary=%s,en_summary=%s,cover=%s where id=%s',
            ch_title, en_title, ch_url, en_url, ch_summary, en_summary, cover, id)
        self.redirect('/manage/main_entrance')


class main_news(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        start = 0
        ps = 50
        page = int(self.get_argument("page", 0))

        if page == 0:
            ps = 50
        else:
            start = ps * page
        news = self.application.db.query('select * from MainNews order by create_time desc limit %s,%s',
                                         start, ps)
        self.render('admin/main_news.html', news=news, pagination=None)


class main_news_detail(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = int(self.get_argument("id", 0))
        news = self.application.db.get('select * from MainNews where id=%s', id)
        if not news:
            news = {'id': 0, 'ch_title': '', 'ch_author': '', 'en_title': '', 'en_author': ''}
        self.render('admin/main_news_detail.html', news=news)

    @tornado.web.authenticated
    def post(self):
        id = int(self.get_argument('id', 0))
        ch_title = self.get_argument('ch_title', '')
        en_title = self.get_argument('en_title', '')
        ch_author = self.get_argument('ch_author', '')
        en_author = self.get_argument('en_author', '')

        news = self.application.db.get('select * from MainNews where id=%s', id)
        if news:
            sql = '''update MainNews set ch_title=%s,ch_author=%s,en_title=%s,en_author=%s where id=%s'''
            params = [ch_title, ch_author, en_title, en_author, id]
        else:
            sql = '''insert into MainNews (ch_title,ch_author,en_title,en_author,ch_content,en_content,cover,state) values(%s,%s,%s,%s,'','','',0)'''
            params = [ch_title, ch_author, en_title, en_author]

        ret = self.application.db.execute(sql, *params)
        self.redirect('/manage/main_news')


class main_news_state(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id, state):
        ret = self.application.db.execute('update MainNews set state=%s where id=%s', state, id)
        self.redirect('/manage/main_news')


class main_news_content(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        lang = self.get_argument('lang', 'ch')
        news = self.application.db.get('select * from MainNews where id=%s', id)
        if not news:
            self.redirect('/manage/main_news')
        else:
            self.render('admin/main_news_content.html', news=news, lang=lang)

    @tornado.web.authenticated
    def post(self, id):
        lang = self.get_argument('lang', 'cn')
        content = self.get_argument('html', '')

        news = self.application.db.get('select * from MainNews where id=%s', id)
        if news:
            if lang == 'cn':
                sql = 'update MainNews set ch_content=%s where id=%s'
            else:
                sql = 'update MainNews set en_content=%s where id=%s'

            ret = self.application.db.execute(sql, content, id)
            self.redirect('/manage/main_news')
        else:
            self.redirect('/manage/main_news')


class design_carousel(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        carousels = self.application.db.query('select * from designCarousel  order by sort asc')

        self.render('admin/design_carousel.html', carousels=carousels)


class design_carousel_detail(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = int(self.get_argument("id", 0))
        slider = self.application.db.get('select * from designCarousel where id=%s', id)
        self.render('admin/design_carousel_detail.html', slider=slider)

    @tornado.web.authenticated
    def post(self):
        id = int(self.get_argument("id", 0))
        ch_title = self.get_argument("ch_title")
        en_title = self.get_argument("en_title")
        web_cover = self.get_argument("web_cover")
        wap_cover = ''

        ret = self.application.db.execute(
            'update designCarousel set ch_title=%s,en_title=%s,web_cover=%s,wap_cover=%s where id=%s', ch_title,
            en_title,
            web_cover, wap_cover, id)

        self.redirect('/manage/design_carousel')


class design_carousel_state(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id, state):
        ret = self.application.db.execute('update designCarousel set state=%s where id=%s', state, id)
        self.redirect('/manage/design_carousel')


class design_carousel_sort(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id, move):
        slider = self.application.db.get('select * from designCarousel where id=%s', id)

        if (slider.sort == 1 and move == 'up') or (slider.sort == 4 and move == 'down'):
            pass
        else:
            if move == 'up':
                tmp_s = self.application.db.get('select * from designCarousel where sort=%s', slider.sort - 1)
                self.application.db.execute('update designCarousel set sort=%s where id=%s', slider.sort - 1, slider.id)
                self.application.db.execute('update designCarousel set sort=%s where id=%s', tmp_s.sort + 1, tmp_s.id)
            else:
                tmp_s = self.application.db.get('select * from designCarousel where sort=%s', slider.sort + 1)
                self.application.db.execute('update designCarousel set sort=%s where id=%s', slider.sort + 1, slider.id)
                self.application.db.execute('update designCarousel set sort=%s where id=%s', tmp_s.sort - 1, tmp_s.id)
        self.redirect('/manage/design_carousel')


class design_news(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        start = 0
        ps = 50
        page = int(self.get_argument("page", 0))

        if page == 0:
            ps = 50
        else:
            start = ps * page
        news = self.application.db.query('select * from designNews order by create_time desc limit %s,%s',
                                         start, ps)
        self.render('admin/design_news.html', news=news, pagination=None)


class design_news_detail(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = int(self.get_argument("id", 0))
        news = self.application.db.get('select * from designNews where id=%s', id)
        if not news:
            news = {'id': 0, 'ch_title': '', 'ch_author': '', 'en_title': '', 'en_author': ''}
        self.render('admin/design_news_detail.html', news=news)

    @tornado.web.authenticated
    def post(self):
        id = int(self.get_argument('id', 0))
        ch_title = self.get_argument('ch_title', '')
        en_title = self.get_argument('en_title', '')
        ch_author = self.get_argument('ch_author', '')
        en_author = self.get_argument('en_author', '')

        news = self.application.db.get('select * from designNews where id=%s', id)
        if news:
            sql = '''update designNews set ch_title=%s,ch_author=%s,en_title=%s,en_author=%s where id=%s'''
            params = [ch_title, ch_author, en_title, en_author, id]
        else:
            sql = '''insert into designNews (ch_title,ch_author,en_title,en_author,ch_content,en_content,cover,state) values(%s,%s,%s,%s,'','','',0)'''
            params = [ch_title, ch_author, en_title, en_author]

        ret = self.application.db.execute(sql, *params)
        self.redirect('/manage/design_news')


class design_news_state(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id, state):
        ret = self.application.db.execute('update designNews set state=%s where id=%s', state, id)
        self.redirect('/manage/design_news')


class design_news_content(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        lang = self.get_argument('lang', 'ch')
        news = self.application.db.get('select * from designNews where id=%s', id)
        if not news:
            self.redirect('/manage/design_news')
        else:
            self.render('admin/design_news_content.html', news=news, lang=lang)

    @tornado.web.authenticated
    def post(self, id):
        lang = self.get_argument('lang', 'cn')
        content = self.get_argument('html', '')

        news = self.application.db.get('select * from designNews where id=%s', id)
        if news:
            if lang == 'cn':
                sql = 'update designNews set ch_content=%s where id=%s'
            else:
                sql = 'update designNews set en_content=%s where id=%s'

            ret = self.application.db.execute(sql, content, id)
            self.redirect('/manage/design_news')
        else:
            self.redirect('/manage/design_news')


class design_project(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        start = 0
        ps = 50
        page = int(self.get_argument("page", 0))

        if page == 0:
            ps = 50
        else:
            start = ps * page
        project = self.application.db.query('select * from DesignProject order by create_time desc limit %s,%s',
                                            start, ps)
        self.render('admin/design_project.html', project=project, pagination=None)


class design_project_detail(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = int(self.get_argument("id", 0))
        project = self.application.db.get('select * from DesignProject where id=%s', id)
        if not project:
            project = {'id'        : 0, 'ch_title': '', 'ch_author': '', 'en_title': '', 'en_author': '', 'cover': '',
                       'ch_content': '', 'en_content': ''}
        self.render('admin/design_project_detail.html', project=project)

    @tornado.web.authenticated
    def post(self):
        id = int(self.get_argument('id', 0))
        ch_title = self.get_argument('ch_title', '')
        en_title = self.get_argument('en_title', '')
        ch_author = self.get_argument('ch_author', '')
        en_author = self.get_argument('en_author', '')
        cover = self.get_argument('cover', '')

        project = self.application.db.get('select * from DesignProject where id=%s', id)
        if project:
            sql = '''update DesignProject set ch_title=%s,ch_author=%s,en_title=%s,en_author=%s,cover=%s where id=%s'''
            params = [ch_title, ch_author, en_title, en_author, cover, id]
        else:
            sql = '''insert into DesignProject (ch_title,ch_author,en_title,en_author,ch_content,en_content,cover,state) values(%s,%s,%s,%s,'','','',0)'''
            params = [ch_title, ch_author, en_title, en_author]

        ret = self.application.db.execute(sql, *params)
        self.redirect('/manage/design_project')


class design_project_state(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id, state):
        ret = self.application.db.execute('update DesignProject set state=%s where id=%s', state, id)
        self.redirect('/manage/design_project')


class design_project_content(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        lang = self.get_argument('lang', 'ch')
        project = self.application.db.get('select * from designproject where id=%s', id)
        if not project:
            self.redirect('/manage/design_project')
        else:
            self.render('admin/design_project_content.html', project=project, lang=lang)

    @tornado.web.authenticated
    def post(self, id):
        lang = self.get_argument('lang', 'cn')
        content = self.get_argument('html', '')

        project = self.application.db.get('select * from designproject where id=%s', id)
        if project:
            if lang == 'cn':
                sql = 'update designproject set ch_content=%s where id=%s'
            else:
                sql = 'update designproject set en_content=%s where id=%s'

            ret = self.application.db.execute(sql, content, id)
            self.redirect('/manage/design_project')
        else:
            self.redirect('/manage/design_project')


class design_project_pictures(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        project = self.application.db.get('select * from designproject where id=%s', id)
        if not project:
            self.redirect('/manage/design_project')
        else:
            pictures = []
            if project.pictures:
                pictures = eval(project.pictures)

            self.render('admin/design_project_pictures.html', project=project, pictures=pictures)

    @tornado.web.authenticated
    def post(self, id):
        pictures = self.get_argument('pictures', '')
        print pictures
        if pictures:
            pictures = pictures.split(',')
        else:
            pictures = []

        project = self.application.db.get('select * from designproject where id=%s', id)
        if project:
            print pictures
            pics = str(pictures if pictures[0] else pictures[1:])

            sql = 'update designproject set pictures=%s where id=%s'

            ret = self.application.db.execute(sql, pics, id)
            self.redirect('/manage/design_project')
        else:
            self.redirect('/manage/design_project')


class events(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        start = 0
        ps = 50
        page = int(self.get_argument("page", 0))

        if page == 0:
            ps = 50
        else:
            start = ps * page
        events = self.application.db.query('select * from Events order by create_time desc limit %s,%s',
                                           start, ps)
        self.render('admin/events.html', events=events, pagination=None)


class events_detail(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = int(self.get_argument("id", 0))
        events = self.application.db.get('select * from Events where id=%s', id)
        if not events:
            events = {'id': 0, 'ch_title': '', 'en_title': '', 'web_cover': ''}
        self.render('admin/events_detail.html', events=events)

    @tornado.web.authenticated
    def post(self):
        id = int(self.get_argument('id', 0))
        ch_title = self.get_argument('ch_title', '')
        en_title = self.get_argument('en_title', '')
        web_cover = self.get_argument('web_cover', '')

        events = self.application.db.get('select * from Events where id=%s', id)
        if events:
            sql = '''update Events set ch_title=%s,en_title=%s,web_cover=%s where id=%s'''
            params = [ch_title, en_title, web_cover, id]
        else:
            sql = '''insert into Events (ch_title,en_title,web_cover,wap_cover,ch_content,en_content,state) values(%s,%s,%s,'','','',0)'''
            params = [ch_title, en_title, web_cover]
        print sql, params
        ret = self.application.db.execute(sql, *params)
        self.redirect('/manage/events')


class events_state(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id, state):
        ret = self.application.db.execute('update Events set state=%s where id=%s', state, id)
        self.redirect('/manage/events')


class events_content(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id):
        lang = self.get_argument('lang', 'ch')
        events = self.application.db.get('select * from Events where id=%s', id)
        if not events:
            self.redirect('/manage/events')
        else:
            self.render('admin/events_content.html', events=events, lang=lang)

    @tornado.web.authenticated
    def post(self, id):
        lang = self.get_argument('lang', 'cn')
        content = self.get_argument('html', '')

        news = self.application.db.get('select * from Events where id=%s', id)
        if news:
            if lang == 'cn':
                sql = 'update Events set ch_content=%s where id=%s'
            else:
                sql = 'update Events set en_content=%s where id=%s'

            ret = self.application.db.execute(sql, content, id)
            self.redirect('/manage/events')
        else:
            self.redirect('/manage/events')


class emembers(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = int(self.get_argument('id', 0))
        start = 0
        ps = 50
        page = int(self.get_argument("page", 0))

        if page == 0:
            ps = 50
        else:
            start = ps * page

        emembers = self.application.db.query('select * from eventmember where event_id=%s order by create_time asc', id)
        self.render('admin/emembers.html', emembers=emembers, pagination=None)


class contacts(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        start = 0
        ps = 1000
        page = int(self.get_argument("page", 0))

        if page == 0:
            ps = 1000
        else:
            start = ps * page
        contacts = self.application.db.query('select * from Contact order by create_time desc limit %s,%s',
                                             start, ps)
        self.render('admin/contact.html', contacts=contacts, pagination=None)


class hotword(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        hotword = self.application.db.query('select * from HotWord')
        self.render('admin/hotword.html', hotword=hotword)


class hotword_detail(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = int(self.get_argument("id", 0))
        hotword = self.application.db.get('select * from HotWord where id=%s', id)
        if not hotword:
            hotword = {'id': 0, 'ch_title': '', 'en_title': ''}
        self.render('admin/hotword_detail.html', hotword=hotword)

    @tornado.web.authenticated
    def post(self):
        id = int(self.get_argument('id', 0))
        ch_title = self.get_argument('ch_title', '')
        en_title = self.get_argument('en_title', '')

        hotword = self.application.db.get('select * from HotWord where id=%s', id)
        if hotword:
            sql = '''update HotWord set ch_title=%s,en_title=%s where id=%s'''
            params = [ch_title, en_title, id]
        else:
            sql = '''insert into HotWord (ch_title,en_title,state) values(%s,%s,0)'''
            params = [ch_title, en_title]

        ret = self.application.db.execute(sql, *params)
        self.redirect('/manage/hotword')


class hotword_state(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id, state):
        ret = self.application.db.execute('update HotWord set state=%s where id=%s', state, id)
        self.redirect('/manage/hotword')


class main_about(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        rows = self.application.db.query('select * from AppleOther where style=0 and state=1 order by sort asc')
        self.render('admin/appleother.html', rows=rows, s=0)


class main_contact(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        rows = self.application.db.query('select * from AppleOther where style=1 and state=1 order by sort asc')
        self.render('admin/appleother.html', rows=rows, s=1)


class design_history(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        rows = self.application.db.query('select * from AppleOther where style=2 and state=1 order by sort asc')
        self.render('admin/appleother.html', rows=rows, s=2)


class design_about(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        rows = self.application.db.query('select * from AppleOther where style=3 and state=1 order by sort asc')
        self.render('admin/appleother.html', rows=rows, s=3)


class design_contact(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        rows = self.application.db.query('select * from AppleOther where style=4 and state=1 order by sort asc')
        self.render('admin/appleother.html', rows=rows, s=4)


class appleother_detail(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self):
        id = int(self.get_argument("id", 0))
        s = int(self.get_argument("s", 0))

        other = self.application.db.get('select * from AppleOther where id=%s', id)

        if other:
            other.ch_content = other.ch_content.replace('<br/>', '\r\n').replace('<br/>', '\n')
            other.en_content = other.en_content.replace('<br/>', '\r\n').replace('<br/>', '\n')
        else:
            other = {'id'   : 0, 'ch_title': '', 'en_title': '', 'ch_content': '', 'en_content': '', 'color': 0,
                     'stype': 0, 'wap_cover': '', 'web_cover': ''}
        self.render('admin/appleother_detail.html', other=other, s=s)

    @tornado.web.authenticated
    def post(self):
        id = int(self.get_argument("id", 0))
        style = int(self.get_argument("s", 0))
        stype = int(self.get_argument("stype", 0))
        color = int(self.get_argument("color", 0))

        ch_title = self.get_argument("ch_title")
        en_title = self.get_argument("en_title")
        web_cover = self.get_argument("web_cover")
        wap_cover = self.get_argument("wap_cover")
        ch_content = self.get_argument("ch_content")
        en_content = self.get_argument("en_content")

        other = self.application.db.get('select * from AppleOther where id=%s', id)
        if other:
            sql = '''update AppleOther set ch_title=%s,en_title=%s,web_cover=%s,wap_cover=%s,ch_content=%s,en_content=%s,stype=%s,color=%s where id=%s'''
            params = [ch_title, en_title, web_cover, wap_cover, ch_content, en_content, stype, color, id]
            style = other.style

        else:
            c = self.application.db.query('select count(0) as c from AppleOther where  style=%s', style)
            count = int(c[0]['c']) + 1
            sql = '''insert into AppleOther (ch_title,en_title,web_cover,wap_cover,ch_content,en_content,stype,color,style,sort) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            params = [ch_title, en_title, web_cover, wap_cover, ch_content, en_content, stype, color, style, count]

        ret = self.application.db.execute(sql, *params)

        url = '/manage/' + ['main_about', 'main_contact', 'design_history', 'design_about', 'design_contact'][style]

        self.redirect(url)


class appleother_state(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id, state):
        ret = self.application.db.execute('update AppleOther set state=%s where id=%s', state, id)

        other = self.application.db.get('select * from AppleOther where id=%s', id)

        url = '/manage/' + ['main_about', 'main_contact', 'design_history', 'design_about', 'design_contact'][
            other['style']]

        self.redirect(url)


class appleother_sort(ManageBaseHandler):
    @tornado.web.authenticated
    def get(self, id, move):
        ao = self.application.db.get('select * from AppleOther where id=%s', id)

        first_sort = self.application.db.get(
            'select * from AppleOther where state=1 and style=%s order by sort asc limit 1', ao['style'])
        last_sort = self.application.db.get(
            'select * from AppleOther where state=1 and style=%s order by sort desc limit 1', ao['style'])

        if (ao.sort == first_sort.sort and move == 'up') or (ao.sort == last_sort.sort and move == 'down'):
            pass
        else:

            if move == 'up':
                tmp_s = self.application.db.get('select * from AppleOther where state=1 and sort=%s and style=%s',
                                                int(ao.sort) - 1, ao.style)

                self.application.db.execute('update AppleOther set sort=%s where id=%s', int(ao.sort) - 1, ao.id)
                self.application.db.execute('update AppleOther set sort=%s where id=%s', int(tmp_s.sort) + 1, tmp_s.id)
            else:
                tmp_s = self.application.db.get('select * from AppleOther where state=1 and sort=%s and style=%s',
                                                int(ao.sort) + 1, ao.style)

                self.application.db.execute('update AppleOther set sort=%s where id=%s', int(ao.sort) + 1, ao.id)
                self.application.db.execute('update AppleOther set sort=%s where id=%s', int(tmp_s.sort) - 1, tmp_s.id)
        url = '/manage/' + ['main_about', 'main_contact', 'design_history', 'design_about', 'design_contact'][
            ao['style']]

        self.redirect(url)
