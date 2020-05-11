import yabaiUtil

def cycleSpaceDown():
  currentSpace = yabaiUtil.query("--spaces --space")
  displaySpaces = yabaiUtil.query("--spaces --display")
  currentIndex = displaySpaces.index(currentSpace)

  if currentIndex == 0:
    nextIndex = len(displaySpaces) - 1
  else:
    nextIndex = currentIndex - 1

  yabaiUtil.runCommand(f"space --focus {displaySpaces[nextIndex]['index']}")

cycleSpaceDown()
