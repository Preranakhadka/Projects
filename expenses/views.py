from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense

@login_required
def home(request):
	context = {}
	expenditure = request.user.expense_set.all()
	context['expenditure'] = expenditure
	return render(request, 'expenses/index_expenses.html', context)

@login_required
def new_expenses(request):
	if request.method == 'POST':
		price = request.POST['price']
		category = request.POST['category']
		user = request.user
		items = request.POST['items']
		Expense(price=price, category=category, user=user, items=items).save()
	return redirect('/expenses')

# Create your views here.
