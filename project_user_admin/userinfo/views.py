# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils import timezone
from models import UserInfo
from forms import UserInfoForm

class UserInfoList(ListView):
	model = UserInfo
	template_name="user_list.html"

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get context data 
		context = super(UserInfoList, self).get_context_data(**kwargs)
		# Add your own context
		context['extra'] = 'Extra data'
		return context

class UserInfoDetail(DetailView):

	def get_object(self):
		# Call the superclass
		obj = super(UserInfoDetail, self).get_object()
		# Record the last accessed date
		obj.last_accessed = timezone.now()
		obj.save()
		# Return the object
		return obj


class UserInfoCreate(CreateView):
	form_class = UserInfoForm
	model = UserInfo
	template_name = "user_create.html"

	def form_valid(self, form):
		"""The base implementation of 'form_valid' will call the 'f.save()' function.
		So, add your additional opt here
		"""
		form.instance.now = timezone.now
		return super(AuthorCreate, self).form_valid(form)

class UserInfoUpdate(UpdateView):
	model = UserInfo
	template_name = "user_edit.html"

class UserInfoDelete(DeleteView):
	model = UserInfo
	template_name = "user_delete_confirm.html"
	success_url = reverse_lazy('index')

class GreetingView(View):
	greeting = "Hello World!"

	def get(self, request):
		return HttpResponse(self.greeting)