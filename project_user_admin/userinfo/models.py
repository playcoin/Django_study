from django.db import models

# Create your models here.
class UserInfo(models.Model):

	username = models.CharField(max_length=254, unique=True)
	password = models.CharField(max_length=254)
	name = models.CharField(max_length=254, help_text='Your actural name!!')
	email = models.EmailField(max_length=254)
	birthday = models.DateField()
	identity = models.PositiveIntegerField()

	class Meta:
		db_table = "userinfo"
		verbose_name = 'UserInfo'
		verbose_name_plural = 'UserInfos'

	def __unicode__(self):
		return "%s(%s)" % (self.username, self.name)

	def get_absolute_url(self):
		return "/"