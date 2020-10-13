import logging.handlers, os


def log_conf():
    # 日志文件位置
    logpath = './Log'
    # 日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 处理器-控制台
    sh = logging.StreamHandler()
    # 处理器-文件
    fh = logging.handlers.TimedRotatingFileHandler(filename=logpath + os.sep + 'mini.log',
                                                   when='midnight', interval=1,
                                                   backupCount=7, encoding='utf-8')
    # 格式化字符串
    f = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    # 格式化器
    formatter = logging.Formatter(f)

    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)


# 请求通用地址
base_url = 'http://e.cn/api/v1'

# 微信code
code = '0115cC0w30978V2G8m1w3bnfjS25cC0J'

# 请求头

headers = {
    "Content-Type": "application/json",
    "token": 'e20e2708a45b574ed2dfc816d9abe4a7'
}
