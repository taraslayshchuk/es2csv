es2csv
======

A CLI tool for exporting data from Elasticsearch into a CSV file
----------------------------------------------------------------

Command line utility, written in Python, for querying Elasticsearch in Lucene query syntax or Query DSL syntax and exporting result as documents into a CSV file. This tool can query bulk docs in multiple indices and get only selected fields, this reduces query execution time.

Quick Look Demo
---------------
.. figure:: https://cloud.githubusercontent.com/assets/7491121/12016825/59eb5f82-ad58-11e5-81eb-871a49e39c37.gif

Installation
------------

From source:

.. code-block:: bash

    $ pip install git+https://github.com/taraslayshchuk/es2csv.git

From pip:

.. code-block:: bash

    $ pip install es2csv

Usage
-----
.. code-block:: bash

 $ es2csv [-h] -q QUERY [-u URL] [-a AUTH] [-i INDEX [INDEX ...]]
          [-D DOC_TYPE [DOC_TYPE ...]] [-t TAGS [TAGS ...]] -o FILE
          [-f FIELDS [FIELDS ...]] [-d DELIMITER] [-m INTEGER] [-k]
          [-r] [-e] [-v] [--debug]

 Arguments:
  -q, --query QUERY                        Query string in Lucene syntax.               [required]
  -o, --output_file FILE                   CSV file location.                           [required]
  -u, --url URL                            Elasticsearch host URL. Default is http://localhost:9200.
  -a, --auth                               Elasticsearch basic authentication in the form of username:password.
  -i, --index-prefixes INDEX [INDEX ...]   Index name prefix(es). Default is ['logstash-*'].
  -D, --doc_types DOC_TYPE [DOC_TYPE ...]  Document type(s).
  -t, --tags TAGS [TAGS ...]               Query tags.
  -f, --fields FIELDS [FIELDS ...]         List of selected fields in output. Default is ['_all'].
  -d, --delimiter DELIMITER                Delimiter to use in CSV file. Default is ",".
  -m, --max INTEGER                        Maximum number of results to return. Default is 0.
  -k, --kibana_nested                      Format nested fields in Kibana style.
  -r, --raw_query                          Switch query format in the Query DSL.
  -e, --meta_fields                        Add meta-fields in output.
  -v, --version                            Show version and exit.
  --debug                                  Debug mode on.
  -h, --help                               show this help message and exit

Examples
--------
Searching on localhost and save to database.csv

.. code-block:: bash

  $ es2csv -q 'host: localhost' -o database.csv

Same in Query DSL syntax

.. code-block:: bash

  $ es2csv -r -q '{"query": {"match": {"host": "localhost"}}}' -o database.csv

Very long queries can be read from file

.. code-block:: bash

  $ es2csv -r -q @'~/query string file.json' -o database.csv
  
With tag

.. code-block:: bash

  $ es2csv -t dev -q 'host: localhost' -o database.csv
  
More tags

.. code-block:: bash

  $ es2csv -t dev prod -q 'host: localhost' -o database.csv
  
On custom Elasticsearch host

.. code-block:: bash

  $ es2csv -u my.cool.host.com:9200 -q 'host: localhost' -o database.csv
  
You are using secure Elasticsearch with nginx? No problem!

.. code-block:: bash

  $ es2csv -u http://my.cool.host.com/es/ -q 'host: localhost' -o database.csv
  
Not default port?

.. code-block:: bash

  $ es2csv -u my.cool.host.com:6666/es/ -q 'host: localhost' -o database.csv
  
With Authorization

.. code-block:: bash

  $ es2csv -u http://login:password@my.cool.host.com:6666/es/ -q 'host: localhost' -o database.csv

With explicit Authorization

.. code-block:: bash

  $ es2csv -a login:password -u http://my.cool.host.com:6666/es/ -q 'host: localhost' -o database.csv 
  
Specifying index

.. code-block:: bash

  $ es2csv -i logstash-2015-07-07 -q 'host: localhost' -o database.csv
  
More indexes

.. code-block:: bash

  $ es2csv -i logstash-2015-07-07 logstash-2015-08-08 -q 'host: localhost' -o database.csv
  
Or index mask

.. code-block:: bash

  $ es2csv -i logstash-2015-* -q 'host: localhost' -o database.csv
  
And now together

.. code-block:: bash

  $ es2csv -i logstash-2015-01-0* logstash-2015-01-10 -q 'host: localhost' -o database.csv
  
Collecting all data on all indices

.. code-block:: bash

  $ es2csv -i _all -q '*' -o database.csv
  
Specifying document type

.. code-block:: bash

  $ es2csv -D log -i _all -q '*' -o database.csv
  
Selecting some fields, what you are interesting in, if you don't need all of them (query run faster)

.. code-block:: bash

  $ es2csv -f host status date -q 'host: localhost' -o database.csv

  
Selecting all fields, by default

.. code-block:: bash

  $ es2csv -f _all -q 'host: localhost' -o database.csv

Selecting meta-fields: _id, _index, _score, _type

.. code-block:: bash

  $ es2csv -e -f _all -q 'host: localhost' -o database.csv

Selecting nested fields

.. code-block:: bash

  $ es2csv -f comments.comment comments.date comments.name -q '*' -i twitter -o database.csv

Max results count

.. code-block:: bash

  $ es2csv -m 6283185 -q '*' -i twitter -o database.csv

Changing column delimiter in CSV file, by default ','

.. code-block:: bash

  $ es2csv -d ';' -q '*' -i twitter -o database.csv
  
Changing nested columns output format to Kibana style like

.. code-block:: bash

  $ es2csv -k -q '*' -i twitter -o database.csv

An JSON document example

.. code-block:: json

  {
    "title": "Nest eggs",
    "body":  "Making your money work...",
    "tags":  [ "cash", "shares" ],
    "comments": [ 
      {
        "name":    "John Smith",
        "comment": "Great article",
        "age":     28,
        "stars":   4,
        "date":    "2014-09-01"
      },
      {
        "name":    "Alice White",
        "comment": "More like this please",
        "age":     31,
        "stars":   5,
        "date":    "2014-10-22"
      }
    ]
  }

A CSV file in Kibana style format

.. code-block::

  body,comments.age,comments.comment,comments.date,comments.name,comments.stars,tags,title
  Making your money work...,"28,31","Great article,More like this please","2014-09-01,2014-10-22","John Smith,Alice White","4,5","cash,shares",Nest eggs

A CSV file in default format

.. code-block::

  body,comments.0.age,comments.0.comment,comments.0.date,comments.0.name,comments.0.stars,comments.1.age,comments.1.comment,comments.1.date,comments.1.name,comments.1.stars,tags.0,tags.1,title
  Making your money work...,28,Great article,2014-09-01,John Smith,4,31,More like this please,2014-10-22,Alice White,5,cash,shares,Nest eggs