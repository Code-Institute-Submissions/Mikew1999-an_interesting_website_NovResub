# An interesting website

<!-- Slideshow from w3 schools -->

View live project here https://an-interesting-website.herokuapp.com/

This is a shop website which sells products made by the company and allows users to list their own products for sale.

It is designed to enable the shopper to find a product they like easily by providing a search form and various ways to filter the results.

# Data schema



## User Experience (UX)

## User stories

1) ### First time visitors goals:
    1) As a first time visitor, I would like to easily understand the purpose of the website.
    2) I would like to browse the list of available products to understand if this is the site for me.
    3) I would like to see the most popular products.
    4) I would like the option to order a product without needing to create an account.

2) ### Shoppers goals
    1) As a shopper, I would like to effortlessly browse through the list of available products.
    2) I would like to be able to filter the products based on certain criteria, such as price and category of product.
    3) I would like the ability to make a review about a product and see other users reviews for that product.
    4) I would like to like a product / add a product to my favourites.
    5) I would like to be able to browse my past orders.
    6) I would like the ability to be able to get in touch with the company easily via a form, should there be any problems with my order.
    7) I would like to browse products listed by a specific user.
    8) I would like to be able to search for a specific product through a convenient search form.

3) ### Business owner / Sellers goals:
    1) As a seller, I would like to be able to list a product for sale.
    2) I would like to be notifed when someone buys my product.
    3) I would like to receive the address and contact details of the customer who has bought my product.


# Design

### Colour scheme

The background colour is white on all pages with many pictures to brighten up the page.
The Shopping bag page has a slightly gray background to make the boxes pop out more.
The buttons are mainly blue and green to ensure they are visible to make the site more intuitive to navigate.

### Typography

I have mainly used Oswald and Montserrat for my fonts as I feel that they provide the site with a professional look but also doesn't look too dated.

### Imagery

I have mainly used imagery from https://fakestoreapi.com/ for the products and product images as they are visually appealing to showcase the marketplace. 
The site allows the users to view pictures of the products so they can quickly find what they are looking for.

# Wireframes


# Features

# Technologies Used

## Frameworks & libraries used

Django

Bootstrap

Jquery

## Languages used

HTML5

CSS3

Javascript

Python 3

# Testing 

## Further testing

## Known bugs

When using multiple monitors the width and height of objects becomes altered.

# Deployment

## To run the server locally

1) Open up environment
2) In the terminal type: 'pip3 install -r requirements.txt'
    This will install all of the required libraries for the project
3) In the terminal type: 'python3 manage.py runserver'
4) Select open browser next to port 8000

## To Deploy

1) Freeze requirements into requirements.txt file: pip3 freeze > requirements.txt
2) Create Procfile at the root of the repository and type 'web: gunicorn an_interesting_site.wsgi:application'.
3) Login to Heroku
4) 

# Credits

https://fakestoreapi.com/ for the products and images to base my site around.