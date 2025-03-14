Instagram Clone with Web Scraper – A Django Project

Overview :
    This project is a social media web application inspired by Instagram, with additional features such as a built-in web scraper for fetching images from Flickr. Users can create posts that include an image, audio, text, and category tags. The application allows for interaction through likes, comments, and replies, all without requiring custom JavaScript.

Key Features:
Home Page (Stream of Posts):
    Displays posts created by users, containing:
    Image (uploaded or scraped from Flickr)
    Audio
    Text (Caption)
    Category Tags (predefined set for filtering)

Web Scraper Integration:
    A custom web scraper is built to fetch images from Flickr, allowing users to:
        Select an image
        Add a personal caption
        Categorize the post using predefined tags

Post Interactions:
    Comments & Replies:
        Users can comment on posts and reply to comments

    Likes System:
        Users can like posts, comments, and replies
        Works without page refresh (achieved using Django's asynchronous capabilities)

Sidebar – Trending Insights:
    Displays the most popular posts and comments, providing users with trending content

User Profile Section:
    Users can manage their profiles by adding:
        Profile Image
        Bio

Profile page displays:
    Most Recent Posts
    Top Posts
    Top Comments
    Liked Posts

Technology Stack:
    Backend: Django (Django REST Framework for APIs)
    Database: MySQL or PostgreSQL
    Frontend: Django Templates (no custom JavaScript)
    Web Scraper: BeautifulSoup/Scrapy for Flickr image scraping

# How to Setup
1. Clone Project
```
git clone https://github.com/sunil-kunkekar/K_Brothers.git
```

2. Go To Project Directory
```
cd Awesome
```
3. Create Virtual Environment
```
python3 -m venv venv
```
4. Active Virtual Environment
```
source venv/bin/activate
```
5. Install Requirements File
```
pip install -r requirements.txt
```
6. Migrate Database
```
python manage.py migrate
```
7. Create Super User
```
python manage.py createsuperuser
```
8. Run Project
```
python manage.py runserver
```
