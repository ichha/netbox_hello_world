from netbox.plugins import PluginConfig

class NetBoxHelloConfig(PluginConfig):
    name = "netbox_hello"
    verbose_name = "NetBox Hello"
    description = "A simple hello-world plugin for NetBox"
    version = "0.1"

config = NetBoxHelloConfig
