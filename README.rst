Pingdom Export: Export your pingdom data
========================================

|Build| |Coverage|

.. |Build| image:: https://travis-ci.org/entering/pingdomexport.svg?branch=master
    :target: https://travis-ci.org/entering/pingdomexport.svg?branch=master

.. |Coverage| image:: https://coveralls.io/repos/github/entering/pingdomexport/badge.svg?branch=master
    :target: https://coveralls.io/github/entering/pingdomexport?branch=master

Installation
------------

To install simply

.. code-block:: bash

    $ pip install pingdomexport

Configure
------------

Check the `configuration file <https://github.com/entering/pingdomexport/blob/master/config.yml.dist>`_.

Place the configuration file in any place that seems fit and make sure the user you will use to run pingdom export
has access to it.

Configuration access
--------------------

.. code-block:: yaml

    pingdom_access:
        username: dummy
        password: dummy
        account_email: dummy
        app_key: dummy

The username, password and account email should be easy to fill is your credentials to log in in pindgom.

The api key you need to create an application. Log in in pingdom then Integrations > The Pingdom API > Register Application

Configuration checks
--------------------

.. code-block:: yaml

    # the checks that you want to export data
    checks:
        # 3 strategies supported
        # all: all checks
        # include: will only include the ids specified
        # exclude: all checks except the ids specified
        strategy: all
        ids: []

Pindgom export allows to export all checks:

.. code-block:: yaml

  checks:
      strategy: all
      ids: []

Specify the checks to export:

.. code-block:: yaml

    checks:
        strategy: include
        ids: [12454, 32932]

Specify the checks to exclude (will export every check except the ones specified):

.. code-block:: yaml

    checks:
        strategy: exclude
        ids: [12454]

Configuration export
--------------------

Pingdom export allows to export the checks and results to mysql, postgres or the stdout.

.. code-block:: yaml

  load:
      # type: output|mysql|postgres
      type: output
      parameters: []
      # if mysql
      #parameters:
      #  db_url: mysql+pymysql://user:password@host/database
      # if postgres
      #parameters:
      #  db_url: postgres://user:password@host/database

If output:

.. code-block:: yaml

  load:
      type: output
      parameters: []

If mysql:

.. code-block:: yaml

  load:
      type: mysql
      parameters:
          db_url: mysql+pymysql://user:password@host/database

If posgres:

.. code-block:: yaml

  load:
      type: postgres
      parameters:
          db_url: mysql+pymysql://user:password@host/database

Database schema
---------------

-  `MySQL <https://github.com/entering/pingdomexport/blob/master/provisioning/roles/mysql/files/schema.sql>`_
-  `Postgres <https://github.com/entering/pingdomexport/blob/master/provisioning/roles/postgresql/files/schema.sql>`_


Run
------------

Run pingdom-run-export --help for help

Export only check information:

.. code-block:: bash

    $ pingdom-run-export --config /full/path/to/config.yml --type checks

Export only checks results:

.. code-block:: bash

    $ pingdom-run-export --config /full/path/to/config.yml --type results

Export checks information & results:

.. code-block:: bash

    $ pingdom-run-export --config /full/path/to/config.yml --type all

Run - partial export
--------------------

By default the pingdom export will always export the full results. But will also allow to specify a range, eg:

.. code-block:: bash

    $ pingdom-run-export --config /full/path/to/config.yml --type results --checks-from 1465071758 --checks-to 1465158158

Big data
--------------------

In case you have multiple checks with months of history, running everything in a single thread will take too much time.

You can use multiple configuration files and run one pingdom export per check. Then just have a crontab running daily and
use the checks-from and checks-to.
