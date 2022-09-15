from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.db.models.functions import Lower

from django.views.generic.edit import UpdateView, DeleteView


# from django.views import generic
# from django.views.generic.list import ListView

# from django.contrib.auth.models import Group

from .models import Product, Category, ProductReview
from .forms import ProductForm, ProductReviewForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) |\
                Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    # A view to show individual product details

    product = get_object_or_404(Product, pk=product_id)
    if request.user:
        if request.method == 'POST':
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                product_review = form.save(commit=False)
                product_review.author = request.user
                product_review.product = product
                product_review.save()
                return redirect(reverse('product_detail', args=[product.id]))
        else:
            form = ProductReviewForm()
    context = {
        'product': product,
        'product_review_form': form,
    }

    return render(
        request, 'products/product_detail.html', context
        )


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template_name = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template_name, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, ('Failed to update product. '
                                     'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template_name = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template_name, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


class UpdateProductReview(SuccessMessageMixin, UpdateView):
    # Update a product review
    model = ProductReview
    template_name = 'update_product_review.html'
    success_message = "Your protuct review was successfully updated."
    fields = ['body']

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


class DeleteProductReview(DeleteView):
    # Delete a product review
    model = ProductReview
    template_name = 'delete_product_review.html'
    success_message = "Your product review was successfully deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteProductReview,
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
