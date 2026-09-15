from django.http import HttpResponse
from django.template import loader

from .models import Product


def index(request):
    # Load the template
    template = loader.get_template("core/index.html")
    products = Product.objects.order_by("price")
    context = {
        "product_data": products
    }
    return HttpResponse(template.render(context, request))


def product_detail(request, product_id):
    return HttpResponse(str(product_id))
