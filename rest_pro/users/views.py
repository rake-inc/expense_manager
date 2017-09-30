from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.views import View
from django.utils.decorators import method_decorator
from .forms import SignupForm
# Create your views here.

class Home(View):
	template_name = 'home.html'

	def get(self, request):
		return render(request,self.template_name,{})

class UserSignup(View):
	template_name = 'signup.html'
	form_class = SignupForm

	def dispatch(self, *args, **kwargs):
		return super(UserSignup,self).dispatch(*args, **kwargs)

	def get(self,request):
		form = self.form_class
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/login/')

class AuthLogout(View):

	@method_decorator(login_required)
	def dispatch(self, request):
		return super(AuthLogout,self).dispatch(*args, **kwargs)

	def get(self, request):
		logout(request)
		return HttpResponseRedirect('/login/')