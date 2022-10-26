from ..commandLine import yabaiUtil
from ..store.storeId import storeId
from .restoreWindowFocus import restoreWindowFocus

def switchSpace(targetSpace, currentSpace = None):
  if currentSpace:
    currentSpaceWindows = yabaiUtil.query(f"--windows --space {currentSpace['index']}")
    try:
      focusedWindow = next(window for window in currentSpaceWindows if window["has-focus"] == True)
      storeId(currentSpace["id"], focusedWindow["id"], "space")
    except StopIteration:
      pass

  try:
    yabaiUtil.runCommand(f"space --focus {targetSpace['index']}")
  except Exception as e:
    if not str(e).endswith("cannot focus an already focused space.\n"):
      raise e

  restoreWindowFocus(targetSpace)
