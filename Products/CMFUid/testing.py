from zope.app.component.hooks import setHooks
from zope.testing.cleanup import cleanUp
from Products.Five import zcml

class UidEventZCMLLayer:

    @classmethod
    def testSetUp(cls):
        import Products

        zcml.load_config('meta.zcml', Products.Five)
        zcml.load_config('event.zcml', Products.Five)
        zcml.load_config('event.zcml', Products.CMFUid)
        setHooks()

    @classmethod
    def testTearDown(cls):
        cleanUp()


# Derive from ZopeLite layer if available
try:
    from Testing.ZopeTestCase.layer import ZopeLite
except ImportError:
    pass # Zope < 2.11
else:
    UidEventZCMLLayer.__bases__ = (ZopeLite,)

