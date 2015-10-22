# Crave Crush Experiement. 11/20/2015
# Author: Nathan Nichols <nathann@ori.org>

from psychopy import visual, core, data, gui, event, data
import csv
import time
import serial

# Lab tech setup

monSize = [800, 600]
info = {}
info['fullscr'] = True
info['port'] = 'com1'
info['participant'] = ''
dlg = gui.DlgFromDict(info)
if not dlg.OK:
    core.quit()
info['dateStr'] = data.getDateStr()

# Serial connection and commands setup
ser = serial.Serial(
                    port=info['port'],
                    baudrate=19200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                   )
if not ser.isOpen():
    ser.open()

# sanity check
ser.write('BUZ13\r')
time.sleep(1)

# Pump setup and phases: infuse 1mL@6mm, withdraw .1mL@15mm (max), stop pump
pump_setup = ['VOL ML\r','TRGFT\r','AL 0\r','PF 0\r','BP 1\r','BP 1\r']
pump_phases = ['dia26.59\r', 'phn01\r', 'funrat\r', 'rat6.6mm\r', 'vol1\r', 'dirinf\r', \
'phn02\r', 'funrat\r', 'rat15mm\r', 'vol0.1\r', 'dirwdr\r', \
'phn03\r', 'funstp\r']

for c in pump_setup:
    ser.write(c)
    time.sleep(.25)

for c in pump_phases:
    ser.write(c)
    time.sleep(.25)

# HELPER FUNCTIONS
def show_instruction(instrStim):
    # shows an instruction until a key is hit.
    while True:
        instrStim.draw()
        win.flip()
        if len(event.getKeys()) > 0:
            break
        event.clearEvents()


def show_stim(stim, seconds):
    # shows a stim for a given number of seconds
    for frame in range(60 * seconds):
        stim.draw()
        win.flip()

# MONITOR
win = visual.Window(monSize, fullscr=info['fullscr'],
                    monitor='testMonitor', units='deg')
# STIMS
instruction1_text = visual.TextStim(win, pos=(0, 0), text="You will see pictures of a chocolate milkshake that will be followed by tastes of milkshake. At certain points, you will be asked for a rating from 0 to 4. \n\nUse the button box to rate your craving for chocolate milkshake after seeing the picture. \n\nPress a button to continue.")
instruction2_text = visual.TextStim(win, pos=(0, 0), text="When you are instructed to administer the dose of Crave Crush or placebo, move slowly and wait until the last five seconds to put it in your mouth. \n\nPress a button to continue.")
instruction3_text = visual.TextStim(win, pos=(0, 0), text="Remember to follow the instructions carefully. \n\nPress a button to continue.")
fixation_text = visual.TextStim(win, text='+', pos=(0, 0), height=2)
taste_delivery_text = visual.TextStim(win, text='Taste delivery', pos=(0, 0))
administer_crave_crush_text = visual.TextStim(win, text='Administer Crave Crush/Placebo now', pos=(0, .6))
dissolve_text = visual.TextStim(win, text='Wait for Crave Crush/Placebo to dissolve', pos=(0, .6))
pumping_text = visual.TextStim(win, text='Pumping...', pos=(0, 0))
pumping_ready_text = visual.TextStim(win, text='Ready to pump. Press \'c\' to initiate.', pos=(0, 0))
scan_trigger_text = visual.TextStim(win, text='Waiting for scan trigger...', pos=(0, 0))
swallow_text = visual.TextStim(win, text='Swallow', pos=(0, 0))
milkshake_image = visual.ImageStim(win, image='Milkshake.jpg')
milkshake_image2 = visual.ImageStim(win, image='Milkshake2.jpg', pos=(0,.5))
crave_rating_scale = visual.RatingScale(win=win, name='crave_rating', marker=u'triangle', size=1.0, pos=[0.0, -0.7], low=0, high=4, labels=[u''], scale=u'Rate your craving from 0 - 4',singleClick=True)
ratings_and_onsets = [] # ALL THE DATA


"""
    The main run block!
"""

