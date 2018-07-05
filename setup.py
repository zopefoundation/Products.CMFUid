from setuptools import setup
from setuptools import find_packages

NAME = 'CMFUid'


def _read(name):
    with open(name) as f:
        return f.read()


_boundary = '\n' + ('-' * 60) + '\n\n'
README = _boundary.join([
    _read('README.rst'),
    _read('CHANGES.rst'),
])


setup(
    name='Products.%s' % NAME,
    version='3.0',
    description='Uid product for the Zope Content Management Framework',
    long_description=README,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Zope :: 4",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    keywords='web application server zope cmf',
    author="Zope Foundation and Contributors",
    author_email="zope-cmf@zope.org",
    url="https://github.com/zopefoundation/Products.CMFUid",
    license="ZPL 2.1",
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=['Products'],
    zip_safe=False,
    setup_requires=[
        'eggtestinfo',
    ],
    install_requires=[
        'Products.CMFCore >= 2.4.0dev',
        'Products.ZCatalog >= 4.1.1',
        'Zope',
        'setuptools',
    ],
    tests_require=[
        'zope.testing >= 3.7.0',
    ],
    test_loader='zope.testing.testrunner.eggsupport:SkipLayers',
    test_suite='Products.%s.tests' % NAME,
    entry_points="""
    [zope2.initialize]
    Products.%s = Products.%s:initialize
    [distutils.commands]
    ftest = zope.testing.testrunner.eggsupport:ftest
    """ % (NAME, NAME),
)
