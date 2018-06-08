# osmlab

Open Source Macroeconomics Lab Webpage built in [Flask](http://flask.pocoo.org).

## Getting started

As a prerequisite, you will need conda installed to help manage your environment.

The first time you run this project, you will need to create the `osmlab` environment:

* `conda env create -f environment.yml`

After that, each time you start developing:

* `source activate osmlab`
* `conda env update` (this is optional, but necessary if any packages have changed since the last time you ran it)

To run the project:

* `bin/start`

The app will run locally at `localhost:5000`.

## Running tests

To run the test suite, run `python osmlab/tests/views_test.py` from the repo root.
