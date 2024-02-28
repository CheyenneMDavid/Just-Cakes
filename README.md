# Just Cakes

**Just Cakes**, is a maker of beautiful cakes, that takes online orders and delivers across the UK.

Users of the site are able to browse a gallery of cake according to ingredients, flavours and diet choice.  They can read the reviews of past customers and contribute to the site content when authenticated and make enquiries via a contact form.

___

## Table of Contents

- [Features](#features)
- [List of Applications in product](#list-of-applications-in-product)
- [Pre-requisites](#pre-requisites)
- [Project Planning \& Development](#project-planning--development)
- [Development Approach](#development-approach)
- [Agile Development Process](#agile-development-process)
- [User Stories](#user-stories)
- [Installation](#installation)
- [Use](#use)
- [Testing](#testing)
- [Conclusion](#conclusion)
- [Further Development](#further-development)
- [Deployment](#deployment)
- [Copy / Improve / Contribute](#copy--improve--contribute)
- [Credits, Acknowledgments and Appreciation](#credits-acknowledgments-and-appreciation)



___
___

## Features:
- **Gallery to browse a gallery of cakes**.
  The gallery of cakes is the landing page and showcases the available cakes, organising the display according to their category.
&nbsp;
- **Registration/sign-in/sign-out**.
  The process of registration, signing in and signing out are handled by Allauth.
&nbsp;
- **Ability to create a customer profile**.
&nbsp;
- **Ability to update and delete customer profiles**.
&nbsp;
- **Ability to write reviews, comment on reviews, and delete reviews**.
&nbsp;
- **Ability to add cake images and details via the Django admin**.
  Additional cake data it easily added via the admin panel.
  Here an admin can add new data but also create new categories, flavours etc..  Enabling a greater flexibility.  The only thing that has been hardcoded is a default image that would be displayed if the admin didn't load one for the gallery.
___

## List of Applications in product:
- Customer Accounts
- Cakes
- Reviews
___


## Pre-requisites:

#### For basic functionality:
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
gunicorn 21.2.0
```



## Project Planning & Development:
Reviews:

Table for planning **"Reviews"** database `models.py`

![Reviews Tables Model](static/assets/images_for_readme/reviews-table.png)
___

### Table for planning **Cakes** database models

Defining type:Wedding, Novelty and Birthday. Allergy: GF for Gluten Free. V for plantbased.  Flavours and colors. And a list of the cakes themselves, making them searchable by users of the site when such extra functionality added.

Using Normalization to organize the data, so when changes to the data is required, it's more easily managed.
In doing so, new content for the fields can be created by a site administrator.  The new content being cake names, descriptions and additional categories if the so wish.

The purpose of the tables when planning the structure of the data was not to reflect the exact details of each cake currently available, but instead have the relevant sections.  So whilst I've used some of the names of cakes and data such as gluten free, etc...  The precise details of cakes on the site is subject to change, which was the purpose of the field structure.



![Cake Types](static/assets/images_for_readme/cake-category-table.png)

![Cake color and color association table](static/assets/images_for_readme/cake-colour-association-table.png)

![Cake flavour and flavour association table](static/assets/images_for_readme/cake-flavour-association-table.png)

![Cake List](static/assets/images_for_readme/cake-list.png)

___

Table for planning **Customer Accounts** database models
![Customer Accounts](static/assets/images_for_readme/customer-account-tables.png)
___
## Development Approach
The Just Cakes project, at this stage is simple.  And the functionality could have been more condensed/streamlined.  But I'm purposely spread it out across applications within the main project.  My intention was to keep it structured in a manner that allowed me to add more features further down the line.  With this in mind, I previously had other apps such as "orders" which whilst not being utilized at this point, I did have fields such as account_number,  payment_method, purchase_order_date, delivery_order_date and basket_item_count which would have contributed to this wider functionality. As few as these extra lines of code were sitting latently as they did, demanded that I add a fair amount of comments around them in order to explain their presence, which resulted in an excessive amount of commenting which in turn detracted from the functional code which was more important.  I decided that removing it and inserting it at a later date was the lesser of the two evils, given that the functional code was the important part for assessment.  Not the provisional code for what the functions might do in the future.

- **Decision to use Function Based Views vs Class Based Views**
As I've been developing this project, I've used both function based views and class based views. Initially I had a preference to class based because it's what was shown in the walk throughs, so it was "familiar".  But as I've progressed, I found myself less reliant on patterns of usage that I had learned.  And instead I found myself leaning toward function based views because I found them to be clearer to "me", for what I was wanting to do.  The `models.py` in each application have remained class based because it's more suited to django. Doubtless, as I progress, my need will change. I'll probably move back and forth between classes and functions according to the complexity of tasks or indeed which seems to suit better, as I myself progress in my learning.
&nbsp;
**Since first writing the above**, this has indeed changed.  When adding the facility to comment and considering the facility to update posts, I've chosen to change more toward class based views.  This has been important because this project has is condensed into only three apps which makes for a lot of things in one space, making the code quite hard to read.
Using Classes makes for cleaner more structured and easier to follow structures.
&nbsp;
- **Use of Environment Variables**
I've used an environment variable to control the DEBUG setting, so that it sets to True when I'm working on development of of the application and then to False when it runs in the deployed production mode.  This ensures security in production and detailed error messages in development.  The idea and code was copied from my walkthrough projects with code institute.

## Development Challenges & Solutions.
During the development of *Just Cakes*, I encountered a number of issues. These are some of the notable ones and the solutions I found...

### Renaming for Clarity and Relevance
- **Reviews / Posts**
Initially, I was following the structure of the walkthrough project which consisted of only one application that handled all the functions of posting, commenting, liking etc...  Aware that the scope for growth would make the application crowded, I decided to follow the design principle "Separation of Concerns".  In doing so, I created individual apps to manage the functions.
The Unused applications which I've spoken about, aside, I had separate apps for the customer accounts, the database of cakes and the app that handled to posts.
Initially attempting to adopt the tutorial's naming conventions led to some confusion, particularly with the "reviews" app, which was too narrowly defined and not entirely reflective of its broader purpose in the context of the site.
Add to this, I was struggling with correctly applying singular and plural usage of the words "review/reviews" when naming the files.
**Resolved** I was unsure of how much disruption would have been caused by changing the application's name, so I decided to leave it as "reviews" but chose to change the html files within the application to "post" and "posts" which were more relevant.
&nbsp;
- **The Index.html**
Another issue that only became apparent later was that in my need to name the html pages according to the applications that they belonged to, I lost focus of keeping index.html as a central point.
The purpose of the site was to showcase their cakes, so I decided to make the gallery view of the cakes the landing page and changed the cakes_list.html to index.html
&nbsp;
- **
___

## Agile Development Process

### User Stories

These are a few key user stories that guided the development of *Just Cakes:*

- As a Site User, I can browse a selection of cakes so that I can choose one I like.
- As a Site User, I can like and unlike reviews so that I can show if I found them helpful

- As a Admin, I can search posts using filters such as titles and when the posts were written so that I'm able to find the posts I'm looking for, quicker and more efficiently

For a complete list of user stories, see [My Project Board](https://github.com/users/CheyenneMDavid/projects/30).


___



### Clashes between package extensions.
Initially installing linters and formatters to ensure code quality and consistency.  But as I tried different extensions, after a while this seemed to cause more issues and I was unable to workout what was clashing with what.  So I separated things into a requirements.txt for the stuff that the project was dependant on, in order to run and the stuff that was useful during development was placed in requirements-dev.txt after reading this article: https://realpython.com/lessons/production-vs-development-dependencies/. In the search for way to stop things clashing I eventually came across the term "virtual environment" which people seemed to mention quite a lot on slack.
I eventually did away with the requirements-dev.txt file and setup a virtual environment and installed only the packages I wanted.

### Other issues encountered during development

- **Fork to solve Database Schema and `models.py` Issues**
In the back and forth with the clashing of extensions, At some point the Database Schema and the `models.py` in the customer_accounts app didn't match up.  On one hand I was getting errors saying that the first_name, last_name and memorable_dates weren't recognized after I had added and migrated them.  On the other hand I couldn't migrate them again because I was told that there were no changes detected.  I tried editing the migration files and finally deleted them in the hope of creating fresh migrations, but seemed to come full circle.  Eventually, creating a new database instance which seemed a cleaner way to go forward.
&nbsp;
- **Database Issue**
  When adding functionality to the reviews app, for users to delete their comments, I had a lot of issues with migrating the changes.  Changes weren't showing so couldn't be migrated and it was crashing as it was. Looking to resolve this, I removed the migration files in the hope that changes would be recognised to no avail. Unable to see a way forward I resorted to flushing the database. Even this was still giving me a message that said no changes had been made.
  So I eventually just deleted the database instance at ElephantSQL, created another and re-entered everything again.
  This left me with a lot of files that I had yet to commit, mostly migration ones.  So they were committed in bulk to clear the clutter.
  &nbsp;
  **New Site**
  I was unable to get my svg pattern which I was using as wallpaper to display.  I thought that this was due to the fat that I hadn't set the DISABLE_COLLECTSTATIC in Heroku and after deploying once with it not set, I couldn't seem to simply set it on the deployments there after.  After numerous attempts to get round this which included trying  to use Whitenoise to serve the static files, I eventually reverted to Cloudinary settings for them.  After numerous re-runs and re-dos I can see that it's not the static file that is the issue because the other styling is present.  The SVG pattern is not.  It's not interfering with the functioning so this can me addressed at a later date.
  &nbsp;
  

___
## Installation
*Note on Versioning
It's crucial to use compatible versions of all dependencies to ensure that your project runs smoothly. In this guide, we are using Django version3.

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
For more details, you can refer to the official [Django Documentation](https://www.djangoproject.com).
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

## Testing
### Written Tests

### Manual Testing

#### Test to ensure that a default image is displayed if an image isn't supplied from the Django admin panel or if they are deleted.

**Method**
I tested this by creating a default image which was placed in Cloudinary.  After which I used the admin panel to save cake images, tying them up with the individual cake data, also added via the admin panel.
I then systematically deleted one  from each category from the admin panel.

**Result** -- **Pass**
The screen was rendered using the default images as they should.
Screenshots of default images displaying:
- **Wedding** 
  
![Wedding section](static/assets/images_for_readme/default-wedding-image.png)
- Birthday
  
![Birthday section](static/assets/images_for_readme/default-birthday-image.png)
- Novelty

![Novelty section](static/assets/images_for_readme/default-novelty-image.png)
&nbsp;
**Test images following the same process for the cakes details page.**
- "test-detail-image-1" is the default image when the individual cake doesn't have an image associated with it.
![Default image](static/assets/images_for_readme/test-detail-image-1.png)
&nbsp;
- "test-detail-image-2" is when a cake image was loaded via the Django interface and was associated with the "Hulk cake".
![Associated image](static/assets/images_for_readme/test-detail-image-2.png)

___

## Conclusion

___

## Further Development

Just Cakes is more the business name.  The application's aim is to create and hold accounts, ability to order/buy online.  Further development would be to add a "delivery application" which would tie in with other applications within the over all , holding many of their bits of information as foreign keys in it's own model.

It's because I plan to develop these aspects, I've purposely kept things quite separate.  So that when it's further developed, as aspects of it expand, they won't impinge on one another.  Hence, apparently redundant code such as

___

## Deployment

___

## Copy / Improve / Contribute
### More work needed.
**Code should be implemented to guard against**
- negative number of layers input from admin panel
- Repetition of input for names such as cake names, flavours, etc..

If anyone wishes to copy and improve this software by contributing changes,
please do.  You will find instructions from
[GitHub](https://github.com/) on how to do this
___

## Credits, Acknowledgments and Appreciation.

The reviews application within the just cakes project has been copied from the Code Institute walkthrough django project "codestar".

Picture images have been courtesy of Midjourney and Microsoft's Bing image-creator. Some I have
I have used ChatGPT as a tutor that is on tap, asking it's advice about structure with a view to further development.
The things I needed to consider from a point of practicality and scalability in future development.  That's why there are parts that are dormant.

The favicon.ico is courtesy of [Favicon Generator](https://favicon.io)


Code and the idea for toggling the DEBUG according to environment is courtesy of Code Institute walkthrough projects.

The wallpaper for the site was sourced as a svg file courtesy of [Hero Patterns](https://heropatterns.com/)
___
