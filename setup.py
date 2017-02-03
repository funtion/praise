try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='praise',
    packages=['praise'],
    version='0.1',
    description='Praise it',
    author='Shufang Xie',
    author_email='xieshufang76@gmail.com',
    url='https://github.com/funtion/praise',
    download_url='https://github.com/funtion/praise/0.1',
    keywords=['praise', 'logging'],
    classifiers=[],
    test_suite='nose.collector',
    tests_require=['nose']
)
