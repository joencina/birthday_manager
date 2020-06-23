[![codecov](https://codecov.io/gh/joencina/birthday_manager/branch/master/graph/badge.svg?token=SA86H36CCQ)](https://codecov.io/gh/joencina/birthday_manager)
# Introduction

## Description
Birthday Manager is a minimalist Django web app to organize birthdays. The deployed version shows a useful case 
scenario by displaying a large set of birthdays scraped from a social network.

Check out the Heroku-deployed version at http://www.encina.xyz

## Functions

Currently, the Birthday Manager supports:
- Displaying today's birthdays
- Adding a new contact
- Searching a contact's birthday by name
- Displaying a full list of contacts ordered by their birthdays


# Local reproduction

If you want to explore this project from your own computer, clone this repository, make a new pipenv environment and follow the steps below.
You need to have a working version of Postgres installed beforehand.

#### Create a database
Run `scripts/setup.sh` (credits to Travis Jungroth)

#### Install dependencies
    pipenv install --dev
    
#### Run
    ./manage.py runserver