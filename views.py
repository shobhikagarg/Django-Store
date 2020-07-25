from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Stock
from .forms import StockCreateForm,StockSearchForm,UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from .forms import IssueForm, ReceiveForm



# Create your views here.
def home(request):
    queryset = Stock.objects.all()
    context={
        'form':'form'
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def list_item(request):
    title='List of items'
    form=StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    paginator=Paginator(queryset,10)
    page=request.GET.get('page')
    queryset=paginator.get_page(page)
    if request.method=='POST':
        queryset=Stock.objects.filter(category__icontains=form['category'].value(),item_name__icontains=form['item_name'].value())
    context = {
        'title': title,
        'queryset': queryset,
        'form': form,
    }
    return render(request, 'list_item.html', context)

def add_item(request):
    form=StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Item Added Successfully!")
        return redirect('/list_item')
    context = {
            'title': 'ADD items',
            'form':form,
        }
    return render(request,'add_item.html',context)

def delete_view(request,id):
    queryset= get_object_or_404(Stock, id=id)
    if request.method=='POST':
        queryset.delete()
        messages.info(request,"Item Deleted!!")
        return HttpResponseRedirect("/")
    context = {
    }
    return render(request, 'delete_view.html', context)

def stock_detail(request, id):
	queryset = Stock.objects.get(id=id)
	context = {
		"title": queryset.item_name,
		"queryset": queryset,
	}
	return render(request, "stock_detail.html", context)

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/list_item')
        else:
            messages.error(request,'Invalid credentials')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def issue_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
		instance.save()

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": 'Issue ' + str(queryset.item_name),
		"queryset": queryset,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}
	return render(request, "add_item.html", context)



def receive_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.receive_quantity
		instance.save()
		messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title": 'Reaceive ' + str(queryset.item_name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "add_item.html", context)
