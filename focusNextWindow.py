from yabaiUtil import runCommand

def focusNextWindow(windows):
  passedFocusedWindow = False
  for window in windows:
    if passedFocusedWindow:
      runCommand(f"window --focus {window['id']}")
      break
    if window["focused"] == 1:
      print('focused', window)
      passedFocusedWindow = True
      