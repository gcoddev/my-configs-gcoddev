#!/bin/sh

# Fondo de pantalla
feh --bg-fill /usr/share/backgrounds/archWallpapers/arch1.jpg &
# Iconos del sistema
notify-send "Bienvenido de nuevo Gary" &
udiskie -t &
nm-applet &
volumeicon &
cbatticon -u 5 &
picom --config ~/.config/picom/picom.conf  &
