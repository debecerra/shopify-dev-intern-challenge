# Inventory Management Web App

This repository contains an inventory tracking web application for a logistics company. This web app was built using Python and Django for the Fall 2022 Shopify Developer Intern Challenge.

[Fall 2022 - Shopify Developer Intern Challenge](https://docs.google.com/document/d/1PoxpoaJymXmFB3iCMhGL6js-ibht7GO_DkCF2elCySU/edit#heading=h.n7bww7g70ipk)

[Fall 2022 - Shopify Production Engineer Intern Challenge](https://docs.google.com/document/d/1cgmV2DW5mEOxhh5ekyopU4Cef07FNalP7WqAJdgpBuw/edit#heading=h.n7bww7g70ipk)

This project meets all requirements for the Shopify Developer Intern Challenge while also having a few extra features to also meet the requirements for the Shopify Production Engineer Intern Challenge.

## Building and Running Locally

This project requires Python 3. Specifically, Python 3.9 was used in development but other versions should work fine as well. It is recommended to use a virtual environment (e.g. venv) to set up dependencies.

```bash
# Set up and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build and run the app
python manage.py migrate
python manage.py runserver
```

## Features
This web application allows for basic CRUD functionality. Users can create inventory items, edit inventory items, delete inventory items and view items in a list. As the additional requirement, users have the ability to create warehouses and assign inventory to specific warehouses. To create an inventory item, users must first create a catalog entry for the item to create as well as a warehouse to store the item. A warehouse can be made in any city from a list of predefined cities (`shopify_dev_intern_challenge/config/cities.yml`). An idea for a future enhancement for this project is to allow for a dynamic list of cities/countries in which warehouses can be created.

This application was build with maintainability and extensibility in mind. The application design, data representation and user interface was designed in a way that easily allows for the addition of new features in the future. The Django ORM helps us enforce data and relational integrity for inventory items, catalog entries and warehouses. Each of these objects is represented as distinct objects in the code, making it easy to add new attributes or define new object types to keep track of new data (e.g. shipments). One design choice that I made is that catalog entries and warehouses cannot be deleted if they are referenced by a inventory item. For example, all inventory items in a warehouse must be moved or deleted before a warehouse can be deleted from the system.

This project interacts with the Open Weather API to obtain current weather data for the cities in which warehouses are located. This weather information is displayed alongside the warehouse and inventory lists. 

# Deployment

I was not able to get the app running on Replit. According to several discussion posts (https://replit.com/talk/ask/Why-is-my-run-button-is-not-working-properly/111814), this appears to be a bug with Replit. After many hours I was able to run the project using the shell but was not able to find a way to deploy the application persistently. However, the project can be found at this Replit link https://replit.com/@debecerra/shopify-dev-intern-challenge. In the Replit development environment, clicking the "Run" button simply does not do anything and does not print anything to the console, installing packages such as Django fail with no error message printed to the console, etc.

Since I was unable to deploy using Replit, I deployed the app on Heroku at the following link https://inventory-app-debecerra.herokuapp.com/.