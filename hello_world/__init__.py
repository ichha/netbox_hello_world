from netbox.plugins import PluginConfig
import os

__version__ = "0.1.0"

class HelloWorldConfig(PluginConfig):
    name = "hello_world"
    verbose_name = "Hello World"
    description = "A simple Hello World plugin for NetBox"
    version = __version__
    author = "Your Name"
    author_email = "you@example.com"
    base_url = "hello-world"
    min_version = "4.0.0"
    required_settings = []
    default_settings = {}

template_dir = os.path.join(os.path.dirname(__file__), "templates")
config = HelloWorldConfig
