from libqtile import widget
from libqtile import qtile
import json
import os

with open("{}/.config/qtile/colors.json".format(os.getenv("HOME"))) as file:
    colors_json = json.load(file)

colors = colors_json


widget_defaults = dict(
    font='mononoki Nerd Font Bold',
    fontsize=18,
    padding=1,
)

extension_defaults = widget_defaults.copy()

def base(fg="ivory", bg="stone"):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=14, size_percent=40)

