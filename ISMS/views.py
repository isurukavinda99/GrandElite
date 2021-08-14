from django.contrib import messages
from django.db.models import Case, When
from django.shortcuts import render , Http404 , redirect , get_object_or_404
from  django.db import transaction
from . forms import *
# Create your views here.

def home(request):

    context = {}

    context['total_category'] = Category.objects.count()
    context['total_items'] = Item.objects.count()
    context['total_supplers'] = Supplier.objects.count()

    lowCountObj = Item.objects.annotate()

    return render(request , 'ISMS/isms_dashboard.html' , context)


def category_dashboard(request):

    category_list = Category.objects.all()

    context = {
        'category_list' : category_list,
    }

    #handal search requests
    if request.method == 'POST':

        search_key = request.POST.get('search_key')

        try:
            category_list = Category.objects.filter(name = search_key)

            if not category_list:
                category_list = Category.objects.filter(id=int(search_key))

            if not category_list:
                messages.warning(request, 'Search key does not match with any entry')

            context['category_list'] = category_list

        except:
            messages.warning(request, 'Search key does not match with any entry')


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


def view_item(request , id):

    context = {}
    try:
        item = Item.objects.get(id=id)
        itemForm = ItemForm(instance=item)
        for field in itemForm.fields:
            itemForm.fields[field].disabled = True
        context['item_form'] = itemForm
        context['item_name'] = item.name
        context['suppler_list'] = item.suppliers.all()
        context['item_id'] = item.id
    except:
        messages.warning(request, 'Item Not Found !')

    return render(request , 'ISMS/inventory/view_item.html' ,context)

def update_item(request , id):
    context = {}
    try:
        item = Item.objects.get(id=id)
        itemForm = ItemForm(instance=item , prefix='item_update_form')
        context['item_form'] = itemForm
        context['item_name'] = item.name
        context['suppler_list'] = item.suppliers.all()

        allocated_list = item.suppliers.all()

        unallocated_list = Supplier.objects.exclude(id__in= item.suppliers.all())
        context['unallocated_list'] = unallocated_list
        context['item_id'] = item.id
    except:
        messages.warning(request, 'Item Not Found !')


    #handla update post request
    if request.method == 'POST':
        item_request_from = ItemForm(request.POST, prefix='item_update_form' , instance=item)

        if item_request_from.is_valid():

            try:
                with transaction.atomic():

                    item_update = item_request_from.save()
                    allocated = request.POST.getlist('allocated')
                    supplier_list = []
                    for allocate in allocated:
                        supplier_list.append(int(allocate))

                    item_update.suppliers.clear()
                    item_update.suppliers.add(*supplier_list)
                    item_update.save()
                    context['item_form'] = ItemForm(instance=item_update, prefix='item_update_form')
                    context['item_name'] = item_update.name
                    messages.success(request, 'Item Update Success!')
            except:
                messages.warning(request, 'Item Update Unsuccess!')
        else:
            context['item_form'] = item_request_from

    return render(request , 'ISMS/inventory/update_item.html' , context)


def delete_item(request , id):

    item = Item.objects.filter(id=id)

    item.delete()

    return redirect('item_dashboard')



