from django.forms import ModelForm
from .models import Testimonial


class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = ('full_name', 'location', 'testimonial')
