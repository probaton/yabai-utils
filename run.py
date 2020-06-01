import sys

from src.actions.cycleSpaceLeft import cycleSpaceLeft
from src.actions.cycleSpaceRight import cycleSpaceRight
from src.actions.focusWindowLeft import focusWindowLeft
from src.actions.focusWindowRight import focusWindowRight
from src.actions.killSpace import killSpace
from src.actions.moveWindowToEmptySpace import moveWindowToEmptySpace

switcher = {
  "cycle-space-left": cycleSpaceLeft,
  "cycle-space-right": cycleSpaceRight,
  "focus-window-left": focusWindowLeft,
  "focus-window-right": focusWindowRight,
  "kill-space": killSpace,
  "move-window-to-empty-space": moveWindowToEmptySpace
}
switcher.get(sys.argv[1], lambda: print("Invalid instruction"))()
