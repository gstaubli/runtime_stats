from setuptools import setup

setup(
    name='runtime_stats',
    version='0.1.0',
    author='Garren Staubli',
    author_email='gstaubli@gmail.com',
    packages=['runtime_stats'],
    url='http://www.github.com/gstaubli/runtime_stats',
    description='Python decorator function to track runtime stats on function calls',
    long_description=open('README.md').read(),
    install_requires=[
        "decorator"
    ]
)