from ..commandLine.yabaiUtil import query, runCommand
from .switchSpace import switchSpace

def getEmptySpace():
  spaces = query("--spaces --display")
  try:
    return next(space for space in spaces if space["windows"] == [])
  except StopIteration:
    return None

def moveWindowToEmptySpace():
  emptySpace = getEmptySpace()
  if not emptySpace:
    runCommand("space --create")
    emptySpace = getEmptySpace()
  
  runCommand(f"window --space {emptySpace['index']}")
  switchSpace(emptySpace)

if __name__ == "__main__":
  moveWindowToEmptySpace()
