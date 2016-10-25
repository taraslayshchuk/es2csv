.. :changelog:

Release Changelog
=================

2.4.0 (2016-10-26)
------------------
- Added JSON validation for raw query. (Issue `#7 <https://github.com/taraslayshchuk/es2csv/issues/7>`_)
- Added checks to exclude hangs during connection issues. (Issue `#9 <https://github.com/taraslayshchuk/es2csv/issues/9>`_)
- Updating version elasticsearch-py to 2.4.0 and freeze this dependence according to mask 2.4.*. (Issue `#14 <https://github.com/taraslayshchuk/es2csv/issues/14>`_)
- Updating version progressbar2 to fix issue with visibility.

1.0.3 (2016-06-12)
------------------
- Added option to read query string from file --query(-q) @'~/filename.json'. (Issue `#5 <https://github.com/taraslayshchuk/es2csv/issues/5>`_)
- Added --meta_fields(-e) argument for selecting meta-fields: _id, _index, _score, _type. (Issue `#6 <https://github.com/taraslayshchuk/es2csv/issues/6>`_)
- Updating version elasticsearch-py to 2.3.0.

1.0.2 (2016-04-12)
------------------
- Added --raw_query(-r) argument for using the native Query DSL format.

1.0.1 (2016-01-22)
------------------
- Fixed support elasticsearch-1.4.0.
- Added --version argument.
- Added history changelog.

1.0.0.dev1 (2016-01-04)
-----------------------
- Fixed encoding in CSV to UTF-8. (Issue `#3 <https://github.com/taraslayshchuk/es2csv/issues/3>`_, Pull `#1 <https://github.com/taraslayshchuk/es2csv/pull/1>`_)
- Added better progressbar unit names. (Pull `#2 <https://github.com/taraslayshchuk/es2csv/pull/2>`_)
- Added pip installation instruction.

1.0.0.dev0 (2015-12-25)
-----------------------
- Initial registration.
- Added first dev-release on github.
- Added first release on PyPI.