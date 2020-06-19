from ..commandLine.yabaiUtil import query
from .switchSpace import switchSpace

def focusDisplay(targetDisplayIndex):
  targetDisplaySpaces = query(f"--spaces --display {targetDisplayIndex}")
  try:
    targetSpace = next(space for space in targetDisplaySpaces if space["visible"] == 1)
    switchSpace(targetSpace, query("--spaces --space"))
  except StopIteration:
    pass  

if __name__ == "__main__":
  from sys import argv
  focusDisplay(argv[1])
