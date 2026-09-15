from django.http import HttpResponse
from django.template import loader

from .models import Product


def index(request):
    # Load the template
    template = loader.get_template("core/index.html")
    products = Product.objects.all()
    context = {
        "product_data": products
    }
    return HttpResponse(template.render(context, request))


def product_detail(request, product_id):
    p = Product.objects.get(id=product_id)
    return HttpResponse(str(p.name))
