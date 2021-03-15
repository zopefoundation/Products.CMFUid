from setuptools import find_packages
from setuptools import setup


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
    version='3.2.0',
    description='Uid product for the Zope Content Management Framework',
    long_description=README,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Plone',
        'Framework :: Zope :: 4',
        'Framework :: Zope :: 5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    keywords='web application server zope cmf',
    author='Zope Foundation and Contributors',
    author_email='zope-cmf@zope.org',
    url='https://github.com/zopefoundation/Products.CMFUid',
    license='ZPL 2.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    namespace_packages=['Products'],
    zip_safe=False,
    install_requires=[
        'Products.CMFCore >= 2.4.0dev',
        'Products.ZCatalog >= 4.1.1',
        'Zope',
        'setuptools',
    ],
    extras_require={
        'test': [
            'zope.testing >= 3.7.0',
        ],
    },
    entry_points="""
    [zope2.initialize]
    Products.%s = Products.%s:initialize
    """ % (NAME, NAME),
)
