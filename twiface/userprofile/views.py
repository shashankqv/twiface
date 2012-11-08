from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

def create_background(request):
    return render_to_response("customize.html",
            context_instance=RequestContext(request))

