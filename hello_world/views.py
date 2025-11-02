# hello_world/views.py
from django.views.generic import TemplateView
from django.template.response import TemplateResponse

class HelloView(TemplateView):
    def get(self, request, *args, **kwargs):
        html = """
        {% extends "base.html" %}
        {% block content %}
            <div class="container mt-5">
                <h1 class="text-success">Inline Success! 🎉</h1>
                <p>View is routing. Templates next.</p>
                <p>URL: {{ request.path }}</p>
            </div>
        {% endblock %}
        """
        return TemplateResponse(request, html)
