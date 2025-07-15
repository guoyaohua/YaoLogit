# encoding=utf-8
"""
Logger 工具类
"""
import datetime
import os

from loguru import logger


class MyLogger(object):
    """
    一个单例日志记录器类，为应用程序提供日志记录功能。

    Attributes:
        logger (loguru.logger): 用于记录消息的日志记录器实例。
    """

    _instance = None

    @classmethod
    def initialize(cls, name, log_dir, verbose=False):
        if cls._instance is not None:
            return cls._instance
        cls._instance = cls(name, log_dir, verbose)
        return cls._instance

    def __init__(self, name, log_dir, verbose=False):
        """
        初始化日志记录器实例。

        Args:
            name (str): 日志记录器的名称。
            log_dir (str): 日志文件的目录。
            verbose (bool, optional): 是否启用详细日志记录。默认为True。
        """
        self.name = name
        self.log_dir = log_dir
        self.verbose = verbose

        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        if not verbose:
            logger.remove()
        today = datetime.datetime.now().strftime(r"%Y-%m-%d")
        # format="<green>{time:HH:mm:ss:SSSS}</green> | {module} line:{line} {function} |{level} | {message}"
        logger.add(
            os.path.join(log_dir, "DEBUG", f"Debug_{name}_{today}.log"),
            level="DEBUG",
            encoding="utf-8",
            enqueue=True,
        )
        logger.add(
            os.path.join(log_dir, "INFO", f"Info_{name}_{today}.log"),
            level="INFO",
            encoding="utf-8",
            enqueue=True,
        )
        logger.add(
            os.path.join(log_dir, "WARNING", f"Warn_{name}_{today}.log"),
            level="WARNING",
            encoding="utf-8",
            enqueue=True,
        )
        logger.add(
            os.path.join(log_dir, "ERROR", f"Error_{name}_{today}.log"),
            level="ERROR",
            encoding="utf-8",
            enqueue=True,
        )
        logger.add(
            os.path.join(log_dir, "CRITICAL", f"Critical_{name}_{today}.log"),
            level="CRITICAL",
            encoding="utf-8",
            enqueue=True,
        )
        self.logger = logger

    @classmethod
    def remove_instance(cls):
        if cls._instance is not None:
            del cls._instance
        cls._instance = None

    @classmethod
    def get_info(cls):
        if cls._instance is not None:
            return cls._instance.name, cls._instance.log_dir, cls._instance.verbose


def get_logger(name, log_dir="../logs", verbose=False):
    """
    获取一个日志记录器实例。

    Args:
        name (str): 日志记录器的名称。
        log_dir (str, optional): 日志文件的目录。默认为'../logs'。
        verbose (bool, optional): 是否启用详细日志记录。默认为 False。

    Returns:
        loguru.logger: 用于记录消息的日志记录器实例。
    """
    return MyLogger.initialize(name, log_dir, verbose).logger


if __name__ == "__main__":
    logger_1 = get_logger("aaa", log_dir="../logs")
    print(MyLogger.get_info())
    logger_2 = get_logger("bbb", log_dir="../logs")
    print(MyLogger.get_info())
    MyLogger.remove_instance()
    print(MyLogger.get_info())
    logger_3 = get_logger("ccc", log_dir="../logs")
    print(MyLogger.get_info())
    logger_1.info("test message")
    logger_1.warning("test message")
