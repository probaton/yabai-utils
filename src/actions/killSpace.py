from ..commandLine.yabaiUtil import query, runCommand
from .restoreWindowFocus import restoreWindowFocus

def getCurrentSpace(displayIndex):
  currentDisplaySpaces = query(f"--spaces --display {displayIndex}")
  try:
    return next(space for space in currentDisplaySpaces if space["is-visible"] == True)["index"]
  except StopIteration:
    return None 

def killSpace():
  currentDisplay = query("--displays --display")["index"]
  currentSpace = getCurrentSpace(currentDisplay)

  winIds = map(lambda win: win["id"], query("--windows --space"))
  for winId in winIds:
    runCommand(f"window {winId} --close")
  
  runCommand(f"space {currentSpace} --destroy")

  newCurrentSpace = getCurrentSpace(currentDisplay)
  if newCurrentSpace:
    restoreWindowFocus(query(f"--spaces --space {newCurrentSpace}"))
  else:
    restoreWindowFocus(query("--spaces --space"))

if __name__ == "__main__":
  killSpace()
