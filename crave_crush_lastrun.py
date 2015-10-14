#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.00), Tue Oct 13 13:00:12 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import time
import serial

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'crave_crush'  # from the Builder filename that created this script
expInfo = {u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/nathann/code/sweetcrave/crave_crush.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image = visual.ImageStim(win=win, name='image',
    image=u'stimuli/Milkshake.jpg', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
rating = visual.RatingScale(win=win, name='rating', marker=u'triangle', size=1.0, pos=[0.0, -0.8], low=1, high=5, labels=[u''], scale=u'Rate your craving from 1 - 5')
image_2 = visual.ImageStim(win=win, name='image_2',
    image=None, mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
fixation_2 = visual.TextStim(win=win, ori=0, name='fixation_2',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

#------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
routineTimer.add(27.000000)
# update component parameters for each repeat
rating.reset()
# keep track of which components have finished
trialComponents = []
trialComponents.append(ISI)
trialComponents.append(fixation)
trialComponents.append(image)
trialComponents.append(rating)
trialComponents.append(image_2)
trialComponents.append(fixation_2)
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trial"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *fixation* updates
    if t >= 0.0 and fixation.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation.tStart = t  # underestimates by a little under one frame
        fixation.frameNStart = frameN  # exact frame index
        fixation.setAutoDraw(True)
    if fixation.status == STARTED and t >= (0.0 + (10.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        fixation.setAutoDraw(False)

    # *image* updates
    if t >= 10.0 and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t  # underestimates by a little under one frame
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    if image.status == STARTED and t >= (10.0 + (10.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        image.setAutoDraw(False)
    # *rating* updates
    if t >= 20.0 and rating.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating.tStart = t  # underestimates by a little under one frame
        rating.frameNStart = frameN  # exact frame index
        rating.setAutoDraw(True)
    continueRoutine &= rating.noResponse  # a response ends the trial

    # *image_2* updates
    if t >= 20 and image_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_2.tStart = t  # underestimates by a little under one frame
        image_2.frameNStart = frameN  # exact frame index
        image_2.setAutoDraw(True)
    if image_2.status == STARTED and t >= (20 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
        image_2.setAutoDraw(False)

    # *fixation_2* updates
    if t >= 25 and fixation_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation_2.tStart = t  # underestimates by a little under one frame
        fixation_2.frameNStart = frameN  # exact frame index
        fixation_2.setAutoDraw(True)
    if fixation_2.status == STARTED and t >= (25 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        fixation_2.setAutoDraw(False)
    # *ISI* period
    if t >= 0.0 and ISI.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI.tStart = t  # underestimates by a little under one frame
        ISI.frameNStart = frameN  # exact frame index
        ISI.start(0.5)
    elif ISI.status == STARTED: #one frame should pass before updating params and completing
        ISI.complete() #finish the static period

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating.response', rating.getRating())
thisExp.addData('rating.rt', rating.getRT())
thisExp.nextEntry()
win.close()
core.quit()
