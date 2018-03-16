import os
from setuptools import setup
from setuptools import find_packages

NAME = 'CMFUid'

here = os.path.abspath(os.path.dirname(__file__))
package = os.path.join(here, 'Products', NAME)

def _package_doc(name):
    with open(os.path.join(package, name)) as f:
        return f.read()

_boundary = '\n' + ('-' * 60) + '\n\n'
README = ( _package_doc('README.txt')
         + _boundary
         + _package_doc('CHANGES.txt')
         + _boundary
         + "Download\n========"
         )

setup(name='Products.%s' % NAME,
      version=_package_doc('version.txt').strip(),
      description='Uid product for the Zope Content Management Framework',
      long_description=README,
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Zope :: 4",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
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
      setup_requires=['eggtestinfo',
                     ],
      install_requires=[
          'Products.BTreeFolder2 >= 4.0.dev0',
          'Products.CMFCore >= 2.4.0b3',
          'Products.GenericSetup',
          'Products.ZCTextIndex >= 4.0.dev0',
          'Products.ZCatalog >= 4.0.dev0',
          'Products.ZSQLMethods >= 3.0.dev0',
          'Zope',
          'Products.GenericSetup >= 1.10.0.dev0',
          'Products.MailHost >= 4.0.dev0',
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
