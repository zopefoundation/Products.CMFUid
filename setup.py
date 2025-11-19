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
    version='5.0',
    description='Uid product for the Zope Content Management Framework',
    long_description=README,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Plone',
        'Framework :: Zope :: 5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    keywords='web application server zope cmf',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.dev',
    url='https://github.com/zopefoundation/Products.CMFUid',
    license='ZPL-2.1',
    python_requires='>=3.10',
    install_requires=[
        'Products.CMFCore >= 2.4.0dev',
        'Products.ZCatalog >= 4.1.1',
        'Zope',
    ],
    extras_require={
        'test': [
            'zope.testing >= 3.7.0',
        ],
    },
    include_package_data=True,
    entry_points="""
    [zope2.initialize]
    Products.{} = Products.{}:initialize
    """.format(NAME, NAME),
)
