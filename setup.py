from setuptools import setup, find_packages

setup(
    name='pwnpy',
    version='1.0.0',
    packages=find_packages(),  # 自动查找子包
    description='A custom PWN utility module',
    author='p0ach1l',
    install_requires=[
        'pwntools>=4.8.0',
    ],
)
