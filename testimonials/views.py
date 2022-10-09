""" Views for testimonials """
from django.shortcuts import render

from .forms import TestimonialForm

from .models import Testimonial


def display_testimonial_form(request):
    """ Display testimonial form """
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'testimonials/success.html')
    form = TestimonialForm()
    context = {'form': form,
               'extra_title': str('Submit Testimonial')}
    return render(request, 'testimonials/submit_testimonial.html', context)


def display_all_testimonials(request):
    """ Display all testimonials """
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
        'extra_title': str('Testimonials'),
    }

    return render(request, 'testimonials/display_testimonials.html', context)
