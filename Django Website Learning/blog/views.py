from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import BlogpostForm
from .models import BlogPost
from datetime import datetime
from .menubar import getYears

# Create your views here.
def show_blog_homepage(request):
    all_blogposts = BlogPost.objects.all()
    content = {
        'blogposts': all_blogposts,
        'menubar_years': getYears()

    }
    return render(request, 'blog/blog_home.html', content)

def create_blogpost(request):
    form = BlogpostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/blog')
    date = datetime.now()
    content = {
        'form': form,
        'accessTime': date,
        'menubar_years': getYears()
    }

    return render(request, 'blog/createpost.html', content)

def get_year_blogposts(request, blogYear):
    blog_post = BlogPost.objects.filter(blogYear=blogYear)
    print(blog_post)
    content = {
        'blogposts': blog_post,
        'menubar_years': getYears(),
        'year': blogYear,
    }
    return render(request, 'blog/blog_year.html', content)

def get_year_month_blogposts(request, blogYear, blogMonth):
    blog_post = BlogPost.objects.filter(blogYear=blogYear, blogMonth=blogMonth)
    months = ['', 'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December']
    content = {
        'blogposts': blog_post,
        'menubar_years': getYears(),
        'year': blogYear,
        'month': months[blogMonth],
    }
    return render(request, 'blog/blog_year_month.html', content)

def get_individual_posts(request, id):
    blog_post = BlogPost.objects.get(id=id)
    content = {
        'blogpost': blog_post,
        'menubar_years': getYears(), 
    }
    return render(request, 'blog/blog_id.html', content)
