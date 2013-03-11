from django.db import models
from django.contrib import admin

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	def __repr__(self):
		return '%s' % (self.name)

	class Meta:
		ordering = ["name"]


class Author(models.Model):
	salutation = models.CharField(max_length=10)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	headshot = models.ImageField(upload_to="./books/tmp")

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('salutation', 'first_name', 'last_name')
	# list_filter = ('first_name', 'last_name')
	# ordering = ('-salutation',)
	# search_fields = ('salutation',)


class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()

	def __str__(self):
		return self.title

admin.site.register([Publisher, Book])
admin.site.register(Author, AuthorAdmin)

