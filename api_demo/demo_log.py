import logging
import time


class DemoLog:

    def log(self):
        #创建一个日志器
        logger = logging.getLogger("logger")
        logger.setLevel(logging.DEBUG)
        #处理器
        sh = logging.StreamHandler()
        #文件处理器
        fh = logging.FileHandler(filename='log/{}_log'.format(time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())),
                                 encoding='utf-8')
        #格式器
        formator = logging.Formatter(fmt='%(asctime)s %(filename)s %(levelname)s %(message)s',
                                     datefmt='%Y/%m/%d/%X')

        sh.setFormatter(formator)
        fh.setFormatter(formator)
        logger.addHandler(sh)
        logger.addHandler(fh)
        logger.debug('debug 信息')
        logger.error('error 信息')
        logger.info('info 信息')
        logger.warning('warn 信息')
        logger.critical('critical 信息')

DemoLog().log()