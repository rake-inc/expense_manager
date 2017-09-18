from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ExpenseForm
from .models import Expense


# Create your views here.

@login_required
def profile(request):
    return render(request, 'profile.html', {})


@login_required
def add_details(request):
    print (request.user.id)
    form = ExpenseForm(initial={'user': request.user.id})
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/accounts/profile')
    return render(request, 'add_details.html', {'form': form})


@csrf_exempt
def profile_api(request):
    print(request.method)
    if request.method == 'POST':
        print(request.body)
        id_ = request.body.decode('utf-8')
        print(id_)
        data = Expense.objects.filter(user_id=int(id_)).values()
        print(data)
        return JsonResponse({'table_data':list(data)}, safe=False)
    return HttpResponse("called")
