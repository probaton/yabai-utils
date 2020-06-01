from ..commandLine import yabaiUtil
from ..store.storeId import storeId
from .restoreWindowFocus import restoreWindowFocus

def switchSpace(targetSpace, currentSpace = None):
  if currentSpace:
    currentSpaceWindows = yabaiUtil.query(f"--windows --space {currentSpace['index']}")
    try:
      focusedWindow = next(window for window in currentSpaceWindows if window["focused"] == 1)
      storeId(currentSpace["id"], focusedWindow["id"], "space")
    except StopIteration:
      pass

  try:
    yabaiUtil.runCommand(f"space --focus {targetSpace['index']}")
  except Exception as err:
    if str(err).endswith("cannot focus an already focused space."):
      pass

  restoreWindowFocus(targetSpace)
