import tornado.web
from views import index
import config


class Application(tornado.web.Application):

    def __init__(self):

        handlers = [
            (r'/',index.IndexHandler),
            (r'/aa',index.AsdHandler,{'a':'a','b':'b'}),
            (r'/json',index.JsonHandler),
            (r'/json2', index.Json2Handler),
            (r'/header',index.HeaderHandler),
            (r'/status',index.StatusHandler),
            (r'/index',index.RedirectHandler),
            (r'/iserror',index.ErrorHandler),
            tornado.web.url(r'/rongge',index.RgHandler,{'c':'c','d':'d'},name='rg'),
            (r'/liuyifei/(\w+)/(\w+)',index.LiuyifeiHandler),
            (r'/zhanmanyu',index.ZhanmanyuHandler),
        ]

        super(Application,self).__init__(handlers,**config.settings)

#xiugai