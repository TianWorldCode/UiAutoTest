import logging
from logging.handlers import TimedRotatingFileHandler
import config


def init_config():
    # 处理器
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # 打印到平台和文件
    fh = TimedRotatingFileHandler(config.LOG_PATH + '/log.log', when='midnight',
                                  interval=1, backupCount=7)
    fh.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    # 设置格式
    fmt = '"%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"'
    formatter = logging.Formatter(fmt=fmt)
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    # 添加到处理器
    logger.addHandler(fh)
    logger.addHandler(sh)

init_config()

