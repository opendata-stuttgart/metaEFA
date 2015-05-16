# meta_efa [![Build Status](https://travis-ci.org/momorientes/metaEFA.svg)](https://travis-ci.org/momorientes/metaEFA)

The easiest way to run the django app is to install Docker and Docker Compose
([Instructions](https://docs.docker.com/compose/install/))


It is advisable to create an alias for docker-compose:
```
alias dc=docker-compose
```

To build the containers run `dc build` if you do this the first time it will take some time.

Then initialize the database:
```
dc run web reset_db
dc run web migrate
```


To run the app (-d for daemonizing => background):
```
dc up [-d]
```


To get a python shell with DB access:
```
dc run web shell_plus
```


After changing something in a model you will need to create migrations:
```
dc run web makemigrations
dc run web migrate
```
