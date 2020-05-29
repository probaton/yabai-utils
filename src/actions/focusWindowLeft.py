from ..commandLine.yabaiUtil import query
from .focusNextWindow import focusNextWindow

def focusWindowLeft():
  visibleWindows = list(filter(lambda s: s["visible"] == 1, query("--windows")))
  visibleWindows.sort(key = lambda window: (window["frame"]["x"], window["frame"]["y"]))
  visibleWindows.reverse()

  focusNextWindow(visibleWindows)

if __name__ == "__main__":
  focusWindowLeft()
  