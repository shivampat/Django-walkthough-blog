from .models import BlogPost

def getYears():
    queryset = BlogPost.objects.all()
    years = []
    for blogpost in queryset: 
        if blogpost.blogYear not in years:
            years.append(blogpost.blogYear)
    return years