from distutils.core import setup

setup(
    name='Brainy',
    version='0.1.3',
    author='Joel Buchheim-Moore',
    author_email='joelbm24@gmail.com',
    scripts=['bin/brainy'],
    package_dir={'brainy': 'lib'},
    packages=['brainy'],
    url='http://github.com/joelbm24/brainy',
    license='LICENSE.txt',
    description='brainfuck interpreter',
    long_description=open('README.txt').read(),
)
