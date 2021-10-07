from setuptools import setup

setup(
    name="csv-diff-python3-blue-monk",
    install_requires=[
    ],
    extras_require={
    },
    entry_points={
        'console_scripts': [
            'csvdiff3=csvdiff3.csvdiff:main',
        ],
    },
)
