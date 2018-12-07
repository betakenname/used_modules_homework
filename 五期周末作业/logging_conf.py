
# 级别 时间 模块名称 函数名称 日志消息
standard_format = '[%(levelname)s][%(asctime)s: 模块:%(module)s 函数:%(funcName)s][消息: %(message)s]'

# 日志路径
logfile_path1 = "log.txt"


LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        }
    },
    'filters': {},
    'handlers': {
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path1,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5, #日志文件最大个数
            'encoding': 'utf-8',  # 日志文件的编码
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],  # 这里把上面定义的handler加上
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        },
    },
}