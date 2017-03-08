# land-availability-ui
Land Availability Tool - Frontend

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
```

example:

```
DATABASE_URL=postgres://andreagrandi@localhost:5432/landavailability-ui
SECRET_KEY='abcd1234'
```

If you are using a Python virtual environment, you can save these values in
$venv_folder/bin/postactivate script:

```
export DATABASE_URL=postgres://andreagrandi@localhost:5432/landavailability-ui
export SECRET_KEY='abcd1234'
```

# Python

The project is being developed and tested with **Python >= 3.5.x**
