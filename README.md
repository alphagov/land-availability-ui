# land-availability-ui
Land Availability Tool - Frontend

# Continuous integration status

[![Travis-CI Status](https://secure.travis-ci.org/alphagov/land-availability-ui.png?branch=master)](http://travis-ci.org/#!/alphagov/land-availability-ui)
[![Coverage Status](https://coveralls.io/repos/github/alphagov/land-availability-ui/badge.svg?branch=master)](https://coveralls.io/github/alphagov/land-availability-ui?branch=master)

# PostgreSQL Setup

Make sure you have **PostgreSQL** (tested with 9.6) installed.

It's strongly suggested to use Postgres.app on OSX and to install all the other
tools and dependencies using **brew**.

## Create DB

```
createdb landavailability-ui
```

# Project Configuration

Make sure you have these environment variables set:

```
DATABASE_URL=postgres://USERNAME:PASSWORD@HOST:PORT/DBNAME
SECRET_KEY='abcd1234'
LAND_AVAILABILITY_API_URL=http://localhost:8000
LAND_AVAILABILITY_API_TOKEN=abcd1234
```

Example value:

```
DATABASE_URL=postgres://andreagrandi@localhost:5432/landavailability-ui
```

If you are using a Python virtual environment, you can save these values in
$venv_folder/bin/postactivate script:

```
export DATABASE_URL=postgres://andreagrandi@localhost:5432/landavailability-ui
...
```

# Python

The project is being developed and tested with **Python >= 3.5.x**
