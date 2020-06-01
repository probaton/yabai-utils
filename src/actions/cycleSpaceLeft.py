from ..commandLine import yabaiUtil
from .switchSpace import switchSpace

def cycleSpaceLeft():
  currentSpace = yabaiUtil.query("--spaces --space")
  displaySpaces = yabaiUtil.query("--spaces --display")
  currentIndex = displaySpaces.index(currentSpace)

  nextIndex = (len(displaySpaces) if currentIndex == 0 else currentIndex) - 1

  switchSpace(displaySpaces[nextIndex], currentSpace)

if __name__ == "__main__":
  cycleSpaceLeft()
