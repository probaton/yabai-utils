from ..commandLine import yabaiUtil
from ..store.getId import getId

def restoreWindowFocus(space):
  windowId = getId(space["id"], "space")
  if windowId and int(windowId) in space["windows"]:
    return yabaiUtil.runCommand(f"window --focus {windowId}")
  
  spaceWindows = yabaiUtil.query("--windows --space")
  if len(spaceWindows) == 1:
    return yabaiUtil.runCommand(f"window --focus {spaceWindows[0]['id']}")
