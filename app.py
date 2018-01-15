# -*- coding:utf8 -*-:
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import torndb
import os.path
from ConfigParser import ConfigParser

from tornado.options import define, options

from app.modules.home import HomeIndex, HomeEvents, HomeEvent, HomeAbout, HomeContact, HomeWOW, HomeNews, HomeNewsd, \
    HomeSearch

from app.modules.design import DesignIndex, DesignProjects, DesignProject, DesignAbout1, DesignAbout2, DesignBlogs, \
    DesignBlog, DesignContact, DesignSearch

from app.modules.manage import MIndex, LogoutHandler, LoginHandler, ChangePasswordHandler, main_carousel, \
    main_carousel_detail, main_carousel_state, main_carousel_sort, main_entrance, main_entrance_detail, \
    main_news, main_news_detail, main_news_content, main_news_state, design_carousel, design_carousel_detail, \
    design_carousel_sort, design_carousel_state, design_news, design_news_content, design_news_detail, \
    design_news_state, design_project, design_project_content, design_project_detail, design_project_state, \
    design_project_pictures, emembers, events, events_content, events_detail, events_state, contacts, hotword, \
    hotword_detail, hotword_state, main_about, main_contact, design_about, design_contact, design_history, \
    appleother_detail, appleother_state, appleother_sort

from app.api.api import MainSearch, DesignSearch as api_DesignSearch, Events as api_events, Contact as api_contact

from app.modules.img import ImageHandler, UploadHandler, DeleteHandler

define("port", default=8000, help="run on the given port", type=int)
define("dev", type=bool, help="dev mode switch", default=True)
define("config", default="", help="config file", type=str)


