##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Unit test layers.
"""

from Testing.ZopeTestCase.layer import ZopeLite
from Zope2.App import zcml
from zope.component.hooks import setHooks
from zope.testing.cleanup import cleanUp


class UidEventZCMLLayer(ZopeLite):

    @classmethod
    def testSetUp(cls):
        import OFS
        import Products

        zcml.load_config('meta.zcml', Products.Five)
        zcml.load_config('event.zcml', OFS)
        zcml.load_config('event.zcml', Products.CMFUid)
        setHooks()

    @classmethod
    def testTearDown(cls):
        cleanUp()
