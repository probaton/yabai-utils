import sys

from src.actions.cycleSpaceLeft import cycleSpaceLeft
from src.actions.cycleSpaceRight import cycleSpaceRight
from src.actions.focusWindowLeft import focusWindowLeft
from src.actions.focusWindowRight import focusWindowRight
from src.actions.killSpace import killSpace
from src.actions.moveWindowToEmptySpace import moveWindowToEmptySpace

instruction = sys.argv[1]
if instruction == "cycle-space-left":
  cycleSpaceLeft()
if instruction == "cycle-space-right":
  cycleSpaceRight()
if instruction == "focus-window-left":
  focusWindowLeft()
if instruction == "focus-window-right":
  focusWindowRight()
if instruction == "kill-space":
  killSpace()
if instruction == "move-window-to-empty-space":
  moveWindowToEmptySpace()
 