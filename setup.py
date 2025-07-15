"""
Setup script for YaoLogit package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="yaologit",
    version="0.1.0",
    author="Yaohua Guo",
    author_email="Guo.Yaohua@foxmail.com",
    description="A process-safe logging package based on loguru",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guoyaohua/yaologit",
    project_urls={
        "Bug Tracker": "https://github.com/guoyaohua/yaologit/issues",
        "Documentation": "https://github.com/guoyaohua/yaologit#readme",
        "Source Code": "https://github.com/guoyaohua/yaologit",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(include=["yaologit", "yaologit.*"]),
    python_requires=">=3.7",
    install_requires=[
        "loguru>=0.7.0",
        "filelock>=3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            # Add any console scripts here if needed
        ],
    },
    keywords="logging, loguru, process-safe, multiprocessing, logger",
    zip_safe=False,
)