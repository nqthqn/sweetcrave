from psychopy import visual, core, event, data, gui
import shutil


monSize = [800, 600]

info = {}
info['fullscr'] = True
info['participant'] = ''
info['condition'] = ''
dlg = gui.DlgFromDict(info)
if not dlg.OK:
    core.quit()

info['dateStr'] = data.getDateStr()

info['instructions'] = "You will see pictures of food and pictures of water. \n\nImagine you are eating the foods or drinking the water when the pictures appear. \n\nPress a button when you are ready for the scan to begin."

win = visual.Window(monSize, fullscr=info['fullscr'],
                    monitor='testMonitor', units='deg')
fixation = visual.TextStim(win, text='+', pos=(0, 0), height=2)
instructions = visual.TextStim(win, pos=(0, 0), text=info['instructions'])
scan_trigger_text = visual.TextStim(win, text='Waiting for scan trigger...', pos=(0, 0))

respClock = core.Clock()

# set up the trials/experiment
if info['condition'] == '1':
    conditions = data.importConditions('sweet_image_condition1.csv')
elif info['condition'] == '2':
    conditions = data.importConditions('sweet_image_condition2.csv')
else:
    core.quit()  # nothing to do


def run_block():
    # create trial handler (loop)
    trials = data.TrialHandler(trialList=conditions, nReps=1,
                               method='sequential')

    while True:
        instructions.draw()
        win.flip()
        if len(event.getKeys()) > 0:
            break
        event.clearEvents()

    while True:
        scan_trigger_text.draw()
        win.flip()
        if 'apostrophe' in event.waitKeys():
            break
        event.clearEvents()

    for thisTrial in trials:
        cue = visual.ImageStim(win, image='stimuli/' + thisTrial.image)

        # jitter s fixation cross
        jitter = int(60 * thisTrial.jitter)
        fixation.setAutoDraw(True)
        for frameN in range(jitter):
            win.flip()

        #  5s sweet food
        cue.setAutoDraw(True)
        for frameN in range(300):
            win.flip()
        cue.setAutoDraw(False)

        event.clearEvents()

        win.flip()
    # END LOOP


run_block()
shutil.copyfile('sweet_image_condition{0}.csv'.format(info['condition']), 'data/{participant}_condition{condition}_{dateStr}.csv'.format(**info))
win.close()
core.quit()
