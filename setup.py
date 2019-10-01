from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='rodin_helpers',
    version='0.1.2',
    author='Dmitry Rodin',
    author_email='madiedinro@gmail.com',
    license='MIT',
    description='Collection of python helpers to prettier print',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    url='https://github.com/madiedinro/rodin_helpers_py',
    include_package_data=True,
    install_requires=[
        'ujson>=1.35,<2'
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    project_urls={
        'Homepage': 'https://github.com/madiedinro/rodin_helpers_py'
    }
)
