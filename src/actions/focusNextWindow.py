from ..commandLine import yabaiUtil

def focusNextWindow(reverse = False):
  visibleWindows = list(filter(lambda s: s["visible"] == 1, yabaiUtil.query("--windows")))
  visibleWindows.sort(key = lambda window: (window["frame"]["x"], window["frame"]["y"]))
  if reverse:
    visibleWindows.reverse()

  passedFocusedWindow = False
  for window in visibleWindows:
    if passedFocusedWindow:
      yabaiUtil.runCommand(f"window --focus {window['id']}")
      break
    if window["focused"] == 1:
      passedFocusedWindow = True
      