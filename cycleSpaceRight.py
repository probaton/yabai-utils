import yabaiUtil

def cycleSpaceRight():
  currentSpace = yabaiUtil.query("--spaces --space")
  displaySpaces = yabaiUtil.query("--spaces --display")
  currentIndex = displaySpaces.index(currentSpace)

  if currentIndex >= len(displaySpaces) - 1:
    nextIndex = 0
  else:
    nextIndex = currentIndex + 1

  yabaiUtil.runCommand(f"space --focus {displaySpaces[nextIndex]['index']}")

if __name__ == "__main__":
  cycleSpaceRight()
