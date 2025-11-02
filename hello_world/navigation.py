from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_hello:hello",  # URL name from urls.py
        link_text="Hello Page",             # Text that appears
        buttons=(),                         # optional
    ),
)
