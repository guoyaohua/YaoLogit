#!/usr/bin/env python
"""
Simple script to test YaoLogit installation
"""

import sys
import subprocess
import tempfile
import shutil
from pathlib import Path

def test_package_installation():
    """Test that the package can be installed and imported"""
    print("Testing YaoLogit package installation...")
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Created temporary directory: {temp_dir}")
        
        # Install the package in development mode
        print("\nInstalling package in development mode...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-e", "."],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Installation failed: {result.stderr}")
            return False
        
        print("Installation successful!")
        
        # Test import
        print("\nTesting import...")
        try:
            import yaologit
            print(f"Successfully imported yaologit version {yaologit.__version__}")
        except ImportError as e:
            print(f"Import failed: {e}")
            return False
        
        # Test basic functionality
        print("\nTesting basic functionality...")
        try:
            from yaologit import get_logger
            
            # Create logs in temp directory
            log_dir = Path(temp_dir) / "test_logs"
            logger = get_logger(name="test", log_dir=str(log_dir), verbose=False)
            
            # Log some messages
            logger.info("Test info message")
            logger.warning("Test warning message")
            logger.error("Test error message")
            
            print("Logging successful!")
            
            # Check that log files were created
            if log_dir.exists():
                print(f"\nLog directory created: {log_dir}")
                for item in log_dir.rglob("*.log"):
                    print(f"  - {item.relative_to(log_dir)}")
            
        except Exception as e:
            print(f"Functionality test failed: {e}")
            return False
    
    print("\nAll tests passed! YaoLogit is ready to use.")
    return True

if __name__ == "__main__":
    # Check if we're in the right directory
    if not Path("setup.py").exists():
        print("Error: Please run this script from the YaoLogit project root directory")
        sys.exit(1)
    
    # Run the test
    success = test_package_installation()
    sys.exit(0 if success else 1)