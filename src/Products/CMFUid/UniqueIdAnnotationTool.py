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
"""Unique Id Annotation Tool

Provides support for managing unique id annotations.
"""

from AccessControl.class_init import InitializeClass
from AccessControl.SecurityInfo import ClassSecurityInfo
from Acquisition import Implicit
from OFS.interfaces import IObjectClonedEvent
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import SimpleItem
from Persistence import Persistent
from zope.component import queryUtility
from zope.interface import implementer
from zope.lifecycleevent.interfaces import IObjectAddedEvent

from Products.CMFCore.utils import UniqueObject
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.utils import registerToolInterface

from .interfaces import IUniqueIdAnnotation
from .interfaces import IUniqueIdAnnotationManagement
from .interfaces import UniqueIdError


@implementer(IUniqueIdAnnotation)
class UniqueIdAnnotation(Persistent, Implicit):

    """Unique id object used as annotation on (content) objects.
    """

    def __init__(self, obj, id):
        """See IUniqueIdAnnotation.
        """
        self._uid = None
        self.id = id
        setattr(obj, id, self)

    def __call__(self):
        """See IUniqueIdAnnotation.
        """
        return self._uid

    def getId(self):
        """See IUniqueIdAnnotation.
        """
        return self.id

    def setUid(self, uid):
        """See IUniqueIdAnnotation.
        """
        self._uid = uid


InitializeClass(UniqueIdAnnotation)


def handleUidAnnotationEvent(ob, event):
    """ Event subscriber for (IContentish, IObjectEvent) events
    """

    if IObjectAddedEvent.providedBy(event):
        if event.newParent is not None:
            anno_tool = queryUtility(IUniqueIdAnnotationManagement)
            uidtool = getToolByName(ob, 'portal_uidhandler', None)
            if anno_tool is not None and uidtool is not None:
                remove_on_add = anno_tool.getProperty('remove_on_add', False)
                remove_on_clone = anno_tool.getProperty('remove_on_clone',
                                                        False)
                assign_on_add = anno_tool.getProperty('assign_on_add', False)

                if (remove_on_add and remove_on_clone) or assign_on_add:
                    try:
                        uidtool.unregister(ob)
                    except UniqueIdError:
                        # did not have one
                        pass
                if assign_on_add:
                    # assign new uid
                    uidtool.register(ob)

    elif IObjectClonedEvent.providedBy(event):
        anno_tool = queryUtility(IUniqueIdAnnotationManagement)
        uidtool = getToolByName(ob, 'portal_uidhandler', None)

        if anno_tool is not None and uidtool is not None:
            remove_on_clone = anno_tool.getProperty('remove_on_clone', False)
            assign_on_clone = anno_tool.getProperty('assign_on_clone', False)
            if remove_on_clone or assign_on_clone:
                try:
                    uidtool.unregister(ob)
                except UniqueIdError:
                    # did not have one
                    pass
            if assign_on_clone:
                # assign new uid
                uidtool.register(ob)


@implementer(IUniqueIdAnnotationManagement)
class UniqueIdAnnotationTool(UniqueObject, SimpleItem, PropertyManager):

    __doc__ = __doc__  # copy from module

    manage_options = (
        PropertyManager.manage_options +
        SimpleItem.manage_options
    )

    id = 'portal_uidannotation'
    alternative_id = 'portal_standard_uidannotation'
    meta_type = 'Unique Id Annotation Tool'

    security = ClassSecurityInfo()

    remove_on_add = True
    remove_on_clone = True
    assign_on_add = False
    assign_on_clone = False
    _properties = (
        {'id': 'remove_on_add', 'type': 'boolean', 'mode': 'w',
         'label': 'Remove the objects unique id on add (and import)'},
        {'id': 'remove_on_clone', 'type': 'boolean', 'mode': 'w',
         'label': 'Remove the objects unique id on clone (CAUTION !!!)'},
        {'id': 'assign_on_add', 'type': 'boolean', 'mode': 'w',
         'label': 'Assign a unique ID when an object is added'},
        {'id': 'assign_on_clone', 'type': 'boolean', 'mode': 'w',
         'label': 'Assign a unique ID when an object is cloned'},
    )

    security.declarePrivate('__call__')

    def __call__(self, obj, id):
        """See IUniqueIdAnnotationManagement.
        """
        return UniqueIdAnnotation(obj, id)


InitializeClass(UniqueIdAnnotationTool)


registerToolInterface('portal_uidannotation', IUniqueIdAnnotationManagement)
