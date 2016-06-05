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

Check the configuration file |Configuration|

.. |Configuration|: https://github.com/entering/pingdomexport/blob/master/config.yml.dist

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

Run
------------

Run pingdom-run-export --help for help
