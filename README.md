# [Just Cakes](https://just-cakes-184a064333be.herokuapp.com/)

 [**Just Cakes**](https://just-cakes-184a064333be.herokuapp.com/) is a maker of beautiful cakes, that takes online orders and delivers across the UK.

 delivers custom cakes across the UK. The platform allows users to explore cakes by categories such as Wedding, Birthday, and Novelty, with clear indicators for dietary preferences like gluten-free or plant-based. Customers can view detailed cake descriptions, read reviews, and write reviews of the service when authenticated.

 The site displays a wide range of cakes but if customers want more unusual "one of a kind" cakes, they can contact "Just Cake" via the online contact form to get a conversation going, or dive straight in with a phone-call to the number displayed in the carousel display at the top of the page.

___

## Table of Contents
- [List of Applications in Product](#list-of-applications-in-product)
- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [Project Planning & Development](#project-planning--development)
    - [Database Schema](#database-schema)
    - [Wireframes](#wireframes)
    - [Design Mockups](#design-mockups)
    - [Development Approach](#development-approach)
- [Application Overview and Functionality](#application-overview-and-functionality)
- [Performance Optimization](#performance-optimization)
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




## List of Applications in product:
- Cakes (Homepage / Landing-page / Gallery)
- Customer Accounts
- Reviews
- Contact
___

## Features:
- **Promotional Carousel**
  The homepage features a dynamic Promotional Carousel that continuously scrolls:
  - *Spend over £95 for free delivery*
  - *Click & Collect Available*
  - *Contact phone number for making direct contact*

- **Homepage / Cake Gallery**.
  The homepage acts as the landing page and also the gallery that showcases the cake styles available, all of which are separated into categories of Wedding, Birthday and Novelty so that a user can easily find what they're looking for, but not without having a cursory glance at the variety available, as each cake image is accompanied by the cake name, a short excerpt describing the cake which acts as a link to the detail page of that cake.
  With clear navigation at the top, leading to other parts of the site, including a link for admins of the site to go straight to the django admin panel, a user is able to find their way about, easily.

- **Individual Cake Detail Page**
Once a user selects a cake from our homepage gallery, they are taken to a detailed page dedicated to that cake. The detail page offers an in-depth look at the cake, including larger clear images, a comprehensive description, pricing, and keys to make clear when a cake is plant based or gluten free.

- **User Reviews List Page**
A list page for User Reviews. An image, when uploaded by the user, else a default image.  An excerpt with accompanying photos, when uploaded by the authenticated user, else a default image is provided, with the Authors name, post title, excerpt from the post and the published date and time along with a heart and a number, representing the number of likes.

- **Individual User Review Detail Page**
A page in which the entire post could be read by a user and where comments and likes can be added by authenticated users.

- **Update & Deletion of Profile**
Upon initial registration, users have an account automatically created.  But other than their user name, the fields are empty.  upon sigh in, the authenticated user has the facility to view account via the navigation where they can update the profile or delete it, there by deleting account.

- **Contact Form Submission**
Users, both authenticated and non-authenticated can enter their details with a description of their requirements in a contact for for submission in order to be contacted by Just Cakes.

- **Registration/Sign-In/Sign-Out**: User authentication is managed using Allauth, ensuring a smooth registration, login, and logout process.

- **Customer Profile Management**: Whilst user's profiles are automatically created upon registration, they are in essence blank other than their user name.  Further to this, users can fully create, update, and delete their profiles on the site.
&nbsp;
- **Admin Capabilities**: Admins can easily add cake data, including images 
  and details, via the Django admin panel. Here, admins are able to create new categories, flavours, descriptions and update prices.

## Pre-requisites

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
___
___


## Project Planning & Development:
This section outlines the planning process and development approach for our project. Below is a flowchart diagram that provides a visual representation of the overall functionality of the application.
![](https://res.cloudinary.com/cheymd/image/upload/v1712064156/JustCakes-Readme-images/basic-layout-of-functionality_v0az3y.png)


- **Reviews**:
Table for planning "Reviews" database
![Reviews Tables Model](https://res.cloudinary.com/cheymd/image/upload/v1711207188/JustCakes-Readme-images/reviews-table_1_pv1kw7.png)

- **Customer Accounts**
Table for planning "Customer Accounts" database
![Customer Accounts](https://res.cloudinary.com/cheymd/image/upload/v1711207083/JustCakes-Readme-images/customer-account-tables_1_blheom.png)

- **Cakes**
Table for planning "Cakes" database
Defining type:Wedding, Novelty and Birthday. Allergy: GF for Gluten Free. V for plantbased.  Flavours and colors. And a list of the cakes themselves, making them searchable by users of the site when such extra functionality added.
&nbsp;
Using Normalization to organize the data, so when changes to the data is required, it's more easily managed.
In doing so, new content for the fields can be created by a site administrator.  The new content being cake names, descriptions and additional categories if they so wish.
&nbsp;
The purpose of the tables when planning the structure of the data was not to reflect the exact details of each cake currently available, but instead have the relevant sections.  So whilst I've used some of the names of cakes and data such as gluten free, etc...  The precise details of cakes on the site is subject to change, which was the purpose of the field structure.

#### Cake Categories
![Cake Categories](https://res.cloudinary.com/cheymd/image/upload/v1711207072/JustCakes-Readme-images/cake-category-table_all7hy.png)

####  Cake Colours
![Cake color and color association table](https://res.cloudinary.com/cheymd/image/upload/v1711207069/JustCakes-Readme-images/cake-colour-association-table_1_gvtskc.png)

Cake Flavours
![Cake flavour and flavour association table](https://res.cloudinary.com/cheymd/image/upload/v1711207077/JustCakes-Readme-images/cake-flavour-association-table_1_kxeb5q.png)

Cake List
![Cake List](https://res.cloudinary.com/cheymd/image/upload/v1711207080/JustCakes-Readme-images/cake-list_1_bti57a.png)

___

## Wireframes
For uniformity, all the pages are templates and are served their header and footer by the base.html that extends to them.  The Header consists of a ticker-tape advertizing at the very top, followed by the logo and navigation.  Whilst the footer holds links for social media platforms and a contact form.

The wireframes I created provide an outline of key pages. While these wireframes may not perfectly reflect the final design of the site, they serve as a foundational guide for the layout and structure of the most relevant pages. Below, you'll find wireframe representations of the landing page and detail pages for cakes and posts.  Images, brief details on the list pages and full details accompanying the images on the detail pages, for both the cakes application and also the reviews application.

Not all pages have wireframes.  Pages that are handled by Allauth have such basic elements that I didn't deem it necessary to present these.  Also pages such as the updating of profiles is literally a vertical listing of fields that the page contains, and so didn't change in the mobile view.
The only changes being how the logo and navigation are laid out in the header.  But the changes in these are a constant in all pages when changing from desktop to mobile.

### Desktop Views

#### Wireframe for: Cake List - Desktop View
 ![Landing Page Desktop Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1712045053/JustCakes-Readme-images/desktop-cake-list_ok8ybo.jpg)

#### Wireframe for: Cake Detail - Desktop View 
 ![Cake Detail - Desktop Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1712045055/JustCakes-Readme-images/desktop-cake-detail_oozmzq.jpg)

#### Wireframe for: Post List Desktop View
 
 ![Post List Desktop Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1712045048/JustCakes-Readme-images/desktop-post-list_rjit9b.jpg)

#### Wireframe for: Post Detail Desktop View

![Post Detail Desktop Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1712045050/JustCakes-Readme-images/desktop-post-detail_r5sp7r.jpg)


### Mobile Views

#### Wireframe for: Cake List - Mobile View
| ![Landing Page Mobile Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1712045043/JustCakes-Readme-images/mobile-cake-list_mfprek.jpg)

#### Wireframe for: Cake Detail - Mobile View
![Cake Detail - Mobile Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1712045046/JustCakes-Readme-images/mobile-cake-detail_pcvukn.jpg)

#### Wireframe for: Post List Mobile View
![Post List Mobile View Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1712045039/JustCakes-Readme-images/mobile-post-list_ivas1f.jpg)

#### Wireframe for: Post Detail Mobile View
![Post Detail Mobile View Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1712045041/JustCakes-Readme-images/mobile-post-detail_sbttxr.jpg)

#### Wireframe for: Update Profile Form
![Update Profile Form](https://res.cloudinary.com/cheymd/image/upload/v1712045058/JustCakes-Readme-images/update-profile-form_ll9txl.jpg)
___
___

## Mockups
In this section, you'll find visual representations of the site's design and layout through mockups. These mockups provide a detailed preview of how the various pages and components will appear to users. They serve as a visual guide for the development process and help ensure consistency in design across different screen sizes and devices.
![Mockup - All Devices](https://res.cloudinary.com/cheymd/image/upload/v1712048533/all-devices-black_gac35v.png)
___
___

## Development Approach
The Just Cakes project, at this stage is simple.  And the functionality could have been more condensed/streamlined.  But I'm purposely spread it out across applications within the main project.  My intention was to keep it structured in a manner that allowed me to add more features further down the line.  With this in mind, I previously had other apps such as "orders" which whilst not being utilized at this point, I did have fields such as account_number,  payment_method, purchase_order_date, delivery_order_date and basket_item_count which would have contributed to this wider functionality. As few as these extra lines of code were sitting latently as they did, demanded that I add a fair amount of comments around them in order to explain their presence, which resulted in an excessive amount of commenting which in turn detracted from the functional code which was more important.  I decided that removing it and inserting it at a later date was the lesser of the two evils, given that the functional code was the important part for assessment.  Not the provisional code for what the functions might do in the future.

- **Decision to use Function Based Views vs Class Based Views**
As I've been developing this project, I've used both function based views and class based views. Initially I had a preference to class based because it's what was shown in the walk throughs, so it was "familiar".  But as I've progressed, I found myself less reliant on patterns of usage that I had learned.  And instead I found myself leaning toward function based views because I found them to be clearer to "me", for what I was wanting to do at times.

  **Since first writing the above**, this has indeed changed.  When adding the facility to comment and considering the facility to update posts, I've swayed toward class based views.  This has been important because this project, has functionalities that are squeezed into very few apps which makes for a lot of things in one space, making the code quite hard to read.
Using Classes makes for cleaner code and easier to follow structures.  But doubtless both ways have their place.
&nbsp;
- **Use of Environment Variables**
I've used an environment variable to control the DEBUG setting, so that it sets to True when I'm working on development of of the application and then to False when it runs in the deployed production mode.  This ensures security in production and detailed error messages in development.  The idea and code was copied from my walkthrough projects with code institute.
___
___

## Application Overview and Functionality of Individual Apps.
This section explains the functionality of each application within the Just Cakes project.
Explanations are provided for how each app works, supported by screenshots to illustrate their operation and design.  This overview provides insights and understanding of the structure and behavior of the applications, offering a clear view of their roles within the overall project.

### Cakes Application Overview.
The Cakes application is intended as the core of the project as the purpose is to showcase the cake designs that are available to order.

Cakes that are fitting for a small children's birthday party or the extreme high level of craftsmanship in designing, creating and providing custom cake designs for the most austentatious occasion.

Utilizing Bootstrap for a responsive layout, the application curates a visually stunning gallery on the homepage, divided into categories like Wedding, Birthday, and Novelty cakes. This categorization aids users in effortlessly navigating through the collection, ensuring a seamless browsing experience.

#### Homepage/Landing-Page/Gallery (Desktop-view)
![Homepage Desktop-view](https://res.cloudinary.com/cheymd/image/upload/v1711207194/JustCakes-Readme-images/homepage-desktop-view_tqgzdx.png)

#### Homepage/Landing-Page/Gallery (Tablet-view)
I've purposely screen-shotted the view that a tablet such as the Samsung Galaxy S6 would have, rather than show a mobile view because the single image screen shot that a mobile would have created would have been excessively long.
![Homepage Tablet-view](https://res.cloudinary.com/cheymd/image/upload/v1711213481/JustCakes-Readme-images/homepage-tablet-view_r9sgnv.png)

#### Dynamic Cake Detail Presentation
For each cake, the application dynamically generates a detail page, enriched with high-resolution images fetched from Cloudinary, comprehensive descriptions, pricing information, and dietary indicators (e.g., plant-based, gluten-free). This page is designed to provide all the necessary information a user might need to make an informed decision, enhancing transparency and trust.

&nbsp;
![Individual Cake Detail](https://res.cloudinary.com/cheymd/image/upload/v1712069531/JustCakes-Readme-images/cakes-detail_xqhkul.png)

&nbsp;
#### Responsive Image Handling
With an emphasis on performance and user experience, images are requested in webp format to ensure faster load times without compromising on quality. A default image with a "coming soon" placeholder is displayed in cases where specific cake images are not available, maintaining a consistent and professional look across the platform.  Already viewable in the above whole page screenshots, this is the individual page's appearance of default image that would be displayed in the place of the correct cake.  I'm differentiating between this and a normal default image because the purpose is to advertise specific cake styles that are available for order, so a "coming soon" image is more suitable.
Integration of navigational elements, such as a "Back to Our Cakes" button on the cake detail page, ensures users can easily return to the main page without the need to use browser navigation.

![Coming Soon Detail](https://res.cloudinary.com/cheymd/image/upload/v1712070694/JustCakes-Readme-images/detail-coming-soon_sbcqv7.png)
___

### Customer Accounts Overview.
Central to the Customer Accounts App is the the customer's profile.  At first this may seem surplus to requirements however, ultimately the application is to be evolve into one that can be fully utilized by a fully "automated" order and delivery/booked collection system, at which point the more detailed nature of Customer Accounts will come into its own.

  Screenshot of the Individual user's account detail/profile page with buttons to return home, update their profile or delete their profile which would also delete their account.
  ![Profile Page](https://res.cloudinary.com/cheymd/image/upload/v1712226451/JustCakes-Readme-images/profile-details_wydnup.png)

&nbsp;
- **Profile Creation and Update**: Initially blank when initially created and associated with a user, the individual customer profile can be updated by the user.  Validation is in place for details such as phone numbers and postcodes using regex and custom validation logic in `forms.py`
  
&nbsp;
Update Profile Form with fields to update, help text to guide the user and an update button.
![](https://res.cloudinary.com/cheymd/image/upload/v1712227329/JustCakes-Readme-images/update-profile-form_fpcptt.png)

### Reviews Application Overview.
The Reviews application bears witness to the quality and bespoke nature of what "Just Cakes" offers its customers in way of professional service and the stunning skill of it's staff in how any style of cake is undertaken for any event.
The application features:

- **Read Reviews**: Unauthenticated users can browse reviews, gaining insights from the experiences of others.
- **Write Reviews**: Authenticated users can write reviews, comment and like posts to show what they found useful.

Screenshot of the posts list page showing excerpts of each post
![posts list](https://res.cloudinary.com/cheymd/image/upload/v1711334249/JustCakes-Readme-images/posts-list-page_siozgi.png)
&nbsp;
&nbsp;

View of a single post page showing number of comments and like for a post and also facility for commenting for authenticated users.
![post detail](https://res.cloudinary.com/cheymd/image/upload/v1711334255/JustCakes-Readme-images/single-post_z1od6s.png)
___

### Contact Application Overview.
The Contact form is accessible from all pages and can be used by authenticated users and unauthenticated users alike.  In the admin panel, the form data can be listed and filtered according to when the forms were received.  To ensure valid data upon form submission, django manages the email address validation, but I've used a regex pattern and a message that tells the user to enter a valid UK phone number if they enter an invalid one.
The regex pattern I've used for validating the phone numbers is from StackOverflow and I've credited it as such in the `forms.py` file itself.
Upon successful form submission, the user gets an onscreen message thanking them, which lasts for 3 seconds before they are then redirected to the homepage.

Screenshot of the "contact form"
![Contact Form](https://res.cloudinary.com/cheymd/image/upload/v1712271776/JustCakes-Readme-images/contact-form_oc4pby.png)

Screenshot of successful contact form submission
![Upon Submitting a contact form](https://res.cloudinary.com/cheymd/image/upload/v1712272553/JustCakes-Readme-images/contact-form-submission_sjib1a.png)
___

## Performance Optimization

To help pages load faster, I've utilised webp where I could.  The images that I have loaded into cloudinary were loaded as webp and when using the dynamic templating to bring them back, the logic I've used requested them from cloudinary as webp, wherever possible.

### Performance Insights

I used Google's "Lighthouse" to measure my site.  Measuring only the main pages, I gained the following scores, of which I've screenshotted the readouts from Lighthouse.

Index Page Desktop Lighthouse Score
![Index Desktop View](https://res.cloudinary.com/cheymd/image/upload/v1712508049/JustCakes-Readme-images/index-page-lighthouse-desktop-score_i43r3o.png)

Index Page Mobile Lighthouse Score
![Index Mobile View](https://res.cloudinary.com/cheymd/image/upload/v1712508048/JustCakes-Readme-images/index-page-lighthouse-mobile-score_ymrbcq.png)

Cake Detail Desktop Lighthouse Score
![Cake Detail Desktop View](https://res.cloudinary.com/cheymd/image/upload/v1712426926/JustCakes-Readme-images/cake-detail-lighthouse-desktop-score_qf9oby.png)

Cake Detail Mobile Lighthouse Score
![Cake Detail Mobile View](https://res.cloudinary.com/cheymd/image/upload/v1712426925/JustCakes-Readme-images/cake-detail-lighthouse-mobile-score_zihdh0.png)


Post List Page Desktop Lighthouse Score
![Post List Desktop View](https://res.cloudinary.com/cheymd/image/upload/v1712501267/JustCakes-Readme-images/post-list-lighthouse-desktop-score_j98snw.png)

Post List Page Mobile Lighthouse Score
![Post List Mobile View](https://res.cloudinary.com/cheymd/image/upload/v1712501268/JustCakes-Readme-images/post-list-lighthouse-mobile-score_pycud6.png)

Post Detail Page Desktop Lighthouse Score
![Post Detail Desktop View](https://res.cloudinary.com/cheymd/image/upload/v1712501268/JustCakes-Readme-images/post-detail-lighthouse-desktop-score_lyw9dw.png)

Post Detail Page Mobile Lighthouse Score
![Post Detail Mobile View](https://res.cloudinary.com/cheymd/image/upload/v1712501267/JustCakes-Readme-images/post-detail-lighthouse-mobile-score_cwkxiu.png)

___

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
- **Customer Accounts versus Customer Profiles**
Not being definitive about customer accounts or customer profiles, the boundaries between the two were blurred, even impacting the logic of what things did.  It was only after a mass-renaming of files that I was able to separate things which resulted in having better logic of how templates where connected to one another and also the logic of what they displayed in relation to one another.
&nbsp;
- **Truncated Excerpts** When looking at why excerpts of posts weren't dynamically displaying, I realised that I had fields for "content" and a field literally called "excerpt".  I had been double thinking this and they were attempting to serve the same purpose.  Unfortunately thinking of the word "excerpt" I kept focus on that and used it when trying to serve it up dynamically.  But it was the content fields that was saving the data.  When realising this, I dropped "excerpt" from the post model and used "content correctly".
I then went about creating new content for the posts so that the posts each had a reasonable number of words before I could make use of truncating down to 25 words.  So I copy pasted generic text in via the admin panel, attributing it to various users.
However... Upon rendering the screen the copy and pasting had taken html styles across and although it didn't show when entering in via the admin panel, it did show in the render.
I tried to clean the output by using ```{{ post.content|striptags }}``` and that did work, but not with truncation, so I decided to not bother with the striptags command on the bases that users would normally be entering text a fresh and this issue is unlikely to arise.
  

### Deployment Challenges and Solutions
  To simplify things to a level where I had less to look at I once again removed the environmental variables that controlled DEBUG and ALLOWED_HOSTS and hardcoded these into the django settings file.
  The ongoing issue was finally resolved when I tried to manually disable the collect static by logging into Heroku via my console and using:
  `heroku config:set DISABLE_COLLECTSTATIC=0` which gave me a return saying that it couldn't find the app.
  Somehow heroku was referencing an application that had previously been deleted.
  Explicitly specifying the app name with:
  `heroku config:set DISABLE_COLLECTSTATIC=0 --app just-cakes` seemed to break this link, solved the situation and enabled me to replace the hardcoded settings with the environmental variables.



- **Authenticated Users vs Customer account.**
  Initially having this set to ensure that whenever a user registered, hence becoming an "authenticated" user, a customer account/profile was created.  This also worked in reverse in that if a user where to delete their profile, their corresponding account in the customer_accounts application would also be deleted and the user would then be redirected to the sign-up page.

- **Code Validation Issues**
  During the validation process using the [W3C Markup Validation Service](https://validator.w3.org/), I received informational messages stating ```Trailing slash on void elements has no effect and interacts badly with unquoted attribute values.``` and was advised to remove them.  I did attempt to do this but as soon as I would hit "save", these would return.  I attempted to change this default behavior by from my IDE by going into my settings, but was unable to find how to change it.
  One such message was regarding trailing slashes on void elements, which have no effect and may interact badly with unquoted attribute values.
  
Additionally, the validation process highlighted other potential issues, including compliance with HTML and CSS standards, ensuring proper nesting of elements, and addressing any deprecated or non-standard attributes. These messages served as valuable feedback, guiding me to refine and improve the quality of my markup code.
___
___

## Agile Development Process
**Agile-Inspired Development Approach**.
This project was guided by an "Agile-inspired" approach in that, without a team or base to which I could goto in order to get others to check, test and provide feedback, I often found myself taking this role in order to assess what I needed to do next.  This made for a slow process, but it did provide an environment that allowed for continual change.  Often I would utilise family and friends who had no technical knowledge whatsoever to use aspects of the site, whilst I gained feedback by way of observing how they went about things, given what I placed in-front of them.  And also listening to what they had to say of their experience.

In retrospect, while this approach was instrumental for refining the UX, I recognize that it was less systematic for developing functionality. This realization underscores the importance of maintaining methodical development practices even when working in a flexible, Agile-influenced manner.

**Iterative Development**
The development unfolded in an iterative manner. Without predefined sprints, I tackled the project in small, manageable increments. Each commit in the version history represents a step in this journey, sometimes forward and occasionally a step back, reflecting an organic, exploratory process as I developed both the project and also my own ability.

**Continuous Adaptation**
Embracing change, one of the Agile's key values, was essential. When functionality didn't work as it was supposed to, or when a better solution was discovered, I adjusted accordingly.  This resulted in a commit history that didn't follow a strict linear path, but did reflect an adaptability and willingness to make changes wherever needed.

**Self-Managed Process**
Lacking a team environment in which stand-ups could be used to track progress, identify obstacles, and plan strategies to overcome them, I created a daily handover book to myself which consisted of a list of tasks that needed doing, a ticking off, of the tasks as they were done and a plan for the next day.  It was a liner method, but one that navigated according to need as required, creating fresh lists and tasks as things evolved.

**Tools for Agile Management**
I used Git for version control and tracking which allowed me to create branches, try out ideas, discard them or keep them depending on how they played out.

**Reflection and Growth**
My solo journey with this project has been as much about learning Agile practices as it has been about developing the application itself. The process has been documented honestly, warts and all, to showcase not just the final product but the resilience and continuous learning that went into creating it.

### User Stories

These are a few key user stories that guided the development of *Just Cakes:*

- As a **Site User**, I can **browse a selection of cakes** so that I can **choose one I like**.
- As a **Site User**, I can **like and unlike reviews** so that I can **show if I found them helpful**

- As a **Admin**, I can **search posts using filters such as titles and when the posts were written** so that I'm **able to find the posts I'm looking for, quicker and more efficiently**

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
  I was unable to get my svg pattern which I was using as wallpaper to display.  I thought that this was due to the fact that I hadn't set the DISABLE_COLLECTSTATIC in Heroku and after deploying once with it not set, I couldn't seem to simply set it on the deployments there after.  After numerous attempts to get round this which included trying  to use Whitenoise to serve the static files, I eventually reverted to Cloudinary settings for them.  After numerous re-runs and re-dos I can see that it's not the static file that is the issue because the other styling is present.  The SVG pattern is not.  It's not interfering with the functioning so this can me addressed at a later date.
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
___
___

## Use

### User: sign-up / sign-in / sign-out
All handled by Allauth
When signing in, there's a timed display telling the user that they are signed in successfully.  The green message informing the user has a close button in the form of an "X".  Whilst it is functional, it's more cosmetic because although a user can click it, the message times out and the screen changes quickly.

### Using the Navigation
Use of the navigation is limited or extended according to whether someone is signed in or not.
When not signed in or unauthenticated use of the navigation is limited to
-Home, Reviews, Sign-in and Sign-up and a direct link to the Admin page.  When Authenticated, the navigation consists of a Home, Reviews, A statement saying who the user is signed in as, A View account button and a sign-out button.

Home takes a user to the gallery of cakes whilst the Reviews button takes a user to the Reviews section. Regardless of whether they are authenticated or not.

If a user is authenticated and signed in, they can click on the "View Account which then takes them to the account detail page where they can view their profile details, update them and delete their account."

### Updating and deleting a profile
When a user signs up, a profile is created, albeit a blank/empty one.
The navigation takes the user to the customer accounts profile page which displays the user's details.  From this page the user can update the blank profile and also delete it, which also deletes their authentication and access to the site until they complete the sign-up process again.
The fields aren't compulsory and the user can choose which fields they update.

### Reviews, Creating Posts and Commenting
The reviews page that the navigation takes a user to, provides the unauthenticated user to read excerpts of each review, so they can choose which they want to read in full in the post's detail page.  At the bottom of this page, there is page navigation,  If there is sufficient posts to create more pages and a button that says "write a review" for the authenticated user who wishes to add to the reviews page.  Also, for the authenticated user, at the bottom of the detail of an individual post is a comments box where a authenticated user can contribute to the individual post.
The authenticated user can also like posts, which adds to the likes count which is displayed under a post.
 
RE-START HERE!  RE-START HERE!  RE-START HERE!  RE-START HERE!  


___
___

## Testing
### Written Tests
- **Comment Form in Reviews App**
Tests for the comment form in the reviews app are copied from the Code Institute walkthrough project called Codestar. The code for which can be found here:
![Comment Form - pass](reviews/tests/tests_forms.py)

&nbsp;
- **Updating Profile Form in Customer_Accounts App**
The test passes for ```test_invalid_form()``` demonstrated the expected errors, as deliberate invalid data was intentionally passed to the form for validation.
**Screenshot of console from test**:
![Deliberate invalid data](https://res.cloudinary.com/cheymd/image/upload/v1711505142/JustCakes-Readme-images/update-profile-form-test-console-display_bl37p9.png)
![Update Profile Form - pass](/customer_accounts/tests/test_forms.py)

&nbsp;
- **User Sign-up/Sign-in/Sign-out**
![Sign-Up, Sign-in, Sign-out - pass](/tests/test_authentication.py)

&nbsp;
- **Contact Form Submission**
![Contact Form Submission - pass](/contact/tests.py)


&nbsp;
- **Cake Models**
![Cake Models - pass](/cakes/tests/tests.py)
&nbsp;
**All Tests Passed.**
![](https://res.cloudinary.com/cheymd/image/upload/v1711513147/JustCakes-Readme-images/all-tests_awc3ew.png)
___

### Manual Testing

#### Test to ensure that a default image is displayed if an image isn't supplied from the Django admin panel or if they are deleted.

**Method**
I tested this by creating a default image which was placed in Cloudinary.  After which I used the admin panel to save cake images, tying them up with the individual cake data, also added via the admin panel.
I then systematically deleted one  from each category from the admin panel.

**Result** -- **Pass**
The screen was rendered using the default images as they should.
Screenshots of default images displaying:

- **Wedding**

![Wedding section](https://res.cloudinary.com/cheymd/image/upload/v1711207106/JustCakes-Readme-images/default-wedding-image_rqnmyg.png)

&nbsp;
- **Birthday**

![Birthday section](https://res.cloudinary.com/cheymd/image/upload/v1711207086/JustCakes-Readme-images/default-birthday-image_cbmgli.png)

&nbsp;
- **Novelty**

![Novelty section](https://res.cloudinary.com/cheymd/image/upload/v1711207106/JustCakes-Readme-images/default-wedding-image_rqnmyg.png)
&nbsp;
___
**Test images following the same process for the cakes details page.**

"**test-detail-image-1**" is the default image when the individual cake doesn't have an image associated with it.
 
&nbsp;
![Default image](https://res.cloudinary.com/cheymd/image/upload/v1711207183/JustCakes-Readme-images/test-detail-image-1_o6v6qg.png)

&nbsp;
"**test-detail-image-2**" is when a cake image was loaded via the Django interface and was associated with the "Hulk cake".

![Associated image](https://res.cloudinary.com/cheymd/image/upload/v1711207191/JustCakes-Readme-images/test-detail-image-2_qvyb6q.png)

___
___

## Code Validation and Quality Assurance

### HTML Validation
As stated in the "Deployment Challenges and Solutions" section, I used https://validator.w3.org to validate my code.  Any issues that were raised were addressed.
The only issue raised there was the matter of trailing slashes which would always return upon saving, despite removing them.

### CSS Validation
Both the project's stylesheets (style.css & custom.css) have been validated with the W3C CSS Validator, confirming adherence to the latest CSS standards.
[![Valid CSS](http://jigsaw.w3.org/css-validator/images/vcss)](http://jigsaw.w3.org/css-validator/check/referer)

### Python Code Quality
For my Python code, I used Black to enforce formatting, ensuring readability and consistency, closely following but not limited to PEP 8 standards. This approach not only helped in maintaining clean code but also contributed to the overall quality of my project.



___
___

## Conclusion
The conclusion for this project is very much one that is about me and the learning I am taking from this.
This project has been a pretty profound learning journey, characterized not just by the development of a web application but also by significant personal and professional growth.  Looking back on the process, now, I'd say that they center round the critical importance of planning and also a willingness in asking for help when hitting a brick wall, rather than repeated smash into it until either breaking through or finally climbing over.

### The Impact of Insufficient Planning
The absence of a detailed plan at the project's inception led to numerous challenges. These ranged from features either creeping in due to not defining the structure, and getting so drawn into individual parts that I forgot to ensure certain aspects were present as I went forward.
This lack of foresight resulted in a development process that ran me, rather than me running it.

### The Impact of Not Reaching Out
Not reaching out has been a significant stumbling block and has cost me a great deal of time. Only upon stepping back from things, I've seen with far more clarity that sometimes overly analyzing something resulted in paralysis. Also, sometimes, the problems that I "thought" were an issue weren't actually mine to solve. I refer to the types of deprecation warnings and other error messages that led me down rabbit holes of troubleshooting, only to realize later that they were either unrelated to my project or could have been easily resolved with a simple update or configuration adjustment. These experiences have underscored the importance of seeking guidance and collaboration when facing challenges, as well as the need to differentiate between critical issues that require immediate attention and those that can be safely ignored or addressed at a later stage.

Despite the challenges and time-consuming detours caused by navigating through these issues, ultimately they've contributed to not just my growth but my actual skill development. Each rabbit hole I found myself in, broadened my skills in areas, parallel to what I was doing.  So, whilst experiences may have prolonged project timelines in the short term, they have equipped me with a deeper understanding of software development and equipped me with problem-solving strategies that will undoubtedly hugely benefit me in future.
Navigating through this chaos, I gained valuable insights and a deeper understanding of software dependencies, version compatibility issues, and the importance of staying informed about evolving technologies, has been immeasurable.

___

## Further Development

Just Cakes is more the business name.  The application's aim is to create and hold accounts with data that would enable the fully automated ordering and delivery of goods and services.
Services that would allow for a calendar bookings for:
- Booking for delivery
- Bookings for collection
- Bookings for taster days which would allow the customers to come and sample the types of cake that they would potentially be ordering.
- Payment features
- Instalment payment features.

Further to this, whilst currently, customers are able to communicate via the contact forms and telephone as to how they may want a one off cake designed, the addition of a user centric front end in which a customer would have a graphical interface from which they can design their own cakes, is planned.
___

## Deployment


___

## Copy / Improve / Contribute
### More work needed.
**Code should be implemented to guard against**
Performance speeds of loading need to be improved.

If anyone wishes to copy and improve this software by contributing changes,
please do.  You will find instructions from
[GitHub](https://github.com/) on how to do this
___

## Credits, Acknowledgments and Appreciation.

The reviews application within the just cakes project has been copied from the Code Institute walkthrough django project "codestar".
StackOverflow for Regex patterns and how to implement them.
Picture images have been courtesy of Midjourney and Microsoft's Bing image-creator. Some I have
I have used ChatGPT as a tutor that is on tap, asking it's advice about structure with a view to further development and also advice on completing aspects of this readme, in how I should go about things.  Sometimes to my detriment because it would get carried away, resulting in me having to scrub work and redo it.
Code Institute Tutors for help when I reached out.
The favicon.ico is courtesy of [Favicon Generator](https://favicon.io)
https://websitemockupgenerator.com


Code and the idea for toggling the DEBUG according to environment is courtesy of Code Institute walkthrough projects.

The wallpaper for the site was sourced as a svg file courtesy of [Hero Patterns](https://heropatterns.com/)
___
