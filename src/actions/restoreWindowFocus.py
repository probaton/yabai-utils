from ..commandLine import yabaiUtil
from ..store.getId import getId

def restoreWindowFocus(space):
  windowId = getId(space["id"], "space")
  if windowId and int(windowId) in space["windows"]:
    yabaiUtil.runCommand(f"window --focus {windowId}")
