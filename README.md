# Yabai-utils
A library of instructions, written in Python 3, for the wondrous [Yabai tiling manager](https://github.com/koekeishiya/yabai) for MacOS. I wrote it because, although Yabai is without a doubt the best tiling manager currently available for MacOS, I found myself disagreeing with some minor (mostly multi-display-specific) implementation details. 

An obvious example is the way that, in a scenario where I have the single window on my left display focused, the Yabai command `yabai -m window --focus east` will return `could not locate a eastward managed window.` instead of focusing the window open on my right display. 

You can convert your Yabai instructions to `yabai-utils` by calling `run.py` with the appropriate instruction with `python3`. 

For the example above, you could replace
```
yabai -m window --focus east
```
with 
```
python3 <path-to-yabai-utils>/run.py focus-window-right
```

Note that `yabai-utils` will attempt to store your window's location (locally) when switching between displays or spaces. It does this in an attempt to compensate for the fact that Yabai will sometimes lose window focus when moving between spaces, forcing users to select a window with the mouse. It will only store the window/display/space ID locally, with the sole purpose of re-instating focus when switching back. This functionality may require extra permissions.  
