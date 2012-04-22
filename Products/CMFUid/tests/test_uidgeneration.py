##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Test the unique id generation.
"""

import unittest
import Testing

from BTrees.Length import Length
from zope.interface.verify import verifyClass

from Products.CMFCore.tests.base.testcase import SecurityTest


class UniqueIdGeneratorToolTests(SecurityTest):

    def _getTargetClass(self):
        from Products.CMFUid.UniqueIdGeneratorTool \
                import UniqueIdGeneratorTool

        return UniqueIdGeneratorTool

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_interfaces(self):
        from Products.CMFUid.interfaces import IUniqueIdGenerator

        verifyClass(IUniqueIdGenerator, self._getTargetClass())

    def test_returnedUidsAreValidAndDifferent(self):
        generator = self._makeOne()
        uid1 = generator()
        uid2 = generator()
        self.assertNotEqual(uid1, uid2)
        self.assertNotEqual(uid1, None)

    def test_converter(self):
        generator = self._makeOne()
        uid = generator()
        str_uid = str(uid)
        result = generator.convert(str_uid)
        self.assertEqual(result, uid)

    def test_migrationFromBTreeLengthToInteger(self):
        # For backwards compatibility with CMF 1.5.0 and 1.5.1, check if
        # the generator correctly replaces a ``BTree.Length.Length`` object
        # to an integer.
        generator = self._makeOne()
        uid1 = generator()
        generator._uid_counter = Length(uid1)
        self.assertTrue(isinstance(generator._uid_counter, Length))
        uid2 = generator()
        self.assertTrue(isinstance(generator._uid_counter, int))
        self.assertNotEqual(uid1, uid2)


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(UniqueIdGeneratorToolTests),
        ))
