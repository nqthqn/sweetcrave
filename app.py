from psychopy import visual, core  # import some libraries from PsychoPy

# create a window
mywin = visual.Window([1280, 720], monitor="testMonitor", units="deg")
print mywin
# create some stimuli
grating = visual.GratingStim(win=mywin, mask="circle", size=6, pos=[0, 0], sf=3)
fixation = visual.GratingStim(win=mywin, size=0.5, pos=[0, -6], sf=0, rgb=-1)

# draw the stimuli and update the window
grating.draw()
fixation.draw()
mywin.update()

# pause, so you get a chance to see it!
core.wait(5.0)
