from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from django.utils.translation import ugettext, ugettext_lazy as _

from forms import PostForm

class PostView(View):
    
    # Allowed methods on the view
    http_method_names = [u'post', u'get']

    template_name = '_new_post_form.html'
    form = PostForm

    context = {
        'form': form,
        'title': 'Post Form',
    }

    def get(self, request):

        response = render(request, self.template_name, self.context) 
    
        return response

    def post(self, request):
        try: 
            form = self.form(data=request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, _('New post created'))
            else:
                self.context['form'] = form
            response = render(request, self.template_name, self.context)
        except Exception as e:
            response = HttpResponse(str(e))

        return response
