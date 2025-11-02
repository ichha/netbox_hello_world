from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:hello_world:hello",          # URL name defined in urls.py
        link_text="Hello World",
        buttons=(
            PluginMenuButton(
                link="plugins:hello_world:hello",
                title="Say hello",
                icon_class="mdi mdi-hand-wave",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
)