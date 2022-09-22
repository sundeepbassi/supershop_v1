from django.db import models

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message_content = models.TextField()
    # Message sent date / time
    sent_on = models.DateTimeField(auto_now_add=True)
    # Have we responded to this message yet?
    responded = models.BooleanField(default=False)

    class Meta:
        """ Ordering contact messages by date order """
        ordering = ['-sent_on']
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        return "Message from " + str(self.email)
