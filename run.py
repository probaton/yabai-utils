import sys

from src.log import log
from src.actions.cycleDisplaySpaces import cycleDisplaySpaces
from src.actions.focusDisplay import focusDisplay
from src.actions.focusNextWindow import focusNextWindow
from src.actions.killEmptySpaces import killEmptySpaces
from src.actions.killSpace import killSpace
from src.actions.moveWindowToDisplay import moveWindowToDisplay
from src.actions.moveWindowToEmptySpace import moveWindowToEmptySpace
from src.actions.moveSpaceToDisplay import moveSpaceToDisplay
from src.actions.resizeWindow import WindowResizer

switcher = {
  "cycle-space-left": lambda: cycleDisplaySpaces(True),
  "cycle-space-right": lambda: cycleDisplaySpaces(),
  "focus-display": lambda: focusDisplay(sys.argv[2]),
  "focus-window-left": lambda: focusNextWindow(True),
  "focus-window-right": lambda: focusNextWindow(),
  "kill-empty-spaces": lambda: killEmptySpaces(),
  "kill-space": killSpace,
  "move-window-to-display": lambda: moveWindowToDisplay(sys.argv[2]),
  "move-window-to-empty-space": moveWindowToEmptySpace,
  "move-space-to-display": lambda: moveSpaceToDisplay(sys.argv[2]),
  "expand-window": WindowResizer().expand,
  "shrink-window": WindowResizer().shrink,
}
try:
  switcher.get(sys.argv[1], lambda: print("Invalid instruction"))()
except Exception as e:
  log(f"Failed to execute {sys.argv[1]}:\n{str(e)}")
  raise e
