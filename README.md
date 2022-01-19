# Magic Window
`magic-window` is a CLI tool to fetch and dismiss a window / container for i3 and sway.

# Usage
Make the currently focused container the magic window:
```
$ magic-window pick
```
Hide it with:
```
$ magic-window hide
```
Show it with:
```
$ magic-window show
```
Toggle between show / hide
```
$ magic-window toggle
```

# Installation
```
$ pip install magic-window
```


# TODO
- Attempt to preserve size of magic window when moving it between monitors
  - Bind it to a single monitor
  - Can have a magic window per monitor?
- When the magic window is shown and is a container with multiple windows, select a valid child to focus.
-