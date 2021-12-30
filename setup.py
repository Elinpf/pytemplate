from setuptools import setup, find_packages

setup(
    name='pytemplate_elinpf',
    version='0.1.0',
    author='elin',
    author_email="elin365433079@gmail.com",
    url="https://github.com/Elinpf/pytemplate",
    description='用于将模板生成器模块化',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    python_requires=">=3.6",
    install_requires=["openpyxl"]
)
