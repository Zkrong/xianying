import os
BASE_DIRS = os.path.dirname(__file__)


#参数
options= {
    'port':8008,
    'list':['dafa','dsa','asda']
}


#配置
settings = {
    'debug':True,
    'static_path':os.path.join(BASE_DIRS,"static"),
    'templates':os.path.join(BASE_DIRS,"templates")
}