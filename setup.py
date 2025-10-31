from from setuptools import setup, find_packages

setup(
    name="lekzy-trading-pro",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp==3.9.1",
        "python-telegram-bot==21.4",
        "pandas==1.5.3",
        "numpy==1.24.3",
        "requests==2.31.0",
        "twelvedata==1.4.0",
        "pytz==2024.1"
    ],
    python_requires=">=3.8",
)
