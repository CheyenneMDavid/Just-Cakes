# [Just Cakes](https://just-cakes-184a064333be.herokuapp.com/)

[**Just Cakes**](https://just-cakes-184a064333be.herokuapp.com/) is a maker of beautiful cakes, that takes online orders and delivers across the UK.

delivers custom cakes across the UK. The platform allows users to explore cakes by categories such as Wedding, Birthday, and Novelty, with clear indicators for dietary preferences like gluten-free or plant-based. Customers can view detailed cake descriptions, read reviews, and write reviews of the service when authenticated.

The site displays a wide range of cakes but if customers want more unusual "one of a kind" cakes, they can contact "Just Cake" via the online contact form to get a conversation going, or dive straight in with a phone-call to the number displayed in the carousel display at the top of the page.

---

## Table of Contents

- [Just Cakes](#just-cakes)
  - [Table of Contents](#table-of-contents)
  - [List of Applications in product:](#list-of-applications-in-product)
  - [Features:](#features)
    - [Promotional Carousel](#promotional-carousel)
    - [Homepage / Cake Gallery](#homepage--cake-gallery)
    - [Individual Cake Detail Page](#individual-cake-detail-page)
    - [User Reviews List Page](#user-reviews-list-page)
    - [Individual User Review Detail Page](#individual-user-review-detail-page)
    - [Update \& Deletion of Profile](#update--deletion-of-profile)
    - [Contact Form Submission](#contact-form-submission)
    - [Registration/Sign-In/Sign-Out](#registrationsign-insign-out)
    - [Customer Profile Management](#customer-profile-management)
    - [Admin Capabilities](#admin-capabilities)
  - [Pre-requisites](#pre-requisites)
    - [For basic functionality:](#for-basic-functionality)

## List of Applications in product:

- Cakes (Homepage / Landing-page / Gallery)
- Customer Accounts
- Reviews
- Contact

---

## Features:

### Promotional Carousel

The homepage features a dynamic Promotional Carousel that continuously scrolls:

- _Spend over £95 for free delivery_
- _Click & Collect Available_
- _Contact phone number for making direct contact_

### Homepage / Cake Gallery

The homepage acts as the landing page and also the gallery that showcases the cake styles available, all of which are separated into categories of Wedding, Birthday and Novelty so that a user can easily find what they're looking for, but not without having a cursory glance at the variety available, as each cake image is accompanied by the cake name, a short excerpt describing the cake which acts as a link to the detail page of that cake.
With clear navigation at the top, leading to other parts of the site, including a link for admins of the site to go straight to the django admin panel, a user is able to find their way about, easily.

### Individual Cake Detail Page

Once a user selects a cake from our homepage gallery, they are taken to a detailed page dedicated to that cake. The detail page offers an in-depth look at the cake, including larger clear images, a comprehensive description, pricing, and keys to make clear when a cake is plant based or gluten free.

### User Reviews List Page

A list page for User Reviews. An image, when uploaded by the user, else a default image. An excerpt with accompanying photos, when uploaded by the authenticated user, else a default image is provided, with the Authors name, post title, excerpt from the post and the published date and time along with a heart and a number, representing the number of likes.

### Individual User Review Detail Page

A page in which the entire post could be read by a user and where comments and likes can be added by authenticated users.

### Update & Deletion of Profile

Upon initial registration, users have an account automatically created. But other than their user name, the fields are empty. upon sigh in, the authenticated user has the facility to view account via the navigation where they can update the profile or delete it, there by deleting account.

### Contact Form Submission

Users, both authenticated and non-authenticated can enter their details with a description of their requirements in a contact for for submission in order to be contacted by Just Cakes.

### Registration/Sign-In/Sign-Out

User authentication is managed using Allauth, ensuring a smooth registration, login, and logout process.

### Customer Profile Management

Whilst user's profiles are automatically created upon registration, they are in essence blank other than their user name. Further to this, users can fully create, update, and delete their profiles on the site.

### Admin Capabilities

Admins can easily add cake data, including images
and details, via the Django admin panel. Here, admins are able to create new categories, flavours, descriptions and update prices.

---

## Pre-requisites

### For basic functionality:

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

---

## Project Planning & Development:

This section outlines the planning process and development approach for our project. Below is a flowchart diagram that provides a visual representation of the overall functionality of the application.

![](https://res.cloudinary.com/cheymd/image/upload/v1712064156/JustCakes-Readme-images/basic-layout-of-functionality_v0az3y.png)

### Database Schema

### Table for planning "Reviews" database

![Reviews Tables Model](https://res.cloudinary.com/cheymd/image/upload/v1711207188/JustCakes-Readme-images/reviews-table_1_pv1kw7.png)

### Table for planning "Customer Accounts" database

![Customer Accounts](https://res.cloudinary.com/cheymd/image/upload/v1711207083/JustCakes-Readme-images/customer-account-tables_1_blheom.png)

### Table for planning "Cakes" database

Defining type:Wedding, Novelty and Birthday. Allergy: GF for Gluten Free. V for plant-based. Flavours and colors. And a list of the cakes themselves, making them searchable by users of the site when such extra functionality added.

Using Normalization to organize the data, so when changes to the data is required, it's more easily managed.
In doing so, new content for the fields can be created by a site administrator. The new content being cake names, descriptions and additional categories if they so wish.

The purpose of the tables when planning the structure of the data was not to reflect the exact details of each cake currently available, but instead have the relevant sections. So whilst I've used some of the names of cakes and data such as gluten free, etc... The precise details of cakes on the site is subject to change, which was the purpose of the field structure.
&nbsp;

#### Cake Categories

![Cake Categories](https://res.cloudinary.com/cheymd/image/upload/v1711207072/JustCakes-Readme-images/cake-category-table_all7hy.png)

#### Cake Colours

![Cake color and color association table](https://res.cloudinary.com/cheymd/image/upload/v1711207069/JustCakes-Readme-images/cake-colour-association-table_1_gvtskc.png)

#### Cake Flavours

![Cake flavour and flavour association table](https://res.cloudinary.com/cheymd/image/upload/v1711207077/JustCakes-Readme-images/cake-flavour-association-table_1_kxeb5q.png)

#### Cake List

![Cake List](https://res.cloudinary.com/cheymd/image/upload/v1711207080/JustCakes-Readme-images/cake-list_1_bti57a.png)

---

## Wireframes

For uniformity, all the pages are templates and are served their header and footer by the base.html that extends to them. The Header consists of a ticker-tape advertizing at the very top, followed by the logo and navigation. Whilst the footer holds links for social media platforms and a contact form.

The wireframes I created provide an outline of key pages. While these wireframes may not perfectly reflect the final design of the site, they serve as a foundational guide for the layout and structure of the most relevant pages. Below, you'll find wireframe representations of the landing page and detail pages for cakes and posts. Images, brief details on the list pages and full details accompanying the images on the detail pages, for both the cakes application and also the reviews application.

Not all pages have wireframes. Pages that are handled by Allauth have basic elements which enable functionality. Other than font size and colors, there is no customization,. Also pages such as the updating of profiles is literally a vertical listing of fields that the page contains, and so didn't change in the mobile view. The only changes being how the logo and navigation are laid out in the header. But such changes are constant when changing from desk/laptop to mobile and are demonstrated as such in the wireframes that are present in this README.

### Wireframes for Desktop Views

#### Index page / Cake List / Landing Page desktop view

![Landing Page Desktop Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1712045053/JustCakes-Readme-images/desktop-cake-list_ok8ybo.jpg)

#### Cake Detail Page desktop view

![Cake Detail - Laptop Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1712045055/JustCakes-Readme-images/desktop-cake-detail_oozmzq.jpg)

#### Post List Page desktop view

![Post List - Laptop Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1724212479/JustCakes-Readme-images/wireframe-post-list_pshvue.jpg)

#### Post Detail Page desktop view

![Post Detail - Laptop Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1712045050/JustCakes-Readme-images/desktop-post-detail_r5sp7r.jpg)

---

### Wireframes for Mobile Views

#### Index page / Cake List / Landing Page mobile view

The Cake List (index page) are scrolling lists. This frame, which is shown in blue and also represents the area which would be a clickable link to the detail page, shows what a single cake list view would contain before repeating the content for another cake for the list page.

![Landing Page / Cakes list Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1724616950/cake-list-mobile-view_yo6cjv.jpg)

#### Cake Detail Page mobile view

![Cake Detail - Mobile Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1724616950/cake-detail-mobile-view_b2segq.jpg)

#### Post List Page mobile view

The Post List is a scrolling list of posts. This frame, which is shown in blue and also represents the area which would be a clickable link to the detail page, shows what a single post list view would contain before repeating the content for another post for the list page.
&nbsp;

![Post List - Mobile Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1724616949/post-list-mobile-view_cq2jxm.jpg)

#### Post Detail Page mobile view

The comment box is only available to authenticated users.

![Post Detail - Mobile View Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1724616950/post-details-mobile-view_gnqxvx.jpg)

#### Account Detail Page mobile view

![Customer Account Mobile View Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1724616950/customer-details-mobile-view_k5fwnc.jpg)

#### Update Profile Form mobile view

![Update Profile Form - Mobile View Wireframe](https://res.cloudinary.com/cheymd/image/upload/v1724616950/details-update-mobile-view_rdk9vd.jpg)

---

## Mockups

In this section, you'll find visual representations of the site's design and layout through mockups. These mockups provide a detailed preview of how the various pages and components will appear to users. They serve as a visual guide for the development process and help ensure consistency in design across different screen sizes and devices.
![Mockup - All Devices](https://res.cloudinary.com/cheymd/image/upload/v1712048533/all-devices-black_gac35v.png)

---

## Development Approach

The Just Cakes project, at this stage is simple. And the functionality could have been more condensed/streamlined. But I'm purposely spread it out across applications within the main project. My intention was to keep it structured in a manner that allowed me to add more features further down the line. With this in mind, I previously had other apps such as "orders" which whilst not being utilized at this point, I did have fields such as account_number, payment_method, purchase_order_date, delivery_order_date and basket_item_count which would have contributed to this wider functionality. As few as these extra lines of code were sitting latently as they did, demanded that I add a fair amount of comments around them in order to explain their presence, which resulted in an excessive amount of commenting which in turn detracted from the functional code which was more important. I decided that removing it and inserting it at a later date was the lesser of the two evils, given that the functional code was the important part for assessment. Not the provisional code for what the functions might do in the future.

- **Decision to use Function Based Views vs Class Based Views**
  As I've been developing this project, I've used both function based views and class based views. Initially I had a preference to class based because it's what was shown in the walkthroughs, so it was "familiar". But as I've progressed, I found myself less reliant on patterns of usage that I had learned. And instead I found myself leaning toward function based views because I found them to be clearer to "me", for what I was wanting to do at times.

  **Since first writing the above**, this has indeed changed. When adding the facility to comment and considering the facility to update posts, I've swayed toward class based views. This has been important because this project, has functionalities that are squeezed into very few apps which makes for a lot of things in one space, making the code quite hard to read.
  Using Classes makes for cleaner code and easier to follow structures. But doubtless both ways have their place.
  &nbsp;

- **Use of Environment Variables**
  I've used an environment variable to control the DEBUG setting, so that it sets to True when I'm working on development of of the application and then to False when it runs in the deployed production mode. This ensures security in production and detailed error messages in development. The idea and code was copied from my walkthrough projects with code institute.

---

## Development Decisions

- **Switching to "only" WebP Format** for Images for the landing page and also the cake detail page.
  Previously having the option of images to be served up as JPG or WebP, the performance was poor.
  Initially setting out to ensure that everything was served as WebP, I realised that the poor performance was not just due to the image format.

- **But also the excessive CSS that was redundant**. Initially, I looked online for help on how to automate the search for redundant CSS, but when following instructions on implementation, I was getting error messages that would send me down rabbit holes. This is happened too many times, so I instead carried out a manual but systematic search through the custom.css for the occurrences of class names in the HTML files with the command `git grep -l '<class name being searched for>' -- '**/*html'`, deleting the classes that didn't return any listings and testing for changes.

- **User Friendly vs Efficiency**
  The landing page is the gallery view which promotes the bespoke cakes that Just Cakes creates and supply. The gallery is maintained by an admin whose is responsible for ensuring that the various lines of cakes are shown to their best. On this bases, I decided that whilst it would be "nice" to make the uploading of cake images a little less regimented for the experience of an admin that was maintaining the site, it was more important that the experience of the user who would be browsing the pages of the site, be a a more fluid process.

- This would be different to the Reviews page that both admins and users
  were able to contribute
  toward. With this in mind I decided that only using WebP images for the cakes gallery was
  orientated toward the user experience... The Reviews page would be less regimented in its formats, for precisely the same reason. Uploading posts and accompanying images should be conditional, because you can't account for every eventuality. But not unfriendly, and so other formats could be uploaded.

- **Optimization of post_list.html Layout and the re-aligning of other HTMLs**.
  Initially when writing the post list page, I followed the format and structure of "Django Blog, CodeStar" which was a Code Institute walkthrough project, but whilst it gave me a workable template that I could use immediately. As I customised the HTML, I drifted further and further from the original structure, but as I did, I neglected to removed unnecessary classes, both bootstrap and ones that that had been defined in the original stylesheet.css.

  It was the process of using Lighthouse, looking at the scores and studying how these scores were calculated, that led me to brave away from the HTML structure that still resembled the walkthrough project and make the layout work better for "me".

  The Lighthouse advice on shifts in the layout resulted in me restructuring how I wanted the images, authors, and excerpts to display. There seemed no quick way to remove unnecessary CSS which Lighthouse suggested was contributing toward the poor performance, so I manually searched for occurrences of a class by using `git grep -l '<classname>' -- '**/*.*'`, slowly removing what seemed to be unnecessary. This did improve things, but the issue of image sizes still remained, despite changing to WebP format for faster loading. Searching the web for ways to size my images in a more efficient way I found https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images, which explained how to use the srcset and sizes attributes. Not feeling confident with the use of these attributes and the syntax they required, I found online help here: https://johnfraney.ca/tools/responsive-image-generator. It allowed me to load in an image and then be presented with the code block, albeit not the sizes I required. Armed with a better understanding of the syntax surrounding the srcset and sizes attributes, I found further help from "BrowserStack" at https://www.browserstack.com/guide/common-screen-resolutions from which I took the measurements for the most common screen sizes and used them in my srcset and sizes settings. Working with them, I added the media-queries, measurements for which I'd taken from BrowserStack and chosen devices that met these measurements using https://blisk.io/devices. Blisk was particularly helpful when setting up the measurements for Emulated Devices in devtools.

---

## Formatters and Linters

After migrating my Gitpod workspace due to a change in how I needed to access the IDE, I noticed changes in code formatting. This led to reinstalling and changing formatters and linters.
Unfortunately, the configurations that I’d previously relied on when installing via the Gitpod Marketplace UI, didn’t seem to work correctly.

### Python Related

In settings.json, blocks of code that related to Python files were greyed out and showed as “Unknown Configuration”. Attempting to understand why this was the case led me to uninstalling and re-installing extensions, checking paths to the packages and updating them from running globally to reaching my virtual environment. Despite the changes made, the configurations that were related to Python remained unrecognised. I understand Pylint to be widely used and actively maintained too for checking quality of Python code, but despite this it was causing warnings of depreciation. In the search to understand why I came across Ruff which claimed to be a simpler, faster and more streamlined tool. Changing to Ruff resulted many of the settings that weren’t going to be included in Newer versions of Pylint as it developed, and so the deprecation warnings came to an end. I’ve not been able to understand why the Python specific configurations which are separate to Ruff remain unrecognised and yet do seem to have effect on files.

### Prettier

Warnings about Beautify being deprecated have been continuous, but these warnings have since changed to saying that Beautify was no longer being supported.
I chose Prettier and ESLint from the Gitpod marketplace for all file formats other than Python. But the settings that normal installation provides didn’t work. The configuration and settings I finally arrived at were a result of guidance, explanations and advice in the form of tutoring by ChatGPT from OpenAI.
This covered the converting of .eslintrc to eslint.config.js, inclusion of the ignore property as opposed to a separate .eslintignore and an additional stylelintrc.json which enables settings that stopped false errors and allowed for specified units such as “["em", "rem", "%", "s"]”
To ensure that the automatic loading of Beautify didn’t clash with prettier settings, I removed it from .gitpod.yml file

---

## Application Overview and Functionality of Individual Apps.

This section explains the functionality of each application within the Just Cakes project.
Explanations are provided for how each app works, supported by screenshots to illustrate their operation and design. This overview provides insights and understanding of the structure and behavior of the applications, offering a clear view of their roles within the overall project. All screen shots are shown in laptops resolutions of 1366 x 768 or 360 x 800, inline with Samsung Galaxy S20 and similar devices.

### Cakes Application Overview.

The Cakes application is intended as the core of the project as the purpose is to showcase the cake designs that are available to order.

Cakes that are fitting for a small children's birthday party or the extreme high level of craftsmanship in designing, creating and providing custom cake designs for the most austentatious occasion.

Utilizing Bootstrap for a responsive layout, the application curates a visually stunning gallery on the homepage, divided into categories like Wedding, Birthday, and Novelty cakes. This categorization aids users in effortlessly navigating through the collection, ensuring a seamless browsing experience.

#### Homepage/Landing-Page/Gallery (Laptop-view)

![Homepage Laptop-view](https://res.cloudinary.com/cheymd/image/upload/v1724208859/JustCakes-Readme-images/homepage-laptop-view_qrxzwi.png)

#### Homepage/Landing-Page/Gallery (Mobile-view)

The tablet view of the desktop is much the same as the laptop view, so I've chosen to omit it. This is the mobile view.
![Homepage Mobile-view](https://res.cloudinary.com/cheymd/image/upload/v1724209336/JustCakes-Readme-images/homepage-mobile-view_gfqtnw.png)

#### Dynamic Cake Detail Presentation

For each cake, the application dynamically generates a detail page, enriched with high-resolution images fetched from Cloudinary, comprehensive descriptions, pricing information, and dietary indicators (e.g., plant-based, gluten-free). This page is designed to provide all the necessary information a user might need to make an informed decision, enhancing transparency and trust.

##### Laptop View

![Individual Cake Laptop-view](https://res.cloudinary.com/cheymd/image/upload/v1724209608/JustCakes-Readme-images/cake-detail-laptop-view_y4duif.png)

##### Mobile View

![Individual Cake Mobile View](https://res.cloudinary.com/cheymd/image/upload/v1724209608/JustCakes-Readme-images/cake-detail-mobile-view_rcdjyx.png)

#### Responsive Image Handling

With an emphasis on performance and user experience, images are requested to be delivered by cloudinary in WebP format by adding `?fm=webp` and `&w=400` to specify the image size and the `srcset` and `sizes` attributes so that the browsers can select the best image size according to the device being used.
A default image with a "coming soon" placeholder is displayed in cases where specific cake images are not available, maintaining a consistent and professional look across the platform. Already viewable in the above whole page screenshots, this is the individual page's appearance of default image that would be displayed in the place of the correct cake. I'm differentiating between this and a normal default image because the purpose is to advertise specific cake styles that are available for order, so a "coming soon" image is more suitable.
Integration of navigational elements, such as a "Back to Our Cakes" button on the cake detail page, ensures users can easily return to the main page without the need to use browser navigation.

## ![Coming Soon Detail](https://res.cloudinary.com/cheymd/image/upload/v1721181874/coming-soon-default_c5vvlj.webp)

### Customer Accounts Overview.

Central to the Customer Accounts App is the the customer's profile. At first this may seem surplus to requirements however, ultimately the application is to be evolve into one that can be fully utilized by a fully "automated" order and delivery/booked collection system, at which point the more detailed nature of Customer Accounts will come into its own.

Screenshot of the Individual user's account detail/profile page with buttons to return home, update their profile or delete their profile which would also delete their account.
![Profile Page](https://res.cloudinary.com/cheymd/image/upload/v1712226451/JustCakes-Readme-images/profile-details_wydnup.png)

Profile Creation and Update
Initially blank when initially created and associated with a user, the individual customer profile can be updated by the user. Validation is in place for details such as phone numbers and postcodes using regex and custom validation logic in `forms.py`

Update Profile Form with fields to update, help text to guide the user and an update button.
![](https://res.cloudinary.com/cheymd/image/upload/v1712227329/JustCakes-Readme-images/update-profile-form_fpcptt.png)

### Reviews Application Overview.

The Reviews application bears witness to the quality and bespoke nature of what "Just Cakes" offers its customers in way of professional service and the stunning skill of it's staff in how any style of cake is undertaken for any event.
The application features:

- **Read Reviews**: Unauthenticated users can browse reviews, gaining insights from the experiences of others.
- **Write Reviews**: Authenticated users can write reviews, comment and like posts to show what they found useful.

Screenshot of the posts list page showing excerpts of each post
![posts list](https://res.cloudinary.com/cheymd/image/upload/v1724208480/JustCakes-Readme-images/posts-list-page_hkzlba.png)

View of a single post page showing number of comments and like for a post and also facility for commenting for authenticated users.
![post detail](https://res.cloudinary.com/cheymd/image/upload/v1711334255/JustCakes-Readme-images/single-post_z1od6s.png)

---

### Contact Application Overview.

The Contact form is accessible from all pages and can be used by authenticated users and unauthenticated users alike. In the admin panel, the form data can be listed and filtered according to when the forms were received. To ensure valid data upon form submission, django manages the email address validation, but I've used a regex pattern and a message that tells the user to enter a valid UK phone number if they enter an invalid one.
The regex pattern I've used for validating the phone numbers is from StackOverflow and I've credited it as such in the `forms.py` file itself.
Upon successful form submission, the user gets an onscreen message thanking them, which lasts for 3 seconds before they are then redirected to the homepage.

#### Screenshot of the "contact form"

![Contact Form](https://res.cloudinary.com/cheymd/image/upload/v1712271776/JustCakes-Readme-images/contact-form_oc4pby.png)

#### Screenshot of successful contact form submission

![Upon Submitting a contact form](https://res.cloudinary.com/cheymd/image/upload/v1712272553/JustCakes-Readme-images/contact-form-submission_sjib1a.png)

---

## Performance Optimization

Needing images to load faster, I've utilized WebP format when uploading for the site, but realized that this doesn't guarantee how they're delivered back for the site, especially when users may upload in jpg or png formats. To overcome this, I used `?fm=webp` to ask for images to be delivered in the format I wanted and `&w=400` for the size I wanted.

### Lazy Loading Images

To improve loading times, I implemented lazy loading selectively across the site. Lazy loading is applied to images on pages where the content is below the fold and not immediately visible to the user, which improves performance by only loading images as they're needed, as they come into view. The one place that lazy loading was not of benefit was the index page because, when in mobile view, regardless of which images followed, the first image of the wedding cakes section would always be above the fold.

Unfortunately this isn't a strategy I could use to the same end in the posts_list.html

### Performance Insights

I used Google's "Lighthouse" to measure my site. Measuring only the main pages, I gained the following scores, of which I've screen shotted the readouts from Lighthouse.

#### Index / Cake List / Gallery Page (Desktop)

![index.html desktop score](https://res.cloudinary.com/cheymd/image/upload/v1724272304/JustCakes-Readme-images/desktop-cake-list_cthxxk.png)

#### Cake Detail / Gallery Page (Desktop)

![cake_detail.html desktop score](https://res.cloudinary.com/cheymd/image/upload/v1724272304/JustCakes-Readme-images/desktop-cake-detail_a4htnt.png)

#### Post List Page (Desktop)

![post_list.html desktop score](https://res.cloudinary.com/cheymd/image/upload/v1724272303/JustCakes-Readme-images/desktop-post-list_qmzohi.png)

#### Post Detail Page (Desktop)

![post_detail.html desktop score](https://res.cloudinary.com/cheymd/image/upload/v1724272303/JustCakes-Readme-images/desktop-post-detail_tazncc.png)

#### Index / Cake List / Gallery Page (Mobile)

![index.html mobile score](https://res.cloudinary.com/cheymd/image/upload/v1724272303/JustCakes-Readme-images/mobile-cake-list_wblwhf.png)

#### Cake Detail (Mobile)

![cake_detail.html mobile score](https://res.cloudinary.com/cheymd/image/upload/v1724272306/JustCakes-Readme-images/mobile-cake-detail_gdgpbe.png)

#### Post List Page (Mobile)

![post_list.html mobile score](https://res.cloudinary.com/cheymd/image/upload/v1724272306/JustCakes-Readme-images/mobile-post-lisl_qrxhyd.png)

#### Post Detail Page (Mobile)

![post_detail.html mobile score](https://res.cloudinary.com/cheymd/image/upload/v1724272305/JustCakes-Readme-images/mobile-post-detail_dgt5po.png)

---

## Development Challenges & Solutions.

During the development of _Just Cakes_, I encountered a number of issues. These are some of the notable ones and the solutions I found...

### Renaming for Clarity and Relevance

- **Reviews / Posts**
  Initially, I was following the structure of the walkthrough project which consisted of only one application that handled all the functions of posting, commenting, liking etc... Aware that the scope for growth would make the application crowded, I decided to follow the design principle "Separation of Concerns". In doing so, I created individual apps to manage the functions.
  The Unused applications which I've spoken about, aside, I had separate apps for the customer accounts, the database of cakes and the app that handled to posts.
  Initially attempting to adopt the tutorial's naming conventions led to some confusion, particularly with the "reviews" app, which was too narrowly defined and not entirely reflective of its broader purpose in the context of the site.
  Add to this, I was struggling with correctly applying singular and plural usage of the words "review/reviews" when naming the files.
  **Resolved** I was unsure of how much disruption would have been caused by changing the application's name, so I decided to leave it as "reviews" but chose to change the HTML files within the application to "post" and "posts" which were more relevant.

- **The Index.html**
  Another issue that only became apparent later was that in my need to name the HTML pages according to the applications that they belonged to, I lost focus of keeping index.html as a central point.
  The purpose of the site was to showcase their cakes, so I decided to make the gallery view of the cakes the landing page and changed the cakes_list.html to index.html

- **Customer Accounts versus Customer Profiles**
  Not being definitive about customer accounts or customer profiles, the boundaries between the two were blurred, even impacting the logic of what things did. It was only after a mass-renaming of files that I was able to separate things which resulted in having better logic of how templates where connected to one another and also the logic of what they displayed in relation to one another.

- **Truncated Excerpts** When looking at why excerpts of posts weren't dynamically displaying, I realised that I had fields for "content" and a field literally called "excerpt". I had been double thinking this and they were attempting to serve the same purpose. Unfortunately thinking of the word "excerpt" I kept focus on that and used it when trying to serve it up dynamically. But it was the content fields that was saving the data. When realising this, I dropped "excerpt" from the post model and used "content correctly".

  I then went about creating new content for the posts so that the posts each had a reasonable number of words before I could make use of truncating down to 25 words. So I copy pasted generic text in via the admin panel, attributing it to various users.
  However... Upon rendering the screen the copy and pasting had taken HTML styles across and although it didn't show when entering in via the admin panel, it did show in the render.
  I tried to clean the output by using `{{ post.content|striptags }}` and that did work, but not with truncation, so I decided to not bother with the striptags command on the bases that users would normally be entering text a fresh and this issue is unlikely to arise.

### Improved Layout

- **Removal of unwanted classes**: In the cakes list page, both the header and the footer didn't act as expected as I shrunk the window. It was fine in all the other pages. This led me looking at unrequired classes. I removed all the container-fluid classes from the all HTML files except for the base.html which was being extended to all other HTMLs, relying on the single container-fluid class that was in the body tag.

- **Clickable Cards**: Originally I had just the titles of posts in the list pages or the paragraph content in the cake gallery as the links to their respective detail pages. In both cases I made the entire cards clickable which made for a better user experience.

These changes improved the overall structure, responsiveness, and usability of the website.

### Deployment Challenges and Solutions

To simplify things to a level where I had less to look at I once again removed the environmental variables that controlled DEBUG and ALLOWED_HOSTS and hardcoded these into the django settings file.
The ongoing issue was finally resolved when I tried to manually disable the collect static by logging into Heroku via my console and using:
`heroku config:set DISABLE_COLLECTSTATIC=0` which gave me a return saying that it couldn't find the app.
Somehow heroku was referencing an application that had previously been deleted.
Explicitly specifying the app name with:
`heroku config:set DISABLE_COLLECTSTATIC=0 --app just-cakes` seemed to break this link, solved the situation and enabled me to replace the hardcoded settings with the environmental variables.

- **Authenticated Users vs Customer account.**
  Initially having this set to ensure that whenever a user registered, hence becoming an "authenticated" user, a customer account/profile was created. This also worked in reverse in that if a user where to delete their profile, their corresponding account in the customer_accounts application would also be deleted and the user would then be redirected to the sign-up page.

- **Code Validation Issues**
  During the validation process using the [W3C Markup Validation Service](https://validator.w3.org/), I received informational messages stating `Trailing slash on void elements has no effect and interacts badly with unquoted attribute values.` and was advised to remove them. I did attempt to do this but as soon as I would hit "save", these would return. I attempted to change this default behavior by from my IDE by going into my settings, but was unable to find how to change it.
  One such message was regarding trailing slashes on void elements, which have no effect and may interact badly with unquoted attribute values.

Additionally, the validation process highlighted other potential issues, including compliance with HTML and CSS standards, ensuring proper nesting of elements, and addressing any deprecated or non-standard attributes. These messages served as valuable feedback, guiding me to refine and improve the quality of my markup code.

---

## Agile Development Process

### Agile-Inspired Development Approach

This project was guided by an "Agile-inspired" approach in that, without a team or base to which I could goto in order to get others to check, test and provide feedback, I often found myself taking this role in order to assess what I needed to do next. This made for a slow process, but it did provide an environment that allowed for continual change. Often I would utilise family and friends who had no technical knowledge whatsoever to use aspects of the site, whilst I gained feedback by way of observing how they went about things, given what I placed in-front of them. And also listening to what they had to say of their experience.

In retrospect, while this approach was instrumental for refining the UX, I recognize that it was less systematic for developing functionality. This realization underscores the importance of maintaining methodical development practices even when working in a flexible, Agile-influenced manner.

### Iterative Development

The development unfolded in an iterative manner. Without predefined sprints, I tackled the project in small, manageable increments. Each commit in the version history represents a step in this journey, sometimes forward and occasionally a step back, reflecting an organic, exploratory process as I developed both the project and also my own ability.

### Continuous Adaptation

Embracing change, one of the Agile's key values, was essential. When functionality didn't work as it was supposed to, or when a better solution was discovered, I adjusted accordingly. This resulted in a commit history that didn't follow a strict linear path, but did reflect an adaptability and willingness to make changes wherever needed.

### Self-Managed Process

Lacking a team environment in which stand-ups could be used to track progress, identify obstacles, and plan strategies to overcome them, I created a daily handover book to myself which consisted of a list of tasks that needed doing, a ticking off, of the tasks as they were done and a plan for the next day. It was a liner method, but one that navigated according to need as required, creating fresh lists and tasks as things evolved.

### Tools for Agile Management

I used Git for version control and tracking which allowed me to create branches, try out ideas, discard them or keep them depending on how they played out.

### Reflection and Growth

My solo journey with this project has been as much about learning Agile practices as it has been about developing the application itself. The process has been documented honestly, warts and all, to showcase not just the final product but the resilience and continuous learning that went into creating it.

### User Stories

These are a few key user stories that guided the development of _Just Cakes:_

- As a **Site User**, I can **browse a selection of cakes** so that I can **choose one I like**.
- As a **Site User**, I can **like and unlike reviews** so that I can **show if I found them helpful**

- As a **Admin**, I can **search posts using filters such as titles and when the posts were written** so that I'm **able to find the posts I'm looking for, quicker and more efficiently**

For a complete list of user stories, see [My Project Board](https://github.com/users/CheyenneMDavid/projects/30).

---

### Clashes between package extensions.

Initially installing linters and formatters to ensure code quality and consistency. But as I tried different extensions, after a while this seemed to cause more issues and I was unable to workout what was clashing with what. So I separated things into a requirements.txt for the stuff that the project was dependant on, in order to run and the stuff that was useful during development was placed in requirements-dev.txt after reading this article: https://realpython.com/lessons/production-vs-development-dependencies/. In the search for way to stop things clashing I eventually came across the term "virtual environment" which people seemed to mention quite a lot on slack.
I eventually did away with the requirements-dev.txt file and setup a virtual environment and installed only the packages I wanted.

### Other issues encountered during development

- **Fork to solve Database Schema and `models.py` Issues**
  In the back and forth with the clashing of extensions, At some point the Database Schema and the `models.py` in the customer_accounts app didn't match up. On one hand I was getting errors saying that the first_name, last_name and memorable_dates weren't recognized after I had added and migrated them. On the other hand I couldn't migrate them again because I was told that there were no changes detected. I tried editing the migration files and finally deleted them in the hope of creating fresh migrations, but seemed to come full circle. Eventually, creating a new database instance which seemed a cleaner way to go forward.

- **Database Issue**
  When adding functionality to the reviews app, for users to delete their comments, I had a lot of issues with migrating the changes. Changes weren't showing so couldn't be migrated and it was crashing as it was. Looking to resolve this, I removed the migration files in the hope that changes would be recognised to no avail. Unable to see a way forward I resorted to flushing the database. Even this was still giving me a message that said no changes had been made.
  So I eventually just deleted the database instance at ElephantSQL, created another and re-entered everything again.
  This left me with a lot of files that I had yet to commit, mostly migration ones. So they were committed in bulk to clear the clutter.

  **New Site**
  I was unable to get my svg pattern which I was using as wallpaper to display. I thought that this was due to the fact that I hadn't set the DISABLE_COLLECTSTATIC in Heroku and after deploying once with it not set, I couldn't seem to simply set it on the deployments there after. After numerous attempts to get round this which included trying to use Whitenoise to serve the static files, I eventually reverted to Cloudinary settings for them. After numerous re-runs and re-dos I can see that it's not the static file that is the issue because the other styling is present. The SVG pattern is not. It's not interfering with the functioning so this can me addressed at a later date.

---

## Installation

### Note on Versioning

It's crucial to use compatible versions of all dependencies to ensure that your project runs smoothly. In this guide, we are using Django version3.

### Install Django

Code: `pip3 install 'django<4'`
Notes: Use Django 3.\* to ensure compatibility and support.
Initialize the Django Project
Code: django-admin startproject PROJ_NAME .
Notes: The '.' at the end specifies that the project should be created in the current directory.

### Create Django Apps

Code: `python3 manage.py` startapp APP_NAME
Notes: This will create a new app inside your Django project. Replace APP_NAME with your desired application name.

### Running and Configuring the Server

### Run the Django Development Server

Code: `python3 manage.py runserver`

### Additional Information

For more details, you can refer to the official [Django Documentation](https://www.djangoproject.com).
Register the App in Django Settings

**Prerequisites**
Check the list of required packages in the README file and make sure to install them.

**Also**, you can find guides and help here for:

- [How to deploy on Heroku](https://devcenter.heroku.com/categories/deployment)
- [How to use Cloudinary cloud based media service](https://cloudinary.com/documentation/how_to_integrate_cloudinary#:~:text=The%20best%20way%20to%20get,in%205%20minutes%20or%20less.)
- [How to use Managed PostgreSQL database hosting service](https://www.elephantsql.com/docs/index.html)

---

## Use

### User: sign-up / sign-in / sign-out

All handled by Allauth
When signing in, there's a timed display telling the user that they are signed in successfully. The green message informing the user has a close button in the form of an "X". Whilst it is functional, it's more cosmetic because although a user can click it, the message times out and the screen changes quickly.

### Using the Navigation

Use of the navigation is limited or extended according to whether someone is signed in or not.
When not signed in or unauthenticated use of the navigation is limited to
-Home, Reviews, Sign-in and Sign-up and a direct link to the Admin page. When Authenticated, the navigation consists of a Home, Reviews, A statement saying who the user is signed in as, A View account button and a sign-out button.

Home takes a user to the gallery of cakes whilst the Reviews button takes a user to the Reviews section. Regardless of whether they are authenticated or not.

If a user is authenticated and signed in, they can click on the "View Account which then takes them to the account detail page where they can view their profile details, update them and delete their account."

### Updating and deleting a profile

When a user signs up, a profile is created, albeit a blank/empty one.
The navigation takes the user to the customer accounts profile page which displays the user's details. From this page the user can update the blank profile and also delete it, which also deletes their authentication and access to the site until they complete the sign-up process again.
The fields aren't compulsory and the user can choose which fields they update.

### Reviews, Creating Posts and Commenting

The reviews page that the navigation takes a user to, provides the unauthenticated user to read excerpts of each review, so they can choose which they want to read in full in the post's detail page. At the bottom of this page, there is page navigation, If there is sufficient posts to create more pages and a button that says "write a review" for the authenticated user who wishes to add to the reviews page. Also, for the authenticated user, at the bottom of the detail of an individual post is a comments box where a authenticated user can contribute to the individual post.
The authenticated user can also like posts, which adds to the likes count which is displayed under a post.

### Browsing Cakes

The index page serves as the landing page where users are able to browse cakes available to order, listed under their category. Each item in the index page consists of a cake image, an excerpt of the cake's description, and acts as a link to the detail page for that page where the user will have a larger detailed picture, a fuller description of the cake which specifies whether it is gluten-free or plant-based, using a font-awesome icon, making it quick and easy to understand.

---

## Testing

### Written Tests

**Comment Form in Reviews App**

Tests for the comment form in the reviews app are copied from the Code Institute walkthrough project called Codestar. The code for which can be found here:  
[Comment Form - pass](reviews/tests/tests_forms.py)

**Updating Profile Form in Customer_Accounts App**

The test passes for `test_invalid_form()` demonstrated the expected errors, as deliberate invalid data was intentionally passed to the form for validation.

**Screenshot of console from test:**

![Deliberate invalid data](https://res.cloudinary.com/cheymd/image/upload/v1711505142/JustCakes-Readme-images/update-profile-form-test-console-display_bl37p9.png)

[Update Profile Form - pass](customer_accounts/tests/test_forms.py)

- **User Sign-up/Sign-in/Sign-out**  
  [Sign-Up, Sign-in, Sign-out - pass](/tests/test_authentication.py)

- **Contact Form Submission**  
  [Contact Form Submission - pass](/contact/tests.py)

- **Cake Models**  
  [Cake Models - pass](/cakes/tests/tests.py)

**All Tests Passed.**

![All tests passed](https://res.cloudinary.com/cheymd/image/upload/v1711513147/JustCakes-Readme-images/all-tests_awc3ew.png)

---

### Manual Testing

#### Test to ensure that a default image is displayed if an image isn't supplied from the Django admin panel or if they are deleted.

**Method**
I tested this by creating a default image which was placed in Cloudinary. After which I used the admin panel to save cake images, tying them up with the individual cake data, also added via the admin panel.
I then systematically deleted one from each category from the admin panel.

**Result** -- **Pass**
The screen was correctly rendered using the generic default image in place of the missing image. This is a screenshot of the process taking place in "Wedding Cakes". The process was also successfully repeated in the sections for Birthday and Novelty Cakes.

**Screenshot of the Default Image Displaying in the index page, within the Wedding Cakes section:**
![Default Image](https://res.cloudinary.com/cheymd/image/upload/v1724690742/JustCakes-Readme-images/default-list-cake-image_akhnwg.png)

**Test images following the same process for the cake's details page.**
The default image also appeared on the individual cake detail page when no specific image was provided.

![Default Image](https://res.cloudinary.com/cheymd/image/upload/v1724690741/JustCakes-Readme-images/default-detail-cake-image_zebrty.png)

---

## Code Validation and Quality Assurance

### HTML Validation

As stated in the "Deployment Challenges and Solutions" section, I used https://validator.w3.org to validate my code.

The only issue raised there was the matter of trailing slashes which would always return upon saving, despite removing them.

**Validation Summary for the Just Cakes [Landing Page](https://just-cakes-184a064333be.herokuapp.com/)**

- Status: Document checking completed. No errors or warnings to show.
- Parser Used: HTML parser
- Character Encoding: UTF-8
- Total Execution Time: 341 milliseconds
- Note: The validation process returned 39 informational messages, which do not affect the functionality or compliance of the HTML
  code.

**Screenshots of the Validation Process:**

_Validation by URL_

![URL Validation](https://res.cloudinary.com/cheymd/image/upload/v1724694449/JustCakes-Readme-images/index-no-erros-or-warnings_bt0vae.png)

_Validation Results:_

![Validation Results](https://res.cloudinary.com/cheymd/image/upload/v1724694448/JustCakes-Readme-images/index-url-being-validated_fma8tz.png)

**Validation Summary for the Just Cakes [Review Page](https://just-cakes-184a064333be.herokuapp.com/reviews/)**

- Status: Document checking completed. No errors or warnings to show.
- Parser Used: HTML parser
- Character Encoding: UTF-8
- Total Execution Time: 280 milliseconds
- Note: The validation process returned 22 informational messages, which do not affect the functionality or compliance of the HTML
  code.

**Screenshots of the Validation Process:**

_Validation by URL_

![URL Validation](https://res.cloudinary.com/cheymd/image/upload/v1724695847/JustCakes-Readme-images/reviews-url-being-validated_fhy1ye.png)

_Validation Results:_

![Validation Results](https://res.cloudinary.com/cheymd/image/upload/v1724695847/JustCakes-Readme-images/reviews-no-erros-or-warnings_jws8zx.png)

### CSS Validation

The project's stylesheets (`style.css` & `custom.css`) have been validated with the W3C CSS Validator, confirming adherence to the latest CSS standards.

- [![Valid CSS](http://jigsaw.w3.org/css-validator/images/vcss)](http://jigsaw.w3.org/css-validator/validator?uri=https://res.cloudinary.com/cheymd/raw/upload/v1724758573/style_css_hisofr.css) Validate `style.css`

- [![Valid CSS](http://jigsaw.w3.org/css-validator/images/vcss)](http://jigsaw.w3.org/css-validator/validator?uri=https://res.cloudinary.com/cheymd/raw/upload/v1724755200/custom_css_zlbnqr.css) Validate `custom.css`

**Note:** The validation may show warnings related to browser-specific CSS properties (like `-webkit-transform` and `-moz-transform`). These are automatically included by the framework or tools used and are not custom additions by me. These warnings can be safely ignored as they do not impact the overall validity of the CSS. More importantly, the `style.css` consists of default styles which are not mine.

### Python Code Quality

I used Black to enforce formatting in my Python code, ensuring readability and consistency. Additionally, I ran the following command to check for any formatting issues:

```
for file in */models.py */views.py */admin.py */urls.py */apps.py; do
    autopep8 --diff "$file"
done
```

No issues were found.

---

## Conclusion

The conclusion for this project is very much one that is about me and the learning I am taking from this.
This project has been a pretty profound learning journey, characterized not just by the development of a web application but also by significant personal and professional growth. Looking back on the process, now, I'd say that they center round the critical importance of planning and also a willingness in asking for help when hitting a brick wall, rather than repeated smash into it until either breaking through or finally climbing over.

### The Impact of Insufficient Planning

The absence of a detailed plan at the project's inception led to numerous challenges. These ranged from features either creeping in due to not defining the structure, and getting so drawn into individual parts that I forgot to ensure certain aspects were present as I went forward.
This lack of foresight resulted in a development process that ran me, rather than me running it.

### The Impact of Not Reaching Out

Not reaching out has been a significant stumbling block and has cost me a great deal of time. Only upon stepping back from things, I've seen with far more clarity that sometimes overly analyzing something resulted in paralysis. Also, sometimes, the problems that I "thought" were an issue weren't actually mine to solve. I refer to the types of deprecation warnings and other error messages that led me down rabbit holes of troubleshooting, only to realize later that they were either unrelated to my project or could have been easily resolved with a simple update or configuration adjustment. These experiences have underscored the importance of seeking guidance and collaboration when facing challenges, as well as the need to differentiate between critical issues that require immediate attention and those that can be safely ignored or addressed at a later stage.

Despite the challenges and time-consuming detours caused by navigating through these issues, ultimately they've contributed to not just my growth but my actual skill development. Each rabbit hole I found myself in, broadened my skills in areas, parallel to what I was doing. So, whilst experiences may have prolonged project timelines in the short term, they have equipped me with a deeper understanding of software development and equipped me with problem-solving strategies that will undoubtedly hugely benefit me in future.
Navigating through this chaos, I gained valuable insights and a deeper understanding of software dependencies, version compatibility issues, and the importance of staying informed about evolving technologies, has been immeasurable.

---

## Further Development

Just Cakes is more the business name. The application's aim is to create and hold accounts with data that would enable the fully automated ordering and delivery of goods and services.
Services that would allow for a calendar bookings for:

- Booking for delivery
- Bookings for collection
- Bookings for taster days which would allow the customers to come and sample the types of cake that they would potentially be ordering.
- Payment features
- Instalment payment features.

Further to this, whilst currently, customers are able to communicate via the contact forms and telephone as to how they may want a one off cake designed, the addition of a user centric front end in which a customer would have a graphical interface from which they can design their own cakes, is planned.

---

## Deployment

This guide outlines the steps to deploy the Just Cakes Project on Heroku, set up ElephantSQL for database management, and Cloudinary for handling media files.

### Prerequisites

Before beginning the deployment process, ensure you have accounts and installations for the following services and platforms:

- **Heroku Account**: Platform to host your app.
- **ElephantSQL Account**: As your database.
- **Cloudinary Account**: To store your media files.
- **GitHub Account**: Which you'll use to clone the repo
- **Gitpod Account or Your Preferred IDE**: This guide uses Gitpod as the IDE.

### Deployment Guide

#### Setting Up on Heroku

1. **Create a Heroku App**: Follow the instructions to create a new app on Heroku. Choose a unique name for your Just Cakes version. Instructions can be found [here](https://dev.to/ivadyhabimana/3-creating-your-first-heroku-app-3d1d).

#### Cloning and Preparing the Repository

1. **Clone the Repository**: Clone the Just Cakes project repository from GitHub. Instructions for cloning are available [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
2. **Open in Gitpod**: Start your Gitpod environment (or your chosen IDE) and open the cloned repository.
3. **Install Dependencies**: Install the project dependencies by running `pip install -r requirements.txt` in the terminal.

#### Database Setup with ElephantSQL

1. **Create a Database Instance**: Navigate to [ElephantSQL's documentation](https://www.elephantsql.com/docs/index.html) and create a new PostgreSQL database instance. Follow the given instructions to set up the instance and obtain the connection URL.

#### Setting Up Cloudinary for Media Management

1. **Create a Cloudinary Account**: Go to [Cloudinary's integration guide](https://cloudinary.com/documentation/how_to_integrate_cloudinary#landingpage) to create an account and get your API keys for media management.

#### Integrating and Deploying to Heroku

1. **Configure Environment Variables**: Set up the necessary environment variables in your Heroku app settings. Include database URLs from ElephantSQL and API keys from Cloudinary.
2. **Deploy Your Application**: Link your GitHub repository to your Heroku app for automatic or manual deployment. Use the Heroku CLI to push your changes if preferred:
   - Log into Heroku CLI: `heroku login`
   - Link your repository: `heroku git:remote -a <your-heroku-app-name>`
   - Deploy your application: `git push heroku main`

#### Verifying Deployment

1. **Check Your Application**: Visit your Heroku app's URL to see the live Just Cakes site. Ensure that the database and media files are correctly linked and functioning.

### Troubleshooting

- **Deployment Errors**: Use `heroku logs --tail` in the terminal to check for any deployment errors.
- **Database Connection Issues**: Verify that the ElephantSQL URL is correctly set in the Heroku app's environment variables.
- **Media Files Not Loading**: Check that Cloudinary API keys are correctly configured in the environment variables.

For further assistance, you can refer to the documentation that is provided by Heroku, ElephantSQL, and Cloudinary, or consult their respective support forums where will find a wealth of experience amongst their membership.

---

## Copy / Improve / Contribute

If anyone wishes to copy and improve this software by contributing changes,
please do. You will find instructions from
[GitHub on how to do this.](https://docs.github.com/en/get-started/quickstart/contributing-to-projects#forking-a-repository)

---

### More work needed.

**Code should be implemented to guard against**
Performance speeds of loading need to be improved.

If anyone wishes to copy and improve this software by contributing changes,
please do. You will find instructions from
[GitHub](https://github.com/) on how to do this

---

## Credits, Acknowledgments and Appreciation.

- The reviews application within the just cakes project has been copied from the Code Institute walkthrough django project "codestar".

  **StackOverflow** for Regex patterns and how to implement them.
  Picture images have been courtesy of **Midjourney** and **Microsoft's Bing image-creator**. whilst the descriptions for the cakes were supplied by chatgpt, which I then tailored until it suited my own needs.

  **Picsart** and `Draw.io` for creating wireframes and flowcharts for my project.
  I have used **ChatGPT** as a tutor, fellow student and sounding board that had on tap, asking it to explain concepts I found hard to grasp, meanings of terms that are often taken as a given and also it's advice about structure of the project with a view to further development and also advice on completing aspects of this very README, in how I should go about things.
  However... Sometimes this has been to my detriment because it would get carried away in conversations about goals and routes to them, resulting in me having to scrub work and redo it.

  **Code Institute Tutors** for help when I reached out.

  **The favicon.ico** is courtesy of [Favicon Generator](https://favicon.io)
  https://websitemockupgenerator.com

- Code and the idea for toggling the DEBUG according to environment is courtesy of Code Institute learning materials

- The wallpaper for the site was sourced as a svg file courtesy of [Hero Patterns](https://heropatterns.com)

- **developer.mozilla.org** for handling responsive images

- **johnfraney.ca** for use of their responsive image generator

- **BrowserStack** for advising most common screen sizes

- **Blisk** for a comprehensive list of devices with accompanying information on Viewport Sizes, Screen Sizes and Device Pixel Ratio which enabled me to setup Emulated Devices in Chrome Devtools which was mega useful in testing the responsiveness.

### Acknowledgement of AI Assistance

Throughout the development of the _Just Cakes_ project, I utilized OpenAI's ChatGPT at various stages, serving as a versatile tool that helped me navigate different aspects of the project. From task prioritization to providing guidance on using third-party software, such as Draw.io for creating ERDs, ChatGPT was a valuable resource.

Often using ChatGPT as a sounding board, discussing the different parts of the application, their purposes, how they relate to one another, and the functionality required to achieve this.

Having already used Django's Generics package during lessons and walkthrough projects, I sought help from ChatGPT, who explained in better detail key attributes of various views within Generics, better enabling me to create the functionality for the apps I had envisaged

In addition, ChatGPT provided configuration assistance for setting up and using code formatting and linting extensions such as **Ruff**, **Black**, **Prettier**, and **ESLint**, wanting consistency across the project. In hindsight, I realised that this particular aspect of help sent me down a few rabbit holes which caused compatibility issues and I should have bee more selective as to how I went about using some extensions.

Finding it an invaluable tool, I used it to create end-of-day summaries that I would then use as a handover to myself, similar to how one might operate within a team. These summaries helped me reflect on the day’s progress and plan the next steps, ensuring continuity and maintaining focus on the project.

I believe that utilizing this tool has enhanced my understanding of the development process and contributed to maintaining a clear focus throughout the project. While ChatGPT was always available—offering advice, explanations and company, whether it be as a fellow student or extremely patient tutor, all final decisions and implementations were mine.
