import time
import sys
import os
import pyscreenshot as ImageGrab
from pykeyboard import PyKeyboard

WEAPON_NAME = "survivalch"
keyboard = PyKeyboard()

output_parent = '../output/' + WEAPON_NAME
try:
    if not os.path.exists(output_parent):
        os.makedirs(output_parent)
except OSError as e:
    print "FAILED TO CREATE OUTPUT FOLDER"
    sys.exit(1)

for i in range(1, 10):

    output_path = "../output/{0}/{1}.png".format(WEAPON_NAME, i)
    keyboard.press_key(keyboard.function_keys[11])

    im = ImageGrab.grab()
    im.save(output_path)
    print "Took pattern: " + str(i)
    time.sleep(1.5)
