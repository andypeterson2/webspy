from setuptools import setup, find_packages

setup(
    name="WebSpy",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "yagmail",
        "beautifulsoup4",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'webspy = webspy.core:main',
        ],
    },
)