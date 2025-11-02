from netbox.plugins import PluginConfig

class HelloWorldConfig(PluginConfig):
    name = "hello_world"
    verbose_name = "Hello World"
    description = "A simple Hello World plugin for NetBox"
    author = "Your Name"
    author_email = "you@example.com"
    base_url = "hello-world"
    min_version = "4.0.0"
    required_settings = []
    default_settings = {}

config = HelloWorldConfig
