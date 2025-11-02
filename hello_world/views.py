from django.shortcuts import render
from django.views.generic import TemplateView

class HelloView(TemplateView):
    def get(self, request):
        return render(request, 'hello_world/hello.html', {
            'title': 'My Simple Plugin Page',
            'message': 'Hello from the NetBox plugin!'
        })
