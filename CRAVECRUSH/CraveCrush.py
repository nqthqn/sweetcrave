from psychopy import visual, core, data, gui, logging, hardware
import time
import serial


# TODO
#  - larger fixation cross
#  - get participant num input
#  - chuckt@uoregon.edu < ask him




ser = serial.Serial(
  port='/dev/tty.KeySerial1', # /dev/tty.KeySerial1 ? /dev/tty.USA19H142P1.1 ?
  baudrate=19200, # 19200
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS
)
if not ser.isOpen():
    ser.open()


def buzzer():
    ser.write('buz1')
    time.sleep(1)
    ser.write('buz0')
    time.sleep(1)
    ser.write('buz1')
    time.sleep(1)
    ser.write('buz0')
    time.sleep(1)

DEBUG = True
fullscr = False
monSize = [1024, 768]  # might need to change this at LCNI
if DEBUG:
    logging.console.setLevel(logging.DEBUG)
else:
    logging.console.setLevel(logging.WARNING)

if DEBUG:
    buzzer()

info = {}
if not DEBUG:
    info['participant'] = ''
dlg = gui.DlgFromDict(info)
if not dlg.OK:
    core.quit()
# info['fixFrames'] = 30  # 0.5s at 60Hz, 1s = 60 frames
info['calibration'] = 60  # 1s = 60 frames (multiple the jitter by 60)
info['cueFrames'] = 5 * 60  # 5s at 60Hz = 300 frames
info['dateStr'] = data.getDateStr()

# initialise stimuli
win = visual.Window(monSize, fullscr=fullscr,
                    monitor='testMonitor', units='deg')
fixation = visual.Circle(win, size=0.5,
                         lineColor='white', fillColor='lightGrey')
respClock = core.Clock()


def pl(*args):
    if DEBUG:
        for a in args:
            print a

def send_cmd(cmd):
    global ser
    ser.write(cmd)

def run_block():
    """ Runs a block of trials
    """
    not_done = True
    # Text Stim
    fixation = visual.TextStim(win, text='+', pos=(0, 0))
    taste_delivery = visual.TextStim(win, text='Taste delivery', pos=(0, 0))
    administer_crave_crush = visual.TextStim(win, text='administer crave crush')
    swallow = visual.TextStim(win, text='Swallow', pos=(0, 0))
    craving = visual.TextStim(win, text='Rate your craving (1 - 5)',
                              pos=(0, .6))
    # Image Stim
    milkshake = visual.ImageStim(win, image='stimuli/Milkshake.jpg')


    while not_done:
        #1 10 sec blank screen with fixation cross
        fixation.setAutoDraw(True)  # automatically draw every frame
        win.flip()
        core.wait(10.0)
        #2 10 sec milkshake image
        milkshake.setAutoDraw(True)
        win.flip()
        core.wait(10.0)
        #3 5 sec milkshake image with craving scale below, participants are asked to rate their craving for the milkshake on the button box 1-5
        milkshake.setAutoDraw(True)
        craving.setAutoDraw(True)
        win.flip()
        core.wait(5.0)
        # TODO get input from button box

        #4 2 second fixation cross
        fixation.setAutoDraw(True)  # automatically draw every frame
        win.flip()
        core.wait(2.0)
        fixation.setAutoDraw(False)
        #5 Four cycles of taste delivery (10 sec each, screen that says 'taste delivery') and swallow (2 sec each, screen that says 'swallow')- total 48 sec
        ser.write('dia26.59')
        for n in range(4):
            taste_delivery.setAutoDraw(True)
            win.flip()
            # TODO: pump 5 mL of milkshake (within 5 seconds?)
            send_cmd('phn0{0}'.format(n))
            send_cmd('funrat')
            send_cmd('rat7.5mm')
            send_cmd('vol.5')
            send_cmd('dirinf')

            core.wait(10.0)
            taste_delivery.setAutoDraw(False)
            swallow.setAutoDraw(True)
            win.flip()
            core.wait(2.0)
            swallow.setAutoDraw(False)
        #6 10 sec milkshake image
        milkshake.setAutoDraw(True)
        win.flip()
        core.wait(10.0)
        #7 5 sec milkshake pic with craving scale below
        milkshake.setAutoDraw(True)
        craving.setAutoDraw(True)
        win.flip()
        core.wait(5.0)
        # TODO get input from button box

        #8 60 sec screen that counts down and tells participant to administer crave crush/placebo
        countdown = 60
        while countdown > 0:
            administer_crave_crush.setAutoDraw(True)
            counter = visual.TextStim(win, text='{0} seconds'.format(countdown))
            counter.setAutoDraw(True)
            win.flip()
            core.wait(60.0)
            countdown = countdown - 1

        # not_done = False
        #9 180 second blank screen for the crave crush/placebo to melt
        core.wait(180.0)
        # REPEAT 1-7

# "%.1fs  %i/20" % (40 - loopClock.getTime(), trialPairNumber)
run_block()
