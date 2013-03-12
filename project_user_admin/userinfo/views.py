# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from models import UserInfo
from forms import UserInfoForm

class UserInfoCreate(CreateView):
	form_class = UserInfoForm
	model = UserInfo
	template_name = "user_list.html"

class UserInfoUpdate(UpdateView):
	model = UserInfo

class UserInfoDelete(DeleteView):
	model = UserInfo
	success_url = reverse_lazy('index')