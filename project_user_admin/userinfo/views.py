# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from models import UserInfo
from forms import UserInfoForm

class UserInfoList(ListView):
	model = UserInfo
	template_name="user_list.html"

class UserInfoCreate(CreateView):
	form_class = UserInfoForm
	model = UserInfo
	template_name = "user_create.html"

class UserInfoUpdate(UpdateView):
	model = UserInfo
	template_name = "user_edit.html"

class UserInfoDelete(DeleteView):
	model = UserInfo
	template_name = "user_delete_confirm.html"
	success_url = reverse_lazy('index')