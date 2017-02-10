from setuptools import setup, find_packages
import re
import os


def _read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        file = open(path, encoding='utf-8')
    except TypeError:
        file = open(path)
    return file.read()

_meta = _read('ghoster/__init__.py')
_project = re.search(r'^__project__\s*=\s*"(.*)"', _meta, re.M).group(1)
_version = re.search(r'^__version__\s*=\s*"(.*)"', _meta, re.M).group(1)
_license = re.search(r'^__license__\s*=\s*"(.*)"', _meta, re.M).group(1)

setup(
    name=_project,
    version=_version,
    description=_read('DESCRIPTION'),
    long_description=_read('README.rst'),
    license=_license,
    author='Andy Lin',
    author_email='andy@tripper.com.tw',
    maintainer='Ryan Chao',
    maintainer_email='ryanchao2012@gmail.com',
    url='https://github.com/ZuirensGit/django-ghoster',
    keywords='django markdown cms',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

