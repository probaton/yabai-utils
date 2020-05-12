from yabaiUtil import query
from focusNextWindow import focusNextWindow

def focusWindowRight():
  visibleWindows = list(filter(lambda s: s["visible"] == 1, query("--windows")))
  visibleWindows.sort(key = lambda window: (window["frame"]["x"], window["frame"]["y"]))

  focusNextWindow(visibleWindows)

if __name__ == "__main__":
  focusWindowRight()
  