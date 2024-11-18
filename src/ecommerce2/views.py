from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ProductModel
from .forms import ProductModelForm
from django.db.models import Q



# Create your views here.
def product_model_delete_view(request, product_id):
    instance = get_object_or_404(ProductModel, id=product_id)
    if request.method == "POST":
        instance.delete()
        HttpResponseRedirect("/ecommerce2/")
        messages.success(request, "Producto eliminado con éxito")
        return HttpResponseRedirect("/ecommerce2/")
    context = {
        "product": instance
    }
    template = "ecommerce2/delete-view.html"
    return render(request, template, context)

def product_model_update_view(request, product_id=None):
    instance = get_object_or_404(ProductModel, id=product_id)
    form = ProductModelForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Producto actualizado con éxito")
        return HttpResponseRedirect("/ecommerce2/{product_id}".format(product_id=instance.id))
    context = {
        "form": form
    }
    template = "ecommerce2/update-view.html"
    return render(request, template, context)

def product_model_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Producto creado con éxito")
        return HttpResponseRedirect("/ecommerce2/{product_id}".format(product_id=instance.id))
    context = {
        "form": form
    }
    template = "ecommerce2/create-view.html"
    return render(request, template, context)

def product_model_detail_view(request, product_id):
    instance = get_object_or_404(ProductModel, id=product_id)
    context = {
        "product": instance
    }
    template = "ecommerce2/detail-view.html"
    return render(request, template, context)

#@login_required
def product_model_view_list(request):
    query = request.GET.get("q", None)
    queryset = ProductModel.objects.all()
    if query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(price__icontains=query)

        )
    print(queryset)
    template = "ecommerce2/list-view.html"
    context = {
        "products": queryset
    }

    if request.user.is_authenticated:
        template = "ecommerce2/list-view.html"
    else:
        template = "ecommerce2/list-view.html"

    return render(request, template, context)

@login_required
def login_required_required_view(request):
    queryset = ProductModel.objects.all()
    print(queryset)
    template = "ecommerce2/list-view.html"
    context = {
        "products": queryset
    }

    if request.user.is_authenticated:
        template = "ecommerce2/list-view.html"
    else:
        template = "ecommerce2/list-view.html"

    return render(request, template, context)
