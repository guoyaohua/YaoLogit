"""
Migration example: How to migrate from the old logger.py to YaoLogit
"""

print("=== Migration Guide ===\n")

print("OLD CODE (using logger.py):")
print("-" * 50)
print('''
from logger import get_logger

# Old way of getting logger
logger = get_logger("myapp", log_dir="../logs", verbose=False)
logger.info("test message")
logger.warning("test warning")
''')

print("\nNEW CODE (using YaoLogit):")
print("-" * 50)
print('''
from yaologit import get_logger

# New way - almost identical API!
logger = get_logger("myapp", log_dir="../logs", verbose=False)
logger.info("test message")
logger.warning("test warning")
''')

print("\n=== Key Improvements in YaoLogit ===\n")

print("1. Process-Safe Singleton:")
print("   - Ensures only ONE logger instance across all processes")
print("   - No more duplicate log entries from subprocesses")
print("   - Automatic synchronization between processes")

print("\n2. Better Configuration:")
print("   - Configure via environment variables")
print("   - More options for rotation, retention, compression")
print("   - Flexible log formats")

print("\n3. Enhanced Features:")
print("   - Context managers for session logging")
print("   - Better multiprocessing support")
print("   - Automatic cleanup of old logs")

print("\n=== Advanced Migration Example ===\n")

# Demonstrate the actual migration
from yaologit import get_logger, YaoLogit, YaoLogitConfig

# Method 1: Direct replacement (simplest migration)
logger = get_logger("migration_test", log_dir="./migration_logs", verbose=True)
logger.info("This works just like the old logger!")

# Method 2: Using advanced configuration
config = YaoLogitConfig(
    name="advanced_app",
    log_dir="./migration_logs",
    rotation="100 MB",  # Rotate when file reaches 100MB
    retention="30 days",  # Keep logs for 30 days
    compression="zip",   # Compress old logs
    separate_by_level=True,  # Separate files for each level
    console_output=True,
    console_level="INFO"
)

YaoLogit.configure(config)
advanced_logger = YaoLogit.get_logger()

# Log with context
advanced_logger.info("User logged in", user_id=123, ip="192.168.1.1")

# Use context manager for session logging
with YaoLogit.session("data_import", file="data.csv") as session_logger:
    session_logger.info("Starting import")
    session_logger.info("Processing records")
    session_logger.success("Import completed")

print("\n✅ Migration successful! Check ./migration_logs/ for the generated log files.")