from django.shortcuts import render

# Create your views here.


# Home page
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


# About Us page
def about_us(request):
    """ A view to return the index page """

    return render(request, 'home/about-us.html')

        'extra_title': str('Testimonials'),