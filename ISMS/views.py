from django.contrib import messages
from django.shortcuts import render , Http404 , redirect
from . forms import *
# Create your views here.

def home(request):
    return render(request , 'ISMS/isms_dashboard.html')


def category_dashboard(request):

    category_list = Category.objects.all()

    context = {
        'category_list' : category_list,
    }

    return render(request , 'ISMS/inventory/category_dashboard.html' , context)


def new_category(request):

    createForm = CategoryForm()

    context = {
        'category_form' : createForm
    }

    if request.method == 'POST':

        createForm_request = CategoryForm(request.POST , request.FILES)

        if(createForm_request.is_valid()):
            createForm_request.save()
            messages.success(request, 'Category created success !')
        else:
            createForm_request.errors
            context['category_form'] = createForm_request

    return render(request , 'ISMS/inventory/add_new_category.html' , context)


def view_category(request , id):

    context = {}

    try:
        category = Category.objects.get(id = id)
        context['category'] = category
    except:
        messages.warning(request , 'Category Not Fount !')

    return render(request , 'ISMS/inventory/view_category.html' , context)


def update_category(request , id):

    context = {}

    try:
        category = Category.objects.get(id = id)
        category_update_form = CategoryForm(instance=category)
        context['category_form'] =  category_update_form
        context['category'] = category.name
    except:
        messages.warning(request , 'Category Not Fount !')


    # handel post requests
    if request.method == 'POST':
        updateForm_request = CategoryForm(request.POST , request.FILES , instance=category)

        if updateForm_request.is_valid():
            updated_category = updateForm_request.save()
            category_update_form = CategoryForm(instance=updated_category)
            context['category_form'] = category_update_form
            context['category'] = updated_category.name
            messages.success(request, 'Category update success !')
        else:
            updateForm_request.errors
            context['category_form'] = updateForm_request


    return render(request , 'ISMS/inventory/update_category.html' , context)


def item_dashboard(request):

    items = Item.objects.all()

    context = {
        'items' : items
    }

    return render(request , 'ISMS/inventory/item_dashboard.html' , context)

def new_item(request):

    item_form = ItemForm(prefix='itemForm');

    suppliers = Supplier.objects.all()

    context = {
        'item_form' : item_form,
        'suppliers' : suppliers
    }

    if request.method == 'POST':
        item_request_form = ItemForm(request.POST , prefix='itemForm')
        if(item_request_form.is_valid()):
            item = item_request_form.save()
            allocated = request.POST.getlist('allocated')
            supplier_list = []
            for allocate in allocated:
                supplier_list.append(int(allocate))

            item.suppliers.add(*supplier_list)
            item.save()
            messages.success(request, 'Item Create success !')
        else:
            context['item_form'] = item_request_form

    return render(request , 'ISMS/inventory/new_item.html' , context)