from ..commandLine import yabaiUtil
from .switchSpace import switchSpace

def cycleSpaceRight():
  currentSpace = yabaiUtil.query("--spaces --space")
  displaySpaces = yabaiUtil.query("--spaces --display")
  currentPosition = displaySpaces.index(currentSpace) + 1

  nextIndex = 0 if currentPosition >= len(displaySpaces) else currentPosition

  switchSpace(currentSpace, displaySpaces[nextIndex])

if __name__ == "__main__":
  cycleSpaceRight()
