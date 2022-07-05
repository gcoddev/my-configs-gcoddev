# From Gary Apaza - GCodDev

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from libqtile import hook

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    #Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    #VOLUME
    #Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    #Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    #Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # My Configs
    Key([mod], "Return", lazy.spawn('alacritty'), desc="Launch terminal"),
    Key([mod, "shift"], "Return", lazy.spawn('thunar'), desc='Archivos'),
    #Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Abrir menu"),
    Key([mod], "m", lazy.spawn("rofi -show drun combi -icon-theme 'We10X' -show-icons"), desc="Abrir menu"),
    Key([mod, 'shift'], "m", lazy.spawn("rofi -show"), desc="Abrir abiertos"),
    Key([mod], "x", lazy.spawn("archlinux-logout"), desc="logout"),
]

#groups = [Group(i) for i in "123456789"]
groups = [Group(i) for i in ["  ", " ﬏ ", "  ", "  ", "  ", "  ", " 辶 ", "  ", "  ",]]

for i, group in enumerate(groups):
    numDesktop=str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                numDesktop,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numDesktop,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

def init_colors():
    return [["#282c34", "#282c34"], # color 0
            ["#1c1f24", "#1c1f24"], # color 1
            ["#ffffff", "#ffffff"], # color 2
            ["#ff6c6b", "#ff6c6b"], # color 3
            ["#98be65", "#98be65"], # color 4
            ["#da8548", "#da8548"], # color 5
            ["#51afef", "#51afef"], # color 6
            ["#c678dd", "#c678dd"], # color 7
            ["#46d9ff", "#46d9ff"], # color 8
            ["#cacaca", "#cacaca"], # color 9
            ["#0066ff", "#0066ff"], # color 10
            ["#555555", "#555555"], # color 11
            ["#dddddd", "#dddddd"], # color 12
            ["#000000", "#000000"], # color 13
	   ]

colors = init_colors()

layouts = [
    layout.Columns(
        #border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_focus = colors[10],
        border_focus_stack = colors[1],
        border_normal = colors[1],
        border_normal_stack = colors[10],
        border_width = 2,
        margin = 5
    ),
    layout.Max(
        border_focus = colors[10],
        border_normal = colors[10],
        border_width = 2,
        margin = 4
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    border_width = 1,
                    disable_drag = True,
                    fontsize = 24,
                    foreground = colors[3],
                    highlight_method = 'block',
                    background = colors[0],
                    padding = 0,
                    active = colors[2],
                    inactive = colors[11],
                    margin_x = 0,
                    margin_y = 3,
                    other_current_screen_border = colors[1],
                    other_screen_border = colors[1],
                    this_current_screen_border = colors[13],
                    this_screen_border = colors[13],
                    urgent_alert_border = 'block',
                    urgent_border = colors[3],
                ),
                widget.Prompt(),
                widget.Sep(
                    background = colors[8],
                    foreground = colors[8]
                ),
                widget.CurrentLayout(
                    background = colors[8],
                    font = "Noto Sans Bold",
                    foreground = colors[1]
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[8],
                    padding = 0,
                    fontsize = 22
                ),

                widget.Sep(
                    background = colors[0],
                    foreground = colors[0]
                ),
                widget.WindowName(),
                
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                
                widget.TextBox(
                    text="",
                    foreground=colors[2],
                    padding = 0,
                    fontsize = 22
                ),
                widget.TextBox(
                    font="FontAwesome",
                    text="  ",
                    foreground=colors[1],
                    background=colors[2],
                    padding = 0,
                    fontsize=16
                ),
                widget.Clock(
                    format="%H:%M:%S",
                    background=colors[2],
                    foreground=colors[1],
                    font='Noto Sans Bold'
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[2],
                    padding = 0,
                    fontsize = 22
                ),

                widget.Sep(
                    background = colors[0],
                    foreground = colors[0]
                ),

                widget.TextBox(
                    text="",
                    foreground=colors[12],
                    padding = 0,
                    fontsize = 22
                ),
                widget.TextBox(
                    font="FontAwesome",
                    text="  ",
                    foreground=colors[1],
                    background=colors[12],
                    padding = 0,
                    fontsize=16
                ),
                widget.Clock(
                    format="%a %p %d-%m-%Y",
                    background=colors[12],
                    foreground=colors[1],
                    font='Noto Sans Bold'
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[12],
                    padding = 0,
                    fontsize = 22
                ),
                
                widget.Sep(
                    background = colors[0],
                    foreground = colors[0]
                ),
                         
                widget.TextBox(
                    text="",
                    foreground=colors[6],
                    padding = 0,
                    fontsize = 22
                ),
                widget.TextBox(
                    font="FontAwesome",
                    text="  ",
                    foreground=colors[1],
                    background=colors[6],
                    padding = 0,
                    fontsize = 16
                ),
                widget.Memory(
                    foreground = colors[1],
                    background = colors[6],
                    mouse_callbacks = {'Button2': lazy.spawn('alacritty -e htop')},
                    fmt = 'Mem: {}',
                    padding = 5,
                    font = 'Noto Sans Bold'
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[6],
                    padding = 0,
                    fontsize = 22
                ),
                         
                widget.Sep(
                    background = colors[0],
                    foreground = colors[0]
                ),
                
                widget.TextBox(
                    text="",
                    foreground=colors[7],
                    padding = 0,
                    fontsize = 22
                ),
                widget.Volume(
                    foreground = colors[1],
                    background = colors[7],
                    fmt = 'Vol: {}',
                    padding = 5,
                    font = 'Noto Sans Bold',
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[7],
                    padding = 0,
                    fontsize = 22
                ),
                         
                widget.Sep(
                    background = colors[0],
                    foreground = colors[0]
                ),
                
                widget.TextBox(
                    text="",
                    foreground=colors[4],
                    padding = 0,
                    fontsize = 22
                ),
                widget.Battery(
                    font="Noto Sans Bold",
                    update_interval = 10,
                    fontsize = 12,
                    foreground = colors[1],
                    background = colors[4],
                    padding = 5,
                    format = '{percent:2.0%} - {hour:d}:{min:02d}'
                ),
	            widget.TextBox(
                    text="",
                    foreground=colors[4],
                    padding = 0,
                    fontsize = 22
                ),
                         
                widget.Sep(
                    background = colors[0],
                    foreground = colors[0]
                ),
                
                widget.TextBox(
                    text="",
                    foreground=colors[13],
                    padding = 0,
                    fontsize = 22
                ),
                widget.Systray(
                    background=colors[13],
                    icon_size=20,
                    padding=5
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[13],
                    padding = 0,
                    fontsize = 22
                ),    
                
                #widget.QuickExit(),
            ],
            25,
            background=colors[0]
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
