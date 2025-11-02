from django.views.generic import TemplateView

class HelloView(TemplateView):
    template_name = 'hello_world/hello.html'
