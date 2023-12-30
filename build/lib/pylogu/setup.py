from setuptools import setup, find_packages

setup(
    name='pylogu',
    version='0.2.3',
    packages=['pylogu', 'pylogu.core'],
    install_requires=['httpx>=0.18.2'],
    python_requires='>=3.7',
    description='Logu - Python SDK',
    author='Kevin Saltarelli',
    author_email='kevinqz@gmail.com',
    url='https://github.com/kevinqz/pylogu',
)
