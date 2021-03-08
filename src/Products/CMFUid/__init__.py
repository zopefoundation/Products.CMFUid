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
"""Unique id generation and handling.
"""


def initialize(context):

    from Products.CMFCore import utils

    from . import UniqueIdAnnotationTool
    from . import UniqueIdGeneratorTool
    from . import UniqueIdHandlerTool

    tools = (
        UniqueIdAnnotationTool.UniqueIdAnnotationTool,
        UniqueIdGeneratorTool.UniqueIdGeneratorTool,
        UniqueIdHandlerTool.UniqueIdHandlerTool,
    )

    utils.ToolInit(
        'CMF Unique Id Tool',
        tools=tools,
        icon='tool.gif',
    ).initialize(context)
