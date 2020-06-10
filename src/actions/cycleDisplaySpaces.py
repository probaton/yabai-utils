from ..commandLine import yabaiUtil
from .switchSpace import switchSpace

def cycleDisplaySpaces(reverse = False):
  displaySpaces = yabaiUtil.query("--spaces --display")
  if reverse:
    displaySpaces.reverse()

  currentSpace = yabaiUtil.query("--spaces --space")
  currentIndex = displaySpaces.index(currentSpace)

  nextIndex = currentIndex + 1 if currentIndex < len(displaySpaces) - 1 else 0
  switchSpace(displaySpaces[nextIndex], currentSpace)
