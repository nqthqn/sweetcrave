# TODO
#  - larger fixation cross
#  - verify csv data

from psychopy import visual, core, event, data, gui, logging

DEBUG = False
fullscr = False
monSize = [1024, 768]  # might need to change this at LCNI
if DEBUG:
    logging.console.setLevel(logging.DEBUG)
else:
    logging.console.setLevel(logging.WARNING)


info = {}
if not DEBUG:
    info['participant'] = ''
info['condition'] = ''
dlg = gui.DlgFromDict(info)
if not dlg.OK:
    core.quit()
# info['fixFrames'] = 30  # 0.5s at 60Hz, 1s = 60 frames
info['calibration'] = 60  # 1s = 60 frames (multiple the jitter by 60)
info['cueFrames'] = 300  # 5s at 60Hz
info['dateStr'] = data.getDateStr()

# initialise stimuli
win = visual.Window(monSize, fullscr=fullscr,
                    monitor='testMonitor', units='deg')
fixation = visual.TextStim(win, text='+', pos=(0, 0))
respClock = core.Clock()

# set up the trials/experiment
if info['condition'] == '1':
    conditions = data.importConditions('sweet_image_condition1.csv')
elif info['condition'] == '2':
    conditions = data.importConditions('sweet_image_condition2.csv')
else:
    core.quit()  # nothing to do


def pl(*args):
    if DEBUG:
        for a in args:
            print a


def run_block():
    """ Runs a block of trials
    """
    # create trial handler (loop)
    trials = data.TrialHandler(trialList=conditions, nReps=1,
                               method='sequential')

    # create the base filename for our data files
    if not DEBUG:
        filename = "data/{participant}_{dateStr}".format(**info)
        logfile = logging.LogFile(filename + ".log",
                                  filemode='w',
                                  level=logging.EXP)

        # add trials to the experiment handler to store data
        thisExp = data.ExperimentHandler(name='Sweet Image', version='1.0',
                                         extraInfo=info, dataFileName=filename)
        # there could be other loops (like practice loop)
        thisExp.addLoop(trials)

    # Loop through trials
    for thisTrial in trials:
        pl(thisTrial)
        cue = visual.ImageStim(win, image='stimuli/' + thisTrial.image)
        # fixation period
        jitter = int(info['calibration'] * thisTrial.jitter)
        print 'jitter={0}'.format(jitter)
        fixation.setAutoDraw(True)
        for frameN in range(jitter):
            win.flip()

        # present cue
        cue.setAutoDraw(True)
        for frameN in range(info['cueFrames']):
            win.flip()
        cue.setAutoDraw(False)

        # win.callOnFlip(respClock.reset)
        event.clearEvents()
        respClock.getTime()
        win.flip()

        # Update log file
        if not DEBUG:
            thisExp.nextEntry()

# Practice

run_block()
# TODO: Show final message
