#!/bin/sh

# Fondo de pantalla
feh --bg-fill --randomize /usr/share/backgrounds/archWallpapers/* &
# Iconos del sistema
udiskie -t &
nm-applet &
volumeicon &
cbatticon -u 5 &
picom --config ~/.config/picom/picom.conf  &
