from yabaiUtil import query, runCommand

def getEmptySpace():
  spaces = query("--spaces --display")
  return next(space for space in spaces if space["windows"] == [])

def moveWindowToEmptySpace():
  try:
    emptySpace = getEmptySpace()
  except StopIteration:
    runCommand("space --create")
    emptySpace = getEmptySpace()
  
  runCommand(f"window --space {emptySpace['index']}")
  runCommand(f"space --focus {emptySpace['index']}")

if __name__ == "__main__":
  moveWindowToEmptySpace()
