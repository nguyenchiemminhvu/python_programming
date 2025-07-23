from setuptools import setup, find_packages

setup(
    name='setuptools_example',
    version='0.1.0',
    description='An example package to demonstrate setuptools usage',
    long_description=open('README.md').read(),
    author='Vu Nguyen',
    author_email="nguyenchiemminhvu@gmail.com",
    license=open('LICENSE').read(),
    packages=["setuptools_example"],
    install_requires=[
        'wheel',
        'setuptools'
    ],
    url="https://github.com/nguyenchiemminhvu/python_programming/tree/main/study/setuptools"
)