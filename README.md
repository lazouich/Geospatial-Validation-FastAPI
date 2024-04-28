# Geospatial Validations Using FastAPI and PostGIS

## Introduction

Geospatial workflows and tooling mostly fall into two (often related) categories: analysis and visualization. The first
is hypothesis testing in support of research; the second info-design for knowledge transfer.
We will look at an often overlooked third category: adding geospatial dimensions to input validation and business logic,
with a specific focus on web applications (FastAPI + PostgreSQL).

This project accompanies my PyCon 2024 talk of the same name.

## Setup

To run this project, you will need to have Docker installed on your machine.
Once you have Docker installed, you can run the following command to start the
application:

```bash
docker-compose up
```

The docker-compose file will start a FastAPI application and a PostgreSQL/PostGIS database as well as run
the alembic migrations to load the necessary data into the database.

There is a [Dockerfile_postgis](Dockerfile_postgis) file that is used to build the PostGIS image. At the time
of writing, the official PostGIS image does not support ARM64 architecture. This Dockerfile is taken directly from
the official [PostGIS image repository](https://github.com/postgis/docker-postgis) and builds successfully on ARM64
architecture.

**Note**: To run this project without Docker, the database urls in the `database.py` and `alembic.ini` files will need
to be
updated.

## Project Structure

The project is structured as follows:

```plaintext
. 
├── Dockerfiles*
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   ├── alembic
│   ├── alembic.ini
│   ├── data_access_layer.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── poetry.lock
├── pyproject.toml
```

- The `main.py` file contains the FastAPI application and endpoints.
- The `models.py` file contains the SQLAlchemy models for the database tables.
- The `schemas.py` file contains the Pydantic models for the request and response bodies.
- The `data_access_layer.py` file contains the functions used to query the database.
- The `alembic` directory contains the migration scripts as well as the `*.sql` file used to load the data into the
  database.

## Resources

Below are some resources that you will find useful as you continue your journey into utilizing geospatial data to extend
this project.

- [PostGIS Documentation](https://postgis.net)
- [GeoAlchemy Documentation](https://geoalchemy-2.readthedocs.io/en/latest/)
- [Pydantic Validators](https://docs.pydantic.dev/latest/concepts/validators/)
- [Spatial Reference Systems](https://en.wikipedia.org/wiki/Spatial_reference_system)
- [FastAPI Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/)

### Visualization

There are many ways to visualize geospatial data. Database GUIs such as `pgAdmin` and `DBeaver` support viewing geospatial
data. 
The two non-database-GUI ways I view geospatial data most often to  are:

- [QGIS](https://qgis.org/en/site/) - An open-source GIS software
- [Plotly](https://plotly.com/python/maps/) - A Python graphing library

### Data

There are many free sources of geospatial data available online. A good place to start is with government agencies as
they provide free access to their geospatial data.
A large number of datasets can be found on
the [United States Open Data Site](https://catalog.data.gov/dataset/?metadata_type=geospatial) website.
The data for this project was sourced from
the [Pittsburgh Open Data site](https://pghgishub-pittsburghpa.opendata.arcgis.com/).