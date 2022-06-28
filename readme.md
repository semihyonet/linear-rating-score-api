# Review Calculation Restfull API

## Setup

For the Database we are using PostgreSQL and after installing docker to a computer the following command should be
initiated.

```shell
sudo docker run --name pg11 -e POSTGRES_PASSWORD=Password123! -d postgres
```

Change directory into the repository directory

```shell
$ cd challange
```

Start the Data Import operationç. This operation migrates the tables and populates the table with data from a JSON.

```shell
$ python3 -m data-import
```

Run server

```shell
$ python3 -m manage runserver
```


## Sections

### Data Import

The Data Import Module serves the purpose of seeding the database with the correct data.

database_seeder.py is the best place to start checking on the module. 

### Rating Calculator

Calculates the ratings of accommodations by iterating reviews. I'am taking linear weighted avarage of ratings.

### API

There are 3 different apps in the API. It's been written with django and rest_framework. 

- Core
Has the Abstract modules that other apps consumes.
- Accommodations
- Reviews

## What to improve

### Scheduled Calculations

We must calculate the Review's dynamically, therefore instead of calculating each record one by one. The weight and
length and calculation date should be recorded into a cache and only the newest aditions should be calculated to recieve
the rating of an accommodation. The rating calculation job should be scheduled to dispatch on a daily basis. To keep the
ratings fresh. 

### Redis Integration

Currently there are (months) 12 * (possible ratings) 5 = 60 different combinations we are using a cache for. That's why
instead of using Redis I only used local dictionaries.

### Project Structure

It's unwise to have a project structure with API apart from other functionalities such as Data Import(Seed) and Review
Calculation. I created those sections to increase readability and separate the modules. However, they all are dependent
on the API therefore the best restructuring would be to put the reviews under a folder named algorithms>Reviews> and for
the data import module, it would be best to rename is "seeders" and put it together with migrations to a folder named
Database