class Application(tornado.web.Application):
    def __init__(self):
       
        handlers = [
            (r"/upload", UploadHandler),

            (r"/([^/]+)", HomeIndex, None, 'main_index'),
            (r"/([^/]+)/event", HomeEvents, None, 'main_events'),
            (r"/([^/]+)/event/([^/]+)", HomeEvent, None, 'main_event'),
            (r"/([^/]+)/about-us", HomeAbout, None, 'main_about'),
            (r"/([^/]+)/contact", HomeContact, None, 'main_contact'),
            (r"/([^/]+)/wow", HomeWOW, None, 'main_wow'),
            (r"/([^/]+)/news", HomeNews, None, 'main_news'),
            (r"/([^/]+)/news/([^/]+)", HomeNewsd, None, 'main_newsd'),
            (r"/([^/]+)/search", HomeSearch, None, 'main_search'),

        ]

        design_handlers = [
            (r"/design/([^/]+)", DesignIndex, None, 'design_index'),
            (r"/design/([^/]+)/projects", DesignProjects, None, 'design_projects'),
            (r"/design/([^/]+)/project/([^/]+)", DesignProject, None, 'design_project'),
            (r"/design/([^/]+)/what-we-do", DesignAbout1, None, 'design_about1'),
            (r"/design/([^/]+)/who-we-are", DesignAbout2, None, 'design_about2'),
            (r"/design/([^/]+)/blog", DesignBlogs, None, 'design_blogs'),
            (r"/design/([^/]+)/blog/([^/]+)", DesignBlog, None, 'design_blog'),
            (r"/design/([^/]+)/contact", DesignContact, None, 'design_contact'),
            (r"/design/([^/]+)/search", DesignSearch, None, 'design_search'),
        ]

        manage_handlers = [
            (r"/manage/index", MIndex, None, 'manage_index'),

            (r"/manage/main_carousel", main_carousel, None, 'manage_main_carousel'),
            (r"/manage/main_carousel_detail/add", main_carousel_detail, None, 'manage_main_carousel_detail'),
            (r"/manage/main_carousel_state/([^/]+)/([^/]+)", main_carousel_state, None, 'manage_main_carousel_state'),
            (r"/manage/main_carousel_sort/([^/]+)/sort/([^/]+)", main_carousel_sort, None, 'manage_main_carousel_sort'),

            (r"/manage/main_entrance", main_entrance, None, 'manage_main_entrance'),
            (r"/manage/main_entrance_detail", main_entrance_detail, None, 'manage_main_entrance_detail'),

            (r"/manage/main_news", main_news, None, 'manage_main_news'),
            (r"/manage/main_news_detail", main_news_detail, None, 'manage_main_news_detail'),
            (r"/manage/main_news_content/([^/]+)/content", main_news_content, None, 'manage_main_news_content'),
            (r"/manage/main_news_state/([^/]+)/([^/]+)", main_news_state, None, 'manage_main_news_state'),

            (r"/manage/design_carousel", design_carousel, None, 'manage_design_carousel'),
            (r"/manage/design_carousel_detail/add", design_carousel_detail, None, 'manage_design_carousel_detail'),
            (r"/manage/design_carousel_state/([^/]+)/([^/]+)", design_carousel_state, None,
             'manage_design_carousel_state'),
            (r"/manage/design_carousel_sort/([^/]+)/sort/([^/]+)", design_carousel_sort, None,
             'manage_design_carousel_sort'),

            (r"/manage/design_news", design_news, None, 'manage_design_news'),
            (r"/manage/design_news_detail", design_news_detail, None, 'manage_design_news_detail'),
            (r"/manage/design_news_content/([^/]+)/content", design_news_content, None, 'manage_design_news_content'),
            (r"/manage/design_news_state/([^/]+)/([^/]+)", design_news_state, None, 'manage_design_news_state'),

            (r"/manage/design_project", design_project, None, 'manage_design_project'),
            (r"/manage/design_project_detail", design_project_detail, None, 'manage_design_project_detail'),
            (r"/manage/design_project_content/([^/]+)/content", design_project_content, None,
             'manage_design_project_content'),
            (r"/manage/design_project_content/([^/]+)/pictures", design_project_pictures, None,
             'manage_design_project_pictures'),
            (r"/manage/design_project_state/([^/]+)/([^/]+)", design_project_state, None,
             'manage_design_project_state'),

            (r"/manage/events", events, None, 'manage_events'),
            (r"/manage/events_detail", events_detail, None, 'manage_events_detail'),
            (r"/manage/events_content/([^/]+)/content", events_content, None, 'manage_events_content'),
            (r"/manage/events_state/([^/]+)/([^/]+)", events_state, None, 'manage_events_state'),
            (r"/manage/emembers", emembers, None, 'manage_emembers'),

            (r"/manage/contacts", contacts, None, 'manage_contacts'),

            (r"/manage/hotword", hotword, None, 'manage_hotword'),
            (r"/manage/hotword_detail", hotword_detail, None, 'manage_hotword_detail'),
            (r"/manage/hotword_state/([^/]+)/([^/]+)", hotword_state, None, 'manage_hotword_state'),

            (r"/manage/main_about", main_about, None, 'manage_main_about'),
            (r"/manage/main_contact", main_contact, None, 'manage_main_contact'),
            (r"/manage/design_history", design_history, None, 'manage_design_history'),
            (r"/manage/design_about", design_about, None, 'manage_design_about'),
            (r"/manage/design_contact", design_contact, None, 'manage_design_contact'),

            (r"/manage/appleother_detail", appleother_detail, None, 'manage_appleother_detail'),
            (r"/manage/appleother_state/([^/]+)/([^/]+)", appleother_state, None, 'manage_appleother_state'),
            (r"/manage/appleother_sort/([^/]+)/sort/([^/]+)", appleother_sort, None, 'manage_appleother_sort'),

            (r"/manage/change_password", ChangePasswordHandler, None, 'manage_change_password'),
            (r"/manage/login", LoginHandler, None, 'manage_login'),
            (r"/manage/logout", LogoutHandler, None, 'manage_logout'),

        ]

        api_handlers = [
            (r"/api/main_search", MainSearch),
            (r"/api/design_search", api_DesignSearch),
            (r"/api/events", api_events),
            (r"/api/a_contact", api_contact),
            (r"/api/delete_pic", DeleteHandler),
        ]

        img_handlers = [

            (r"/uploads/([^/]+)/([^/]+)", ImageHandler),

        ]

        handlers.extend(design_handlers)
        handlers.extend(manage_handlers)
        handlers.extend(api_handlers)
        handlers.extend(img_handlers)

        self.CP = ConfigParser()
        self.CP.read(options.config)

        #test
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=options.dev,
            cookie_secret="\xa1yn$\x1e\x12\x83\xc7\x0e\xf9u\xba\xddN\xb6k\xbf\xc1\xa0\xa2a\x99\xabJ",
            login_url="/manage/login"
        )

        self.db = torndb.Connection(host=self.CP.get('mysql', 'host') + ':' + self.CP.get('mysql', 'port'),
                                    database=self.CP.get('mysql', 'database'),
                                    user=self.CP.get('mysql', 'user'),
                                    password=self.CP.get('mysql', 'passwd'),
                                    time_zone="+8:00",
                                    )

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
