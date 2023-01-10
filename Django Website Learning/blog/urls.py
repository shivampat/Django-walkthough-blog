from django.urls import path, include 

from .views import show_blog_homepage, create_blogpost, get_year_month_blogposts, get_year_blogposts, get_individual_posts


urlpatterns = [
    path('', show_blog_homepage, name='view-homepage'),
    path('create_post', create_blogpost, name='create-post'),
    path('<int:blogYear>/', get_year_blogposts, name='get-year-month-blogposts'), 
    path('<int:blogYear>/<int:blogMonth>/', get_year_month_blogposts, name='get-year-month-blogposts'),
    path('<int:id>', get_individual_posts, name='get-id-blogposts'),  
    
]