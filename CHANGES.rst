Products.CMFUid Changelog
=========================

5.0 (unreleased)
----------------

- Add support for Python 3.13.

- Drop support for Python 3.8.

- Drop support for Python 3.7.

- Add support for Python 3.12.


4.2 (2024-01-23)
----------------

- Fix ``DeprecationWarning``: import ``IObjectAddedEvent`` from ``zope.lifecycleevent``.


4.1 (2023-10-02)
----------------

- Modified the code of ``handleUidAnnotationEvent`` to check if both the
  annotation tool and the UID tool exist before using them. This change
  ensures that the code won't run unless both tools are available.


4.0 (2023-02-01)
----------------

- Drop support for Python 2.7, 3.5, 3.6.


3.5 (2022-12-16)
----------------

- Fix insidious buildout configuration bug for tests against Zope 4.

- Add support for Python 3.11.


3.4 (2022-07-21)
----------------

- When an object is reindexed after its UID is set,
  only reindex the ``cmf_uid`` index rather than all indexes.


3.3 (2022-07-13)
----------------

- Add support for Python 3.10.


3.2.0 (2021-03-15)
------------------

- Add support for Python 3.9.

- Change package structure to move package code into a ``src`` subfolder.


3.1.0 (2020-09-28)
------------------

- Fixed deprecation warning for zope.component.interfaces.IObjectEvent.

- Drop support for ``python setup.py test`` which is broken in Python 3.7+.


3.0.2 (2020-06-24)
------------------

- Clean up and sanitize package and tests configurations

- Remove DeprecationWarning: "InitializeClass is deprecated.
  Please import from AccessControl.class_init."
  Works now with Zope 5


3.0.1 (2018-11-07)
------------------

- fix test isolation problems
  [petschki]


3.0 (2018-07-05)
----------------

- Require `Zope >= 4`.

- Add support for Python 3.5 and 3.6.

- Adapt tests to the new indexing operations queueing.
  Part of PLIP 1343: https://github.com/plone/Products.CMFPlone/issues/1343
  [gforcada]


2.3.0-beta (2012-03-21)
-----------------------

- Made sure converted tools are used as utilities.

- Require at least Zope 2.13.12.


2.2.1 (2010-07-04)
------------------

- Deal with deprecation warnings for Zope 2.13.

- Fix markup error (Chameleon compatibility)


2.2.0 (2010-01-04)
------------------

- no changes from version 2.2.0-beta


2.2.0-beta (2009-12-06)
-----------------------

- no changes from version 2.2.0-alpha


2.2.0-alpha (2009-11-13)
------------------------

- moved the Zope dependency to version 2.12.0b3dev

- Cleaned up / normalized imports:

  o Don't import from Globals;  instead, use real locations.

  o Make other imports use the actual source module, rather than an
    intermediate (e.g., prefer importing 'ClassSecurityInfo' from
    'AccessControl.SecurityInfo' rather than from 'AccessControl').

- Add missing utility registration for IUniqueIdHandler.  See
  https://bugs.launchpad.net/bugs/299058 .

- UniqueIdHandlerTool: Call the reindexObject attribute of the object
  getting a uid, rather than portal_catalog's reindexObject.  This is
  needed to properly handle objects like the portal itself which shouldn't
  get catalogued ever.

- Removed redundant and unexpected code to auto-create catalog index and
  column for the UID handler tool. The index and column are already
  created by the default CMFUid GenericSetup profile.
  (http://www.zope.org/Collectors/CMF/472)


2.1.2 (2008-09-13)
------------------

- no changes from 2.1.2-beta


2.1.2-beta (2008-08-26)
-----------------------

- completed devolution from monolithic CMF package into its component
  products that are distributed as eggs from PyPI.

- testing: Base UidEventZCMLLayer on ZopeTestCase.layer.ZopeLite.

- UniqueIdHandlerTool: Use %r instead of %s in error messages, so
  we don't trip over non-ASCII representations (e.g. File and Image).


2.1.1 (2008-01-06)
------------------

- no changes


2.1.1-beta(2007-12/29)
----------------------

- Testing: Derive test layers from ZopeLite layer if available.


2.1.0 (2007-08-08)
------------------

- Fixed all componentregistry.xml files to use plain object paths and strip
  and slashes. GenericSetup does only support registering objects which are
  in the site root.


2.1.0-beta2 (2007-07-12)
------------------------

- moved the Zope dependency to version 2.10.4

- Remove antique usage of marker attributes in favor of interfaces,
  leaving BBB behind for places potentially affecting third-party code.
  (http://www.zope.org/Collectors/CMF/440)

- Add POST-only protections to security critical methods.
  http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-0240)

- UniqueIdAnnotationTool: Annotation handling has been switched
  from triggering it through old-style manage_*-methods to using
  events. UID assigning behavior has been made more flexible. Please
  review CMFUid/README.txt for information about the current
  behavior and the new features.
  (http://www.zope.org/Collectors/CMF/474)


2.1.0-beta (2007-03-09)
-----------------------

- moved the Zope dependency to verson 2.10.2

- Tool lookup and registration is now done "the Zope 3 way" as utilities, see
  http://svn.zope.org/CMF/branches/2.1/docs/ToolsAreUtilities.stx?view=auto

- UniqueIdHandlerTool: Touching the internal UID value on a
  content item will not cause reindexing all indices anymore, only the
  specific UID index will be touched.
  (http://www.zope.org/Collectors/CMF/469)


2.1.0-alpha2 (2006-11-23)
-------------------------

- moved the Zope dependency to version 2.10.1

- Fixed test breakage induced by use of Z3 pagetemplates in Zope 2.10+.

- browser views: Added some zope.formlib based forms.

- testing: Added test layers for setting up ZCML.


2.1.0-alpha (2006-10-09)
------------------------

- skins: Changed encoding of translated portal_status_messages.
  Now getBrowserCharset is used to play nice with Five forms. Customized
  setRedirect and getMainGlobals scripts have to be updated.

- Profiles: All profiles are now registered by ZCML.

- ZClasses: Removed unmaintained support for ZClasses.
  Marked the 'initializeBases*' methods as deprecated.

- Content: Added IFactory utilities for all content classes.
  They are now used by default instead of the old constructor methods.

- Content: All content classes are now registered by ZCML.
  ContentInit is still used to register oldstyle constructors.

- setup handlers: Removed support for CMF 1.5 CMFSetup profiles.


Earlier releases
----------------

For a complete list of changes before version 2.1.0-alpha, see the HISTORY.txt
file on the CMF-2.1 branch:
http://svn.zope.org/CMF/branches/2.1/HISTORY.txt?view=auto
