#   Created 8-09-2011
#   Ricky Savjani
#   (savjani at bcm.edu)

#import necessary packages
from distutils.core import setup
import os, matplotlib
import py2exe

#the name of your .exe file
progName = 'SweetImage.py'

#Initialize Holder Files
# preference_files = []
# app_files = []
# my_data_files=matplotlib.get_py2exe_datafiles()

#define which files you want to copy for data_files
# for files in os.listdir('C:\\Program Files\\PsychoPy2\\Lib\\site-packages\\PsychoPy-1.65.00-py2.6.egg\\psychopy\\preferences\\'):
#     f1 = 'C:\\Program Files\\PsychoPy2\\Lib\\site-packages\\PsychoPy-1.65.00-py2.6.egg\\psychopy\\preferences\\' + files
#     preference_files.append(f1)

#combine the files
# all_files = [("psychopy\\preferences", preference_files), my_data_files[0]]

#define the setup
setup(
                # console=[progName],
                # data_files = all_files,
                options = {
                    "py2exe":{
                        "skip_archive": True,
                        "optimize": 2
                    }
                }
)