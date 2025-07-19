"""
YaoLogit - A process-safe logging package based on loguru

YaoLogit provides a simple and powerful logging solution that ensures
only one logger instance is created per Python process, including subprocesses.
"""

__version__ = "0.1.0"
__author__ = "Yaohua Guo"
__email__ = "Guo.Yaohua@foxmail.com"

from .core import YaoLogit, get_logger
from .config import YaoLogitConfig
from .exceptions import YaoLogitError, ConfigurationError

__all__ = [
    "YaoLogit",
    "get_logger",
    "YaoLogitConfig",
    "YaoLogitError",
    "ConfigurationError",
]