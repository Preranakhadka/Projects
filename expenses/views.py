from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense


# Create your views here.

@login_required
def home(request):
	expenditure = Expense.objects.all()
	context={"expenditure": expenditure}
	return render(request, 'expenses/index_expenses.html', context)

@login_required
def new_expenses(request):
	if request.method == 'POST':
		price = request.POST['price']
		category = request.POST['category']
		user = request.user
		items = request.POST['items']
		Expense(price=price, category=category, user=user, items=items).save()
	return redirect('/expenses/')


def edit_expenses(request):
	post=get_object_or_404(POST,Expense)
	if request.method=="POST":
		price = price(request.POST,instance=post)
		category = category(request.POST,instance=post)
		user = request.user
		items = items(request.POST,instance=post)
		Expense(price=price, category=category, user=user, items=items).save()
	return redirect('/expenses/')
	else:
		expenditure=expenditure(instance=post)
		expenses='expenses/index_expenses.html'
		context={expenditure:expenditure}
		return render (request,expenses,context)

		

def delete_expenses(request):
	post=get_object_or_404(POST,Expense)
	if request.method=="POST":
		price = price(request.POST,instance=post)
		category = category(request.POST,instance=post)
		user = request.user
		items = items(request.POST,instance=post)
		Expense(price=price, category=category, user=user, items=items).save()
	return redirect('/expenses/')
	else:
		expenditure=expenditure(instance=post)
		expenses='expenses/index_expenses.html'
		context={expenditure:expenditure}
		return render (request,expenses,context)
   
#    






