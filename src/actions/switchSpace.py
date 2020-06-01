from ..commandLine import yabaiUtil
from ..store.getId import getId
from ..store.storeId import storeId

def switchSpace(currentSpace, targetSpace):
  currentSpaceWindows = yabaiUtil.query(f"--windows --space {currentSpace['index']}")
  try:
    focusedWindow = next(window for window in currentSpaceWindows if window["focused"] == 1)
  except StopIteration:
    pass

  storeId(currentSpace["id"], focusedWindow["id"], "space")
  yabaiUtil.runCommand(f"space --focus {targetSpace['index']}")

  try:
    targetWindowId = getId(targetSpace["id"], "space")
    yabaiUtil.runCommand(f"window --focus {targetWindowId}")
  except Exception as err:
    if str(err).endswith("value 'None' is not a valid option for WINDOW_SEL"):
      pass

