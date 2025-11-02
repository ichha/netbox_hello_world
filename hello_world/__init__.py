from netbox.plugins import PluginConfig
version = __version__
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


# This is REQUIRED — NetBox looks for this exact name
config = HelloWorldConfig
