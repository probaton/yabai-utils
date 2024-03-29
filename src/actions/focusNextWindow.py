from ..commandLine import yabaiUtil
from ..store.storeId import storeId

def focusNextWindow(reverse = False):
  visibleWindows = list(filter(lambda s: s["is-visible"] == True, yabaiUtil.query("--windows")))
  visibleWindows.sort(key = lambda window: (window["frame"]["x"], window["frame"]["y"]))
  if reverse:
    visibleWindows.reverse()

  currentWindow = next(window for window in visibleWindows if window["has-focus"] == True)
  try:
    nextWindow = visibleWindows[visibleWindows.index(currentWindow) + 1]
  except IndexError:
    return

  if currentWindow["space"] != nextWindow["space"]:
    currentSpace = yabaiUtil.query("--spaces --space")
    storeId(currentSpace["id"], currentWindow["id"], "space")
  
  yabaiUtil.runCommand(f"window --focus {nextWindow['id']}")
