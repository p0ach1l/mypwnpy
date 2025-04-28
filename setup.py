from setuptools import setup, find_packages

setup(
    name='pwnscript',
    version='2.0.0',
    packages=find_packages(),  # 自动查找子包
    description='A custom PWN utility module',
    author='p0ach1l',
    install_requires=[
        'pwntools>=4.8.0',
    ],
)
