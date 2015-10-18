# TODO
# - get data of cue onsets in csv with participant number prefixed
# - adjust the rating scale

from psychopy import visual, core, data, gui, event, data
import csv
import time
import serial

# Lab tech setup

monSize = [800, 600]
info = {}
info['fullscr'] = True
info['participant'] = ''
dlg = gui.DlgFromDict(info)
if not dlg.OK:
    core.quit()
info['dateStr'] = data.getDateStr()

# Serial connection and commands setup
ser = serial.Serial(
                    port='com1',
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

pump_setup = ['VOL ML\r','TRGFT\r','AL 0\r','PF 0\r','BP 1\r','BP 1\r']

# infuse 1mL@6mm, withdraw .1mL@15mm (max), stop pump
pump_phases = ['dia26.59\r', 'phn01\r', 'funrat\r', 'rat6mm\r', 'vol1\r', 'dirinf\r', \
'phn02\r', 'funrat\r', 'rat15mm\r', 'vol0.1\r', 'dirwdr\r', \
'phn03\r', 'funstp\r']

for c in pump_setup:
    ser.write(c)
    time.sleep(.25)

for c in pump_phases:
    ser.write(c)
    time.sleep(.25)

win = visual.Window(monSize, fullscr=info['fullscr'],
                    monitor='testMonitor', units='deg')

# instruction Stims
instruction1_text = visual.TextStim(win, pos=(0, 0), text="You will see pictures of a chocolate milkshake that will be followed by tastes of milkshake. At certain points, you will be asked for a rating from 1 to 5. \n\nUse the button box to rate your craving for chocolate milkshake after seeing the picture. \n\nPress a button to continue.")
instruction2_text = visual.TextStim(win, pos=(0, 0), text="When you are instructed to administer the dose of Crave Crush or placebo, move slowly and wait until the last five seconds to put it in your mouth. \n\nPress a button to continue.")
instruction3_text = visual.TextStim(win, pos=(0, 0), text="Remember to follow the instructions carefully. \n\nPress a button to continue.")

# Other Stims
fixation_text = visual.TextStim(win, text='+', pos=(0, 0), height=2)
taste_delivery_text = visual.TextStim(win, text='Taste delivery', pos=(0, 0))
administer_crave_crush_text = visual.TextStim(win, text='Administer Crave Crush/Placebo now', pos=(0, .6))
pumping_text = visual.TextStim(win, text='Pumping...', pos=(0, 0))
pumping_ready_text = visual.TextStim(win, text='Ready to pump. Press \'c\' to initiate.', pos=(0, 0))
scan_trigger_text = visual.TextStim(win, text='Waiting for scan trigger...', pos=(0, 0))
swallow_text = visual.TextStim(win, text='Swallow', pos=(0, 0))
milkshake_image = visual.ImageStim(win, image='Milkshake.jpg')
milkshake_image2 = visual.ImageStim(win, image='Milkshake2.jpg', pos=(0,.5))
crave_rating_scale = visual.RatingScale(win=win, name='crave_rating', marker=u'triangle', size=1.0, pos=[0.0, -0.7], low=1, high=5, labels=[u''], scale=u'Rate your craving from 1 - 5')

ratings = [] # ALL THE DATA

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

    for cycle in [0,1]:

        # LET THE SCANNING BEGIN
        show_stim(fixation_text, 10)  # 10 sec blank screen with fixation cross
        show_stim(milkshake_image, 10)  # 10 sec milkshake image
        # 5 sec milkshake image with craving scale below, participants are asked to rate their craving for the milkshake on the button box 1-5
        for frame in range(60 * 5):
            milkshake_image2.draw()
            crave_rating_scale.draw()
            win.flip()
        if crave_rating_scale.noResponse:
            ratings.append(-1)
        else:
            ratings.append(crave_rating_scale.getRating())
        crave_rating_scale.reset()
        show_stim(fixation_text, 20) #  20 second fixation cross

        #  Four cycles of taste delivery (10 sec each, screen that says 'taste delivery') and swallow (2 sec each, screen that says 'swallow')- total 48 sec
        for i in [0,1,2,3]:
            ser.write('run\r')
            for frame in range(60 * 10):
                taste_delivery_text.draw()
                win.flip()
            for frame in range(60 * 2):
                swallow_text.draw()
                win.flip()

        show_stim(fixation_text, 20) #  20 second blank screen with fixation cross
        show_stim(milkshake_image,10) #  10 sec milkshake image
         # 5 sec milkshake image with craving scale below, participants are asked to rate their craving for the milkshake on the button box 1-5
        for frame in range(60 * 5):
            milkshake_image2.draw()
            crave_rating_scale.draw()
            win.flip()
        if crave_rating_scale.noResponse:
            ratings.append(0)
        else:
            ratings.append(crave_rating_scale.getRating())

        #  9> 60 sec screen that counts down and tells participant to administer crave crush/placebo
        if cycle == 0:
            timer = core.CountdownTimer(60)
            while timer.getTime() > 0:  # after 5s will become negative
                administer_crave_crush_text.draw()
                counter = visual.TextStim(win, text='\n\n{0} seconds'.format(int(timer.getTime())))
                counter.draw()
                win.flip()
            #  10> 180 second blank screen for the crave crush/placebo to melt
            timer = core.CountdownTimer(180)
            while timer.getTime() > 0:  # after 5s will become negative
                counter = visual.TextStim(win, text='\n\n{0} seconds'.format(int(timer.getTime())))
                counter.draw()
                win.flip()

run_block()
win.close()
print ratings

myfile = open('data/{participant}_{dateStr}'.format(**info), 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(ratings)

core.quit()
