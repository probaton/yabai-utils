from ..commandLine import yabaiUtil

def cycleSpaceRight():
  currentSpace = yabaiUtil.query("--spaces --space")
  displaySpaces = yabaiUtil.query("--spaces --display")
  currentPosition = displaySpaces.index(currentSpace) + 1

  nextIndex = 0 if currentPosition >= len(displaySpaces) else currentPosition

  yabaiUtil.runCommand(f"space --focus {displaySpaces[nextIndex]['index']}")

if __name__ == "__main__":
  cycleSpaceRight()
