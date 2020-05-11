import yabaiUtil

def cycleSpaceLeft():
  currentSpace = yabaiUtil.query("--spaces --space")
  displaySpaces = yabaiUtil.query("--spaces --display")
  currentIndex = displaySpaces.index(currentSpace)

  if currentIndex == 0:
    nextIndex = len(displaySpaces) - 1
  else:
    nextIndex = currentIndex - 1

  yabaiUtil.runCommand(f"space --focus {displaySpaces[nextIndex]['index']}")

if __name__ == "__main__":
  cycleSpaceLeft()