# YaoLogit

[![Python Version](https://img.shields.io/pypi/pyversions/yaologit.svg)](https://pypi.org/project/yaologit/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

YaoLogit is a process-safe logging package built on top of [loguru](https://github.com/Delgan/loguru) that ensures only one logger instance is created per Python process, including subprocesses. It provides a simple, powerful, and thread-safe logging solution for Python applications.

## Features

- **Process-Safe Singleton**: Ensures only one logger instance across all processes and subprocesses
- **Thread-Safe**: Uses loguru's `enqueue` parameter for thread-safe logging
- **Automatic Log Rotation**: Built-in support for time-based and size-based log rotation
- **Log Compression**: Automatic compression of rotated logs
- **Flexible Configuration**: Configure via code, environment variables, or configuration files
- **Multiple Log Levels**: Separate log files for different log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- **Easy Integration**: Drop-in replacement for standard logging with minimal code changes
- **Cross-Platform**: Works on Windows, Linux, and macOS

## Installation

Install YaoLogit using pip:

```bash
pip install yaologit
```

## Quick Start

### Basic Usage

```python
from yaologit import get_logger

# Get logger instance
logger = get_logger()

# Log messages
logger.info("This is an info message")
logger.debug("This is a debug message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

### Custom Configuration

```python
from yaologit import get_logger

# Configure logger with custom settings
logger = get_logger(
    name="myapp",
    log_dir="./logs",
    verbose=True,
    rotation="100 MB",
    retention="30 days",
    compression="zip"
)

logger.info("Logger configured with custom settings")
```

### Advanced Configuration

```python
from yaologit import YaoLogit, YaoLogitConfig

# Create custom configuration
config = YaoLogitConfig(
    name="myapp",
    log_dir="./logs",
    levels=["INFO", "WARNING", "ERROR"],
    separate_by_level=True,
    rotation="1 day",
    retention="7 days",
    compression="gz",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>"
)

# Initialize YaoLogit
YaoLogit.configure(config)
logger = YaoLogit.get_logger()

logger.info("Advanced configuration applied")
```

### Environment Variables

YaoLogit can be configured using environment variables:

```bash
export YAOLOGIT_NAME=myapp
export YAOLOGIT_LOG_DIR=/var/log/myapp
export YAOLOGIT_VERBOSE=true
export YAOLOGIT_ROTATION="100 MB"
export YAOLOGIT_RETENTION="30 days"
export YAOLOGIT_LEVELS="INFO,WARNING,ERROR"
```

Then in your code:

```python
from yaologit import YaoLogit, YaoLogitConfig

# Load configuration from environment
config = YaoLogitConfig.from_env()
YaoLogit.configure(config)
logger = YaoLogit.get_logger()
```

### Context Manager

Use context managers for temporary logging contexts:

```python
from yaologit import YaoLogit

YaoLogit.configure()

with YaoLogit.session("data_processing", user_id=12345) as logger:
    logger.info("Processing started")
    # ... do processing ...
    logger.info("Processing completed")
```

### Multiprocessing Example

YaoLogit ensures consistent logging across multiple processes:

```python
import multiprocessing
from yaologit import get_logger

def worker_function(worker_id):
    # Each process will use the same logger instance
    logger = get_logger("myapp")
    logger.info(f"Worker {worker_id} started")
    # ... do work ...
    logger.info(f"Worker {worker_id} finished")

if __name__ == "__main__":
    # Initialize logger in main process
    logger = get_logger("myapp", log_dir="./logs")
    logger.info("Main process started")
    
    # Create worker processes
    processes = []
    for i in range(4):
        p = multiprocessing.Process(target=worker_function, args=(i,))
        p.start()
        processes.append(p)
    
    # Wait for all processes to complete
    for p in processes:
        p.join()
    
    logger.info("All workers completed")
```

## Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `name` | str | "yaologit" | Logger name |
| `log_dir` | str/Path | "./logs" | Directory for log files |
| `verbose` | bool | True | Enable console output |
| `levels` | List[str] | ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] | Log levels to handle |
| `separate_by_level` | bool | True | Create separate files for each log level |
| `enqueue` | bool | True | Enable thread-safe logging |
| `rotation` | str | "1 day" | When to rotate log files |
| `retention` | str | "7 days" | How long to keep old logs |
| `compression` | str | "zip" | Compression format for rotated logs |
| `format` | str | (see below) | Log message format |
| `console_output` | bool | True | Enable console output |
| `console_level` | str | "INFO" | Minimum level for console output |

### Default Format

```
<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>
```

## API Reference

### `get_logger(name=None, log_dir=None, verbose=True, **kwargs)`

Get a logger instance with the specified configuration.

**Parameters:**
- `name` (str, optional): Logger name
- `log_dir` (str, optional): Log directory path
- `verbose` (bool): Enable console output
- `**kwargs`: Additional configuration options

**Returns:**
- `loguru.Logger`: Logger instance

### `YaoLogit.configure(config=None, **kwargs)`

Configure the YaoLogit singleton.

**Parameters:**
- `config` (YaoLogitConfig, optional): Configuration object
- `**kwargs`: Configuration options to override

**Returns:**
- `YaoLogit`: YaoLogit instance

### `YaoLogit.get_logger()`

Get the configured logger instance.

**Returns:**
- `loguru.Logger`: Logger instance

**Raises:**
- `LoggerNotInitializedError`: If logger not configured

### `YaoLogit.session(name, **kwargs)`

Create a temporary logging context.

**Parameters:**
- `name` (str): Session name
- `**kwargs`: Additional context data

**Yields:**
- `loguru.Logger`: Contextualized logger

## Development

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/yourusername/yaologit.git
cd yaologit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### Running tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=yaologit

# Run specific test file
pytest tests/test_core.py
```

### Code formatting

```bash
# Format code with black
black yaologit tests

# Check code style
flake8 yaologit tests

# Type checking
mypy yaologit
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built on top of the excellent [loguru](https://github.com/Delgan/loguru) library
- Inspired by the need for process-safe logging in multiprocessing applications

## Changelog

### 0.1.0 (2025-01-11)
- Initial release
- Process-safe singleton implementation
- Thread-safe logging with loguru
- Automatic log rotation and compression
- Flexible configuration system
- Support for multiple log levels
- Environment variable configuration
- Context manager support