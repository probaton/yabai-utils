import sys

from ..commandLine.yabaiUtil import query, runCommand

def moveWindowToDisplay(displayId):
  currentSpaceWindows = query("--windows --space")
  currentSpace = query("--spaces --space")["index"]
  
  runCommand(f"window --display {displayId}")
  # if len(currentSpaceWindows) == 1:
    # runCommand(f"space --destroy {currentSpace}")
  runCommand(f"space --destroy 3")

  print(currentSpace)

if __name__ == "__main__":
  moveWindowToDisplay(sys.argv[1])