.. :changelog:

Release Changelog
=================

5.2.1 (2017-04-02)
------------------
- Added --verify-certs, --ca-certs, --client-cert, --client-key arguments for SSL configuration. (Issue `#11 <https://github.com/taraslayshchuk/es2csv/issues/11>`_ and `#24 <https://github.com/taraslayshchuk/es2csv/issues/24>`_, Pull `#22 <https://github.com/taraslayshchuk/es2csv/pull/22>`_)
- Added --scroll_size(-s) argument to specify the scroll size of requests. (Pull `#27 <https://github.com/taraslayshchuk/es2csv/pull/27>`_)

5.2.0 (2017-02-16)
------------------
- Updating version elasticsearch-py to 5.2.* and added support of Elasticsearch 5. (Issue `#19 <https://github.com/taraslayshchuk/es2csv/issues/19>`_)

2.4.3 (2017-02-15)
------------------
- Update doc according to wildcard support in fields naming.
- Added support of old version pip. (Issue `#16 <https://github.com/taraslayshchuk/es2csv/issues/16>`_)

2.4.2 (2017-02-14)
------------------
- Added wildcard support in fields naming.
- Removed column sorting. (Issue `#21 <https://github.com/taraslayshchuk/es2csv/issues/21>`_)

2.4.1 (2016-11-10)
------------------
- Added --auth(-a) argument for Elasticsearch basic authentication. (Pull `#17 <https://github.com/taraslayshchuk/es2csv/pull/17>`_)
- Added --doc_types(-D) argument for specifying document type. (Pull `#13 <https://github.com/taraslayshchuk/es2csv/pull/13>`_)

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
