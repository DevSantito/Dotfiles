#!/bin/sh

# Autostart script for Qtile

cmd_exist() { unalias "$1" >/dev/null 2>&1 ; command -v "$1" >/dev/null 2>&1 ;}
__kill() { kill -9 "$(pidof "$1")" >/dev/null 2>&1 ; }
__start() { sleep 1 && "$@" >/dev/null 2>&1 & }
__running() { pidof "$1" >/dev/null 2>&1 ;}

# Set the wallpaper using either feh or nitrogen

#if cmd_exist feh ; then
#    __kill feh
#    __start feh --bg-fill /home/justine/Pictures/Wallpapers/deer_art_vector_134088_3840x2160.jpg
#fi

if cmd_exist nitrogen ; then
    __kill nitrogen
    __start nitrogen --restore
fi

# Apps to autostart

if cmd_exist picom ; then
    __kill picom
    __start picom
fi

# Authentication dialog

if [ -f /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 ]; then
    __kill polkit-gnome-authentication-agent-1
    __start /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
fi

# Notification daemon

if cmd_exist dunst ; then
    __kill dunst
    __start dunst
fi

# Unclutter

if cmd_exist unclutter ; then
    __kill unclutter
    __start unclutter
fi

# Flameshot

if cmd_exist flameshot ; then
    __kill flameshot
    __start flameshot
fi


#  Xrandr config
xrandr --output HDMI-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP-0 --off --output DP-1 --off --output DP-2 --off --output DP-3 --mode 1920x1080 --pos 1920x176 --rotate normal --output DP-4 --off --output DP-5 --off




