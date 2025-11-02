from django.views.generic import TemplateView
from extras.plugins import PluginTemplateExtension


class HelloView(TemplateView):
    template_name = "hello_world/hello.html"


# Optional: expose the view as a plugin template extension (not required for a page)
class HelloWorldExtension(PluginTemplateExtension):
    model = "dcim.device"

    def right_page(self):
        return """
        <div class="panel panel-default">
            <div class="panel-heading"><strong>Hello World</strong></div>
            <div class="panel-body">
                <a href="{% url 'plugins:hello_world:hello' %}" class="btn btn-primary">
                    Go to Hello page
                </a>
            </div>
        </div>
        """

# Uncomment the line below if you want the extension to appear on device detail pages
# template_extensions = [HelloWorldExtension]
