from setuptools import setup, find_packages

setup(
    name='pytemplate',
    version='0.1.0',
    author='elin',
    description='用于将模板生成器模块化',
    package_dir={'': 'src'},
    packages=find_packages('src'),
)
