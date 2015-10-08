from psychopy import visual, core  # import some libraries from PsychoPy

win = visual.Window([800, 600], monitor = "self", units = "deg")
visual.ImageStim(win, image = 'test.png', pos = [0,0], size = 1)
win.update()
core.wait(2.0)
