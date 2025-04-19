
from setuptools import setup, find_packages

setup(
    name='savepoint-cli',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sp = cli:main',
        ],
    },
    install_requires=[],
    include_package_data=True,
    description='Savepoint Protocol CLI — semantic version control for thought',
    author='Peter Salvato',
)
