from setuptools import setup

setup(
    name='oselab',
    packages=['oselab'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-Assets',
        'Flask-Markdown',
    ],
)
