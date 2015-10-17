from psychopy import visual, core, data, gui, event
import time
import serial

# /dev/tty.KeySerial1 ? /dev/tty.USA19H142P1.1 ?
ser = serial.Serial(
                    port='com1',
                    baudrate=19200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                   )
if not ser.isOpen():
    ser.open()

print ser

ser.write('BUZ13\r')
time.sleep(1)
core.quit()

# setup
ser.write('DIA 26.59')
time.sleep(1)
ser.write('VOL ML')
time.sleep(1)
ser.write('TRGFT')
time.sleep(1)
ser.write('AL 0')
time.sleep(1)
ser.write('PF 0')
time.sleep(1)
ser.write('BP 1')
time.sleep(1)
ser.write('BP 1')
time.sleep(1)

ser.write('PHN 1')
ser.write('FUN RAT')
ser.write('RAT 750 MH')
ser.write('VOL 2.0')
ser.write('DIR INF')

ser.write('PHN 1')
ser.write('FUN RAT')
ser.write('RAT 750 MH')
ser.write('VOL 2.0')
ser.write('DIR INF')
ser.write('FUN RUN')



fullscr = False
monSize = [1024, 768]  # might need to change this at LCNI

info = {}

info['participant'] = ''
dlg = gui.DlgFromDict(info)
if not dlg.OK:
    core.quit()

info['dateStr'] = data.getDateStr()

win = visual.Window(monSize, fullscr=fullscr,
                    monitor='testMonitor', units='deg')

# instruction Stims
instruction1 = visual.TextStim(win, pos=(0, 0), text="You will see pictures of a chocolate milkshake that will be followed by tastes of milkshake. At certain points, you will be asked for a rating from 1 to 5. \n\nUse the button box to rate your craving for chocolate milkshake after seeing the picture. \n\nPress a button to continue.")
instruction2 = visual.TextStim(win, pos=(0, 0), text="When you are instructed to administer the dose of Crave Crush or placebo, move slowly and wait until the last five seconds to put it in your mouth. \n\nPress a button to continue.")
instruction3 = visual.TextStim(win, pos=(0, 0), text="Remember to follow the instructions carefully. \n\nPress a button when you are ready for the scan to begin.")

# Stims
fixation = visual.TextStim(win, text='+', pos=(0, 0), height=2)
taste_delivery = visual.TextStim(win, text='Taste delivery', pos=(0, 0))
administer_crave_crush = visual.TextStim(win, text='Administer crave crush', pos=(0, .6))
swallow = visual.TextStim(win, text='Swallow', pos=(0, 0))
milkshake = visual.ImageStim(win, image='Milkshake.jpg')

crave_rating = visual.RatingScale(win=win, name='crave_rating', marker=u'triangle', size=1.0, pos=[0.0, -0.5], low=1, high=5, labels=[u''], scale=u'Rate your craving from 1 - 5')


def run_block():
    for cycle in range(2):
        # Instructions
        while True:
            instruction1.draw()
            win.flip()
            if len(event.getKeys()) > 0:
                break
            event.clearEvents()
        while True:
            instruction2.draw()
            win.flip()
            if len(event.getKeys()) > 0:
                break
            event.clearEvents()
        while True:
            instruction3.draw()
            win.flip()
            if len(event.getKeys()) > 0:
                break
            event.clearEvents()

        # LET THE SCANNING BEGIN

        #  1> 10 sec blank screen with fixation cross
        for frame in range(60 * 10):
            fixation.draw()
            win.flip()

        #  2> 10 sec milkshake image
        for frame in range(60 * 10):
            milkshake.draw()
            win.flip()
        #  3> 5 sec milkshake image with craving scale below, participants are asked to rate their craving for the milkshake on the button box 1-5
        for frame in range(60 * 5):
            milkshake.draw()
            crave_rating.draw()
            # TODO: get bbox input
            win.flip()

        #  4> 20 second fixation cross
        for frame in range(60 * 20):
            fixation.draw()
            win.flip()
        #  5> Four cycles of taste delivery (10 sec each, screen that says 'taste delivery') and swallow (2 sec each, screen that says 'swallow')- total 48 sec

        # TODO - pump it baby!!!
        for cycle in range(4):
            for frame in range(60 * 10):
                taste_delivery.draw()
                win.flip()
            for frame in range(60 * 2):
                swallow.draw()
                win.flip()

        #  6> 20 second blank screen with fixation cross
        for frame in range(60 * 10):
            fixation.draw()
            win.flip()
        #  7> 10 sec milkshake image
        for frame in range(60 * 10):
            milkshake.draw()
            win.flip()
        #  8> 5 sec milkshake pic with craving scale below
        for frame in range(60 * 5):
            milkshake.draw()
            crave_rating.draw()
            # TODO: get bbox input
            win.flip()
        #  9> 60 sec screen that counts down and tells participant to administer crave crush/placebo
        if cycle == 0:
            timer = core.CountdownTimer(60)
            while timer.getTime() > 0:  # after 5s will become negative
                administer_crave_crush.draw()
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
