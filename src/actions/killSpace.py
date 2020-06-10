from ..commandLine.yabaiUtil import query, runCommand
from .restoreWindowFocus import restoreWindowFocus

def killSpace():
  currentSpace = query("--spaces --space")["index"]

  winIds = map(lambda win: win["id"], query("--windows --space"))
  for winId in winIds:
    runCommand(f"window {winId} --close")
  
  runCommand(f"space {currentSpace} --destroy")
  restoreWindowFocus(query("--spaces --space"))

if __name__ == "__main__":
  killSpace()
