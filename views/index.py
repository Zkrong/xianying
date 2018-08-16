import tornado.web
from tornado.web import RequestHandler



class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        url = self.reverse_url('rg')
        self.write("<a href='%s'>sdadf<a>"%(url))


class AsdHandler(RequestHandler):
    def initialize(self,a,b):
        self.a = a
        self.b = b

    def get(self):
        print(self.a,self.b)
        self.write('mmm')


import json
class JsonHandler(RequestHandler):
    def get(self,*args,**kwargs):
        per = {
            'as':'as',
            'cxc':'asa'
        }

        jsonStr = json.dumps(per)
        self.set_header("Content-Type","application/json;charset=UTF-8")
        self.set_header('sunck','good')
        self.write(jsonStr)

class Json2Handler(RequestHandler):
    def get(self,*args,**kwargs):
        per = {
            'as':'as',
            'cxc':'asa'
        }
        self.write(per)

class HeaderHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type','text/html;charset=UTF-8')

    def get(self):
        pass

class StatusHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(999)
        self.write('*******')


class RedirectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect('/')


class ErrorHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            code = 500
            self.write('服务器内部错误')
        elif status_code ==404:
            code = 404
            self.write('资源不存在')
        self.set_status(code)

    def get(self, *args, **kwargs):
        flag = self.get_query_argument('flag')
        if flag == '0':
            self.send_error(500)
        self.write('right')


class RgHandler(RequestHandler):
    def initialize(self,c,d):
        self.c = c
        self.d = d
    def get(self, *args, **kwargs):
        print(self.c,self.d)
        self.write('rg shuai')


class LiuyifeiHandler(RequestHandler):
    def get(self, h1,h2,*args,**kwargs):
        # print(h1,h2)
        print(h1)
        self.write('liu is nice')

class ZhanmanyuHandler(RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_argument('a')
        b = self.get_query_argument('b')
        c = self.get_query_argument('c')
        print(a,b,c)
        self.write('zhanmanyu nice')