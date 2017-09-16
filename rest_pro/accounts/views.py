from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import ExpenseForm
from .models import Expense
# Create your views here.

@login_required
def profile(request):
    return render(request,'profile.html',{})

@login_required
def add_details(request):
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
    return render(request,'add_details.html',{})
