""" Views for product reviews """

from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.edit import UpdateView, DeleteView

from .models import ProductReview
from .forms import ProductReviewForm

# Create your views here.


def get_approved_product_reviews(product_id):
    """ Get all the approved product reviews for a given product (id) """
    return ProductReview.objects.filter(product=product_id, approved=True)


def write_product_review(request):
    """ Functionality for user to write a product review """

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductReviewForm()

    context = {
        'product_review_form': form,
    }

    return render(
        request, 'product-review-form.html', context
    )


class update_product_review(SuccessMessageMixin, UpdateView):
    """ Update a product review """
    model = ProductReview
    template_name = 'update_product_review.html'
    success_message = "Your product review was successfully updated."
    context_object_name = 'product_review'
    fields = ['title', 'review']

    # After updating a product review, go to the url specified in this
    # function.
    #
    # Note that this URL, is the page on which we clicked the Edit link,
    # this makes more sense to the user, i.e. they edit (update) a product
    # review on a page then return to that same page, to see the product
    # review updated.
    def get_success_url(self):
        next_url = self.request.GET['nexturl']
        return next_url


class delete_product_review(DeleteView):
    """ Delete a product review """
    model = ProductReview
    template_name = 'delete_product_review.html'
    success_message = "Your product review was successfully deleted."
    context_object_name = 'product_review'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(delete_product_review,
                     self).delete(request, *args, **kwargs)

    # After deleting a product review, go to the url specified in this
    # function.
    #
    # Note that this URL, is the page on which we clicked the Delete link,
    # this makes more sense to the user, i.e. they delete a product review
    # on a page then return to that same page, to see the product review
    # deleted.
    def get_success_url(self):
        next_url = self.request.GET['nexturl']
        return next_url
