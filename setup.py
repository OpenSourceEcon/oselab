import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    longdesc = fh.read()

setuptools.setup(
    name='oselab',
    version='0.1.0',
    author='Richard W. Evans',
    license="CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    description="Websit for the Open Source Economics Laboratory",
    long_description_content_type="text/markdown",
    long_description=longdesc,
    packages=['oselab'],
    include_package_data=True,
    include_packages=True,
    python_requires='>=3.12, <3.13',
    install_requires=[
        'flask>=1.1.2',
        'Flask-Assets',
        'Flask-Markdown',
        'Pygments>=2.2.0',
        'gunicorn'
    ],
)
