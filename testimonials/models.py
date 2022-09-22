from django.db import models

# Create your models here.


class Testimonial(models.Model):
    full_name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    testimonial = models.TextField()
    display_on_website = models.BooleanField(default=False)
    # Testimonial sent date / time
    sent_on = models.DateTimeField(auto_now_add=True)
    # Have we processed this testimonial yet?
    processed = models.BooleanField(default=False)

    def __str__(self):
        return "Testimonial by " + str(self.full_name) + " from " + str(self.location)
