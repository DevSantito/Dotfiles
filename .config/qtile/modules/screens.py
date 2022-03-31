from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import subprocess
import os

def init_widgets_list():
    widgets_list = [                    
                widget.GroupBox(
                    **base(),
                    fontsize=18,
                    padding=7,
                    disable_drag=True,
                    rounded=True,
                    active=colors["chalky"],
                    inactive=colors["malibu"],
                    highlight_method='text',
                    block_highlight_text_color=colors["violet"],
                    this_current_screen_border=colors["sage"],
                    this_screen_border=colors["sage"],
                    urgent_alert_method='text',
                    urgent_border=colors["error"],
                    other_current_screen_border=colors["sage"],
                    other_screen_border=colors["sage"]
                ),
                
                widget.Systray(
                    **base(),
                    padding=10,
                ),  

                widget.Spacer(**base()),

                widget.WindowName(
                    **base(fg="malibu"),
                    width=bar.CALCULATED,
                    empty_group_string="Desktop",
                    fontsize=14,
                    max_chars=45,
                    fmt='{}'
                ),

                widget.Spacer(**base()),

                separator(),

                widget.GenPollText(
                    **base(fg="violet"),
                    func=lambda: subprocess.check_output(["upower"], encoding="utf-8"),
                    update_interval=1,
                ),

                separator(),

                widget.Volume(
                    **base(fg="violet"),
                    fmt = ': {}',
                    update_interval=1,
                ),

                separator(),

                widget.Clock(
                    **base(fg="whiskey"),
                    format = "%A, %B %d - %H:%M "
                ),

                separator(),
        ]
    return widgets_list

def init_widgets_secondary():
    widgets_secondary = init_widgets_list()
    del widgets_secondary[9:10]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_secondary

def init_widgets_main():
    widgets_main = init_widgets_list()
    return widgets_main                # Monitor 2 will display all widgets in widgets_list


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_main(), opacity=1.0, size=30))]

screens = init_screens()