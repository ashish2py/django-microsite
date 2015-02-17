#########################################
# A Pythonic Django Microsite example
# Inspired by Flask and Bottle framework
#########################################


import sys
from django.conf import settings

settings.configure(
	DEBUG=True,
	SECRET_KEU='secretkeygoeshere',
	ROOT_URLCONF = __name__,
	MIDDLEWARE_CLASSES = (
	    'django.middleware.common.CommonMiddleware',
	    'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
	),
)

from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	return HttpResponse("Hey see this! It's working.")

urlpatterns = (	
	url(r'^$', index,name="index_page"),
)

if __name__ == "__main__":
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)

