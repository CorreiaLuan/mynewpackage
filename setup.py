from setuptools import setup
from mynewpackage import __version__

setup(
    name='mynewpackage',
    version=__version__,
    description='My private package from private github repo',
    url='https://github.com/CorreiaLuan/mynewpackage.git',
    author='Luan Correia',
    author_email='luan.a.correia@live.com',
    license='unlicense',
    install_requires=[
        'pandas'
    ],
    packages=['mynewpackage'],
    zip_safe=False
)