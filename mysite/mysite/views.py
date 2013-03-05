from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response
import datetime, os

def current_datetime( request ):
	now = datetime.datetime.now()
	date
	html = "<html><body>It is now %s.</body></html>" % now
	# html = "<html><body>It is now %s.</body></html>" % os.getcwd()
	return HttpResponse(html)

def current_datetime_temp(request):
	now = datetime.datetime.now()
	return HttpResponse(render_to_response('base_curtime.html', {"now" : now}))

def hours_ahead(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), It will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def hours_ahead_temp(request, offset):
	offset = int(offset)
	now = datetime.datetime.now() + datetime.timedelta(hours=offset)

	## method 0
	# fp = open("./mysite/templates/mytemplate.html")
	# template = Template(fp.read())
	# fp.close()
	# html = template.render(Context({"offset" : offset, "now" : now}))
	# return HttpResponse(html)

	## method 1
	# template = get_template("mytemplate.html")
	# html = template.render(Context({"offset" : offset, "now" : now}))
	# return HttpResponse(html)

	## method 2
	# return HttpResponse(render_to_response("mytemplate.html", {"offset" : offset, "now" : now}))

	## method 3
	return HttpResponse(render_to_response("mytemplate.html", locals()))

