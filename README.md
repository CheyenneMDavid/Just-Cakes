# *~Just Cakes ~*

*Just Cakes*, is a maker of beautiful cakes, that takes online orders and delivers across the UK.

Users of the site are able to create an account, browse a gallery of available cakes, search according to ingredients, flavours and diet choice, and choose dates for collection or delivery.

*Just Cakes* welcomes feedback and reviews from their customers on a dedicated page.
___
___

## Table of Contents

- [Features](#features)
- [List of Applications](#list-of-applications-in-product)
- [Pre-requisites](#pre-requisites)
- [Project Planning & Development](#project-planning--development)
- [Installation](#installation)
- [Use](#use)
- [Testing of Functions](#testing-of-functions)
- [Further Development](#further-development)
- [Deployment](#deployment)
- [Copy / Improve / Contribute](#copy--improve--contribute)
- [Credits, Acknowledgments and Appreciation to](#credits-acknowledgments-and-appreciation-to)



___
___

## Features
___


## List of Applications in product.
- Core
- Customer Accounts
- Cakes
- Orders
- Reviews

___


## Pre-requisites

#### For basic functionality
```
Django3.2.20
dj-database-url 0.5.0
psycopg2==2.9.7
PostgreSQL
django-allauth 0.55.0
Pillow 10.0.0
cloudinary 1.34.0
dj3-cloudinary-storage 0.0.6
django-cloudinary-storage 0.3.0
```
#### Nice to haves
```
black 23.7.0
pylint-django 2.5.3
gunicorn 21.2.0
```



### Project Planning & Development
Reviews:

Table for planning **"Reviews"** database models.py

![Reviews Tables Model](static/assets/images_for_readme/reviews-table.png)
___

Table for planning **Cakes** database models

Defining type:Wedding, Novelty and Birthday. Allergy: GF for Gluten Free. V for plantbased.  Flavours and colors. And a list of the cakes themselves, making them searchable by users of the site.

Using Normalization to organize the data, so when changes to the data is required, it's more easily managed.



![Cake Types](static/assets/images_for_readme/cake-type.png)

![Cake color and color association table](static/assets/images_for_readme/cake-color-association-table.png)

![Cake flavour and flavour association table](static/assets/images_for_readme/cake-flavour-association-table.png)

![Cake List](static/assets/images_for_readme/cake-list.png)

___

Table for planning **Customer Accounts** database models
![Customer Accounts](static/assets/images_for_readme/customer-account-tables.png)


___
## Installation

*Note on Versioning
It's crucial to use compatible versions of all dependencies to ensure that your project runs smoothly. In this guide, we are using Django version 3.

### Install Django

Code: ```pip3 install 'django<4'```

Notes: Use Django 3.* to ensure compatibility and support.
Initialize the Django Project
Code: django-admin startproject PROJ_NAME .
Notes: The '.' at the end specifies that the project should be created in the current directory.
Create Django Apps

Code: ```python3 manage.py``` startapp APP_NAME
Notes: This will create a new app inside your Django project. Replace APP_NAME with your desired application name.
Running and Configuring the Server
Run the Django Development Server
Code: ```python3 manage.py runserver```

**Additional Information**
For more details, you can refer to the official Django documentation [here](https://www.djangoproject.com).
Register the App in Django Settings

**Prerequisites**
Check the list of required packages in the README file and make sure to install them.

**Also**, you can find guides and help here for:
- [How to deploy on Heroku](https://devcenter.heroku.com/categories/deployment)
- [How to use Cloudinary cloud based media service](https://cloudinary.com/documentation/how_to_integrate_cloudinary#:~:text=The%20best%20way%20to%20get,in%205%20minutes%20or%20less.)
- [How to use Managed PostgreSQL database hosting service](https://www.elephantsql.com/docs/index.html)

## Use

### User: sign-up / sign-in / sign-out
All handled by Allauth


___
___

## Testing of functions

## Conclusion

___

## Further Development

Just Cakes is more the business name.  The application's aim is to create and hold accounts, ability to order/buy online.  Further development would be to add a "delivery application" which would tie in with other applications within the over all , holding many of their bits of information as foreign keys in it's own model.

It's because I plan to develop these aspects, I've purposely kept things quite separate.  So that when it's further developed, as aspects of it expand, they won't impinge on one another.  Hence, apparently redundant code such as 

___

## Deployment

___

## Copy / Improve / Contribute

If anyone wishes to copy and improve this software by contributing changes,
please do.  You will find instructions from
[GitHub on how to do this.]
___

## Credits, Acknowledgments and Appreciation.

Much of this project has been based on the walkthrough tutorials I've had with Code Institute.  The section in Reviews is close to verbatim.

I have used ChatGPT to workout the structure of what I wanted to build.  The things I needed to consider from a point of practicality and scalability in future development.  That's why there are parts that appear redundant at the moment.

I've found it to be the best resource in understanding something because I could just keep asking it to explain a single point, over and over again in different ways until I grasped it.  And it does not get impatient with repeating itself.
Other than the Reviews application, which I have used from the walkthrough project, all of the code is my own.  And because of that, I have not needed to credit anyone in the comments.
I have used ChatGPT as a tutor that is on tap.  But none of the code is written by ChatGPT or any other form of AI (there's no point and also it's unnecessary).
___