def run_block():
    # Pump test
    while True:
        pumping_ready_text.draw()
        win.flip()
        if 'c' in event.waitKeys():
            break
        event.clearEvents()
    ser.write('run\r')
    while True:
        pumping_text.draw()
        win.flip()
        if 'c' in event.waitKeys():
            break
        event.clearEvents()

    # Instructions (press any key to continue)
    show_instruction(instruction1_text)
    show_instruction(instruction2_text)
    show_instruction(instruction3_text)

    # Await scan trigger
    while True:
        scan_trigger_text.draw()
        win.flip()
        # keycode 39
        if 'apostrophe' in event.waitKeys():
            break
        event.clearEvents()

    clock=core.Clock()
    for cycle in [0,1]:
        t = clock.getTime()
        ratings_and_onsets.append(['fixation',t])
        show_stim(fixation_text, 10)  # 10 sec blank screen with fixation cross
        t = clock.getTime()
        ratings_and_onsets.append(['milkshake',t])
        show_stim(milkshake_image, 10)  # 10 sec milkshake image
        # >>5 sec milkshake image with craving scale below, participants are asked to rate their craving for the milkshake on the button box 1-5
        t = clock.getTime()
        ratings_and_onsets.append(['rate_milkshake',t])
        for frame in range(60 * 5):
            milkshake_image2.draw()
            crave_rating_scale.draw()
            win.flip()
        if crave_rating_scale.noResponse:
            ratings_and_onsets.append(['rating',-1])
            crave_rating_scale.reset()
        else:
            rate = crave_rating_scale.getRating()
            crave_rating_scale.reset()
            ratings_and_onsets.append(['rating',rate])
        show_stim(fixation_text, 20) #  20 second fixation cross
        #  Four cycles of taste delivery (10 sec each, screen that says 'taste delivery') and swallow (2 sec each, screen that says 'swallow')- total 48 sec
        for i in [0,1,2,3]:
            ser.write('run\r')
            t = clock.getTime()
            ratings_and_onsets.append(['taste_delivery',t])
            for frame in range(60 * 10):
                taste_delivery_text.draw()
                win.flip()
            t = clock.getTime()
            ratings_and_onsets.append(['swallow',t])
            for frame in range(60 * 2):
                swallow_text.draw()
                win.flip()
        t = clock.getTime()
        ratings_and_onsets.append(['fixation',t])
        show_stim(fixation_text, 20) #  20 second blank screen with fixation cross
        t = clock.getTime()
        ratings_and_onsets.append(['milkshake',t])
        show_stim(milkshake_image,10) #  10 sec milkshake image
         # >>5 sec milkshake image with craving scale below, participants are asked to rate their craving for the milkshake on the button box 1-5
        t = clock.getTime()
        ratings_and_onsets.append(['rate_milkshake',t])
        for frame in range(60 * 5):
            milkshake_image2.draw()
            crave_rating_scale.draw()
            win.flip()
        if crave_rating_scale.noResponse:
            ratings_and_onsets.append(['rating',-1])
            crave_rating_scale.reset()
        else:
            rate = crave_rating_scale.getRating()
            crave_rating_scale.reset()
            ratings_and_onsets.append(['rating',rate])

        #  9> 60 sec screen that counts down and tells participant to administer crave crush/placebo
        if cycle == 0:
            timer = core.CountdownTimer(60)
            t = clock.getTime()
            ratings_and_onsets.append(['administer_crave_crush',t])
            while timer.getTime() > 0:  # after 5s will become negative
                administer_crave_crush_text.draw()
                counter = visual.TextStim(win, text='\n\n{0} seconds'.format(int(timer.getTime())))
                counter.draw()
                win.flip()
            #  10> 180 second blank screen for the crave crush/placebo to melt
            timer = core.CountdownTimer(180)
            t = clock.getTime()
            ratings_and_onsets.append(['wait_for_dissolve',t])
            while timer.getTime() > 0:  # after 5s will become negative
                dissolve_text.draw()
                counter = visual.TextStim(win, text='\n\n{0} seconds'.format(int(timer.getTime())))
                counter.draw()
                win.flip()

run_block()
win.close()
print ratings_and_onsets

myfile = open('data/{participant}_{dateStr}.csv'.format(**info), 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(['event','data'])
for row in ratings_and_onsets:
    wr.writerow(row)

core.quit()
