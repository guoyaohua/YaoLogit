# Changelog

All notable changes to YaoLogit will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-01-11

### Added
- Initial release of YaoLogit
- Process-safe singleton logger implementation based on loguru
- Thread-safe logging using loguru's `enqueue` parameter
- Support for multiple log levels with separate files
- Automatic log rotation and compression
- Configuration via code, environment variables, or config files
- Context manager support for session-based logging
- Multiprocessing support ensuring single logger instance across processes
- Comprehensive test suite
- Full documentation and examples
- Python 3.7+ support

### Features
- **Process-Safe Singleton**: Ensures only one logger instance exists across all processes and subprocesses
- **Thread-Safe**: Built on loguru's thread-safe implementation
- **Flexible Configuration**: Multiple ways to configure the logger
- **Log Rotation**: Time-based and size-based rotation with compression
- **Multiple Output Formats**: Console and file outputs with customizable formats
- **Environment Variable Support**: Configure via environment variables
- **Context Binding**: Add contextual information to log messages
- **Cross-Platform**: Works on Windows, Linux, and macOS

[0.1.0]: https://github.com/yourusername/yaologit/releases/tag/v0.1.0