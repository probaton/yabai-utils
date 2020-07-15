import sys

from src.log import log
from src.actions.cycleDisplaySpaces import cycleDisplaySpaces
from src.actions.focusDisplay import focusDisplay
from src.actions.focusNextWindow import focusNextWindow
from src.actions.killEmptySpaces import killEmptySpaces
from src.actions.killSpace import killSpace
from src.actions.moveWindowToEmptySpace import moveWindowToEmptySpace

switcher = {
  "cycle-space-left": lambda: cycleDisplaySpaces(True),
  "cycle-space-right": lambda: cycleDisplaySpaces(),
  "focus-display": lambda: focusDisplay(sys.argv[2]),
  "focus-window-left": lambda: focusNextWindow(True),
  "focus-window-right": lambda: focusNextWindow(),
  "kill-empty-spaces": lambda: killEmptySpaces(),
  "kill-space": killSpace,
  "move-window-to-empty-space": moveWindowToEmptySpace,
}
try:
  switcher.get(sys.argv[1], lambda: print("Invalid instruction"))()
except Exception as e:
  log(str(e))
  raise e
