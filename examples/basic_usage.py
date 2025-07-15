"""
Basic usage example for YaoLogit
"""

from yaologit import get_logger

def main():
    # Get logger instance with default configuration
    logger = get_logger()
    
    # Log messages at different levels
    logger.trace("This is a trace message (most detailed)")
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.success("This is a success message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
    # Log with additional context
    logger.info("User logged in", user_id=123, ip_address="192.168.1.1")
    
    # Log with exception information
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("An error occurred during calculation")
    
    # Using bind for context
    user_logger = logger.bind(user_id=456)
    user_logger.info("User action performed")
    user_logger.warning("User quota exceeded")
    
    print("\nCheck the logs directory for generated log files!")

if __name__ == "__main__":
    main()