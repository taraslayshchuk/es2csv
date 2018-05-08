=========
Arguments
=========

============================================================  ==================================================================== 
                         Argument                                                        Description 
============================================================  ==================================================================== 
`-q, --query <#query>`_ QUERY                                 Query string in Lucene syntax.               [required]
`-o, --output-file <#output-file>`_ FILE                      CSV file location.                           [required]
`-u, --url <#url>`_ URL                                       Elasticsearch host URL. Default is "http://localhost:9200".
`-a, --auth <#auth>`_                                         Elasticsearch basic authentication in the form of username:password.
`-i, --index-prefixes <#index-prefixes>`_ INDEX [INDEX ...]   Index name prefix(es). Default is ['logstash-\*'].
`-D, --doc-types <#doc-types>`_ DOC_TYPE [DOC_TYPE ...]       Document type(s).
`-t, --tags <#tags>`_ TAGS [TAGS ...]                         Query tags.
`-f, --fields <#fields>`_ FIELDS [FIELDS ...]                 List of selected fields in output. Default is ['_all'].
`-s, --sort <#sort>`_ FIELDS [FIELDS ...]                     List of <field>:<direction> pairs to sort on. Default is [].
`-d, --delimiter <#delimiter>`_ DELIMITER                     Delimiter to use in CSV file. Default is ",".
`-m, --max <#max>`_ INTEGER                                   Maximum number of results to return. Default is 0.
-s, --scroll-size INTEGER                                     Scroll size for each batch of results. Default is 100.
`-k, --kibana-nested <#kibana-nested>`_                       Format nested fields in Kibana style.
`-r, --raw-query <#raw-query>`_                               Switch query format in the Query DSL.
`-e, --meta-fields <#meta-fields>`_                           Add meta-fields in output.
`--verify-certs <#verify-certs>`_                             Verify SSL certificates. Default is False.
`--ca-certs CA_CERTS <#ca-certs>`_                            Location of CA bundle.
--client-cert CLIENT_CERT                                     Location of Client Auth cert.
--client-key CLIENT_KEY                                       Location of Client Cert Key.
-v, --version                                                 Show version and exit.
--debug                                                       Debug mode on.
-h, --help                                                    show this help message and exit
============================================================  ==================================================================== 

========
Examples
========

query
-----
Searching on http://localhost:9200, by default

.. code-block:: bash

  $ es2csv -q 'user: John' -o database.csv

output-file
-----------
Save to my_database.csv file

.. code-block:: bash

  $ es2csv -q 'user: John' -o my_database.csv

url
---
On custom Elasticsearch host

.. code-block:: bash

  $ es2csv -u my.cool.host.com:9200 -q 'user: John' -o database.csv

You are using secure Elasticsearch with nginx? No problem!

.. code-block:: bash

  $ es2csv -u http://my.cool.host.com/es/ -q 'user: John' -o database.csv

Not default port?

.. code-block:: bash

  $ es2csv -u my.cool.host.com:6666/es/ -q 'user: John' -o database.csv

auth
----
With Authorization

.. code-block:: bash

  $ es2csv -u http://login:password@my.cool.host.com:6666/es/ -q 'user: John' -o database.csv

With explicit Authorization

.. code-block:: bash

  $ es2csv -a login:password -u http://my.cool.host.com:6666/es/ -q 'user: John' -o database.csv

index-prefixes
--------------
Specifying index

.. code-block:: bash

  $ es2csv -i logstash-2015-07-07 -q 'user: John' -o database.csv

More indexes

.. code-block:: bash

  $ es2csv -i logstash-2015-07-07 logstash-2015-08-08 -q 'user: John' -o database.csv

Or index mask

.. code-block:: bash

  $ es2csv -i logstash-2015-* -q 'user: John' -o database.csv

And now together

.. code-block:: bash

  $ es2csv -i logstash-2015-01-0* logstash-2015-01-10 -q 'user: John' -o database.csv

Collecting all data on all indices

.. code-block:: bash

  $ es2csv -i _all -q '*' -o database.csv

doc-types
---------
Specifying document type

.. code-block:: bash

  $ es2csv -D log -i _all -q '*' -o database.csv

tags
----
With tag

.. code-block:: bash

  $ es2csv -t dev -q 'user: John' -o database.csv

More tags

.. code-block:: bash

  $ es2csv -t dev prod -q 'user: John' -o database.csv

fields
------
Selecting some fields, what you are interesting in, if you don't need all of them (query run faster)

.. code-block:: bash

  $ es2csv -f host status date -q 'user: John' -o database.csv

Or field mask

.. code-block:: bash

  $ es2csv -f 'ho*' 'st*us' '*ate' -q 'user: John' -o database.csv

Selecting all fields, by default

.. code-block:: bash

  $ es2csv -f _all -q 'user: John' -o database.csv

Selecting nested fields

.. code-block:: bash

  $ es2csv -f comments.comment comments.date comments.name -q '*' -i twitter -o database.csv

sort
----
Sorting by fields, in order what you are interesting in, could contains only field name (will be sorted in ascending order)

.. code-block:: bash

  $ es2csv -S key -q '*' -o database.csv

Or field pair: field name and direction (desc or asc)

.. code-block:: bash

  $ es2csv -S status:desc -q '*' -o database.csv

Using multiple pairs

.. code-block:: bash

  $ es2csv -S key:desc status:asc -q '*' -o database.csv

Selecting some field(s), but sorting by other(s)

.. code-block:: bash

  $ es2csv -S key -f user -q '*' -o database.csv

delimiter
---------
Changing column delimiter in CSV file, by default ','

.. code-block:: bash

  $ es2csv -d ';' -q '*' -i twitter -o database.csv

max
---
Max results count

.. code-block:: bash

  $ es2csv -m 6283185 -q '*' -i twitter -o database.csv

Retrieve 2000 results in just 2 requests (two scrolls 1000 each):

.. code-block:: bash

  $ es2csv -m 2000 -s 1000 -q '*' -i twitter -o database.csv

kibana-nested
-------------
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

.. code-block:: csv

  body,comments.age,comments.comment,comments.date,comments.name,comments.stars,tags,title
  Making your money work...,"28,31","Great article,More like this please","2014-09-01,2014-10-22","John Smith,Alice White","4,5","cash,shares",Nest eggs

A CSV file in default format

.. code-block:: csv

  body,comments.0.age,comments.0.comment,comments.0.date,comments.0.name,comments.0.stars,comments.1.age,comments.1.comment,comments.1.date,comments.1.name,comments.1.stars,tags.0,tags.1,title
  Making your money work...,28,Great article,2014-09-01,John Smith,4,31,More like this please,2014-10-22,Alice White,5,cash,shares,Nest eggs

raw-query
---------
Query DSL syntax

.. code-block:: bash

  $ es2csv -r -q '{"query": {"match": {"user": "John"}}}' -o database.csv

Very long queries can be read from file

.. code-block:: bash

  $ es2csv -r -q @'~/query string file.json' -o database.csv

meta-fields
-----------
Selecting meta-fields: _id, _index, _score, _type, _explanation. If the selected meta-field is not available than we use `NaN` as a default.

.. code-block:: bash

  $ es2csv -e -f _all -q 'user: John' -o database.csv

verify-certs
------------
With enabled SSL certificate verification (off by default)

.. code-block:: bash

  $ es2csv --verify-certs -u https://my.cool.host.com/es/ -q 'user: John' -o database.csv

ca-certs
--------
With your own certificate authority bundle

.. code-block:: bash

  $ es2csv --ca-certs '/path/to/your/ca_bundle' --verify-certs -u https://host.com -q '*' -o out.csv
