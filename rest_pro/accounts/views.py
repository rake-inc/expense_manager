from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.utils import timezone
from .forms import ExpenseForm
from .models import Expense
from .serializers import ExpenseSerializer


# Create your views here.

class ProfileView(View):
    template_name = 'profile.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)
    
    def get(self,request):
        print(self.template_name)
        return render(request,self.template_name,{})



class AddDetails(View):
    form_class = ExpenseForm
    template_name = 'add_details.html'


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddDetails,self).dispatch(*args, **kwargs)
    
    def get(self,request):
        form = self.form_class(initial={'user': request.user.id})
        return render(request, self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/profile')

class ModelView(ListView):
    model = Expense
    template_name = 'expense_list.html'


    def get_queryset(self):
        print(dir(self))
        return Expense.objects.filter(user_id = self.request.user.id)

class ProfileApi(APIView):

    def dispatch(self, *args, **kwargs):
        return super(ProfileApi, self).dispatch(*args, **kwargs)
    
    def get(self,request,format='json'):
        obj = Expense.objects.filter(user_id=request.user.id)
        serializer=ExpenseSerializer(obj,many=True)
        return Response(serializer.data)