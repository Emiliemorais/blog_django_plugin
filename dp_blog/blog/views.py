from django.shortcuts import render
from django.views.generic import View

class PostView(View):
    
    # Allowed methods on the view
    http_method_names = [u'get', u'post']

    def get(self, request):
    	return render(request, "test.html", {"ola": "ola"})

    def post(self, request):
    	pass
