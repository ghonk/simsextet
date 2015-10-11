"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    __  __ __   ___    ___    ___   ______   ___    ___    ___  
   /  ]|  |  | /   \  /   \  /   \ |      | /   \  /   \  /   \ 
  /  / |  |  ||     ||     ||     ||      ||     ||     ||     |
 /  /  |  _  ||  O  ||  O  ||  O  ||_|  |_||  O  ||  O  ||  O  |
/   \_ |  |  ||     ||     ||     |  |  |  |     ||     ||     |
\     ||  |  ||     ||     ||     |  |  |  |     ||     ||     |
 \____||__|__| \___/  \___/  \___/   |__|   \___/  \___/  \___/  aka Sextet_Sim
                                                                
This experiment presents participants with trials consisting of 
six words: a base word, a thematic associate, a taxonomic 
co-category member, and 3 unrelated words. Participants' goal is
to use the mouse to select the two words that are most similar. 
Word Choice (Accuracy) and Reaction Time are collected as DVs  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
__author__  = "g_honk"
__credits__ = "n_conaway"
__status__  = "prototype/pilot"
__license__ = "GPL"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from psychopy import visual, event, core
from socket   import gethostname
from time     import strftime
from os       import getcwd, listdir, path, system
import numpy  as np	 
import random as rnd
from misc     import *
import sys
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Experiment Settings
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

experiment_name = "choootooo"
conditions   = [1,2]
window_color = [1,1,1]
font_color   = [-1,-1,-1]
text_font    = "Consolas"
text_size    = 22

# Set up interface
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Get subject information and materials
if sys.platform=='darwin':
    checkdirectory(getcwd() + '/subjects/')

    # Get subject information
    [subject_number,condition,subject_file] = getsubjectinfo(
        experiment_name,conditions,getcwd() + '/subjects/')
    
    # Get materials list
    trial_materials = np.genfromtxt(
    	getcwd()+"\\materials\\stimuli.csv",delimiter=",",dtype="str").astype(str)

else:
    checkdirectory(getcwd() + '\\subjects\\')

    # Get subject information
    [subject_number,condition,subject_file] = getsubjectinfo(
        experiment_name,conditions,getcwd() + '\\subjects\\')

    # Get materials list
    trial_materials = np.genfromtxt(
    	getcwd()+"\\materials\\stimuli.csv",delimiter=",",dtype="str").astype(str)

trial_materials = trial_materials.tolist()
item_key = ['BASE','TAXONOMIC','THEMATIC','UNRELATED','UNRELATED','UNRELATED']

# Create window and set logging option
if gethostname() not in ['klab1','klab2','klab3']:
    win=visual.Window([1440,900],units='pix',color = window_color, fullscr=True, screen = 1)

else:
    win=visual.Window([1440,900],units='pix', color = window_color, fullscr = True)
    checkdirectory(getcwd() + '\\logfiles\\')
    log_file=getcwd()+ '\\logfiles\\' + str(subject_number)+ '-logfile.txt'
    while path.exists(log_file):
       log_file=log_file+'_dupe.txt'
    log_file=open(log_file,'w')
    sys.stdout=log_file
    sys.stderr=log_file

# Define the mouse and timer
cursor = event.Mouse(visible = True, newPos = None, win = win)
timer = core.Clock()

# Get current date and time
current_time = strftime("%a, %d %b %Y %X")

# Get instructions
from instructs import *
instructions = visual.TextStim(win, text = '', wrapWidth = 900,
	color = font_color, font = text_font, height = text_size)
fix_cross = visual.TextStim(win, text = '+', color = font_color, 
	font = text_font, height = text_size, pos = [0,0])


# Start logging info
print '\n SUBJECT INFORMATION:'
print ['ID: ', subject_number]
print ['condition: ', condition]
print ['Data file: ', subject_file]
print ['Run Time: ', current_time]
print '\n'
print ['----- Materials ------']
rnd.shuffle(trial_materials)
for i in trial_materials:
	print i

subject_data = [[current_time], str(subject_number)]

# Start the experiment, display instructions
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if condition == 1:
	instructions.setText(cond1_instructs)
else:
	instructions.setText(cond2_instructs)

instructions.setText(cond_instructs)

instructions.draw()
win.flip()
event.waitKeys()

instructions.setText(init2_instructs)
instructions.draw()
win.flip()
event.waitKeys()

# Set up display
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
buttons     = []
button_text = []
button_pos  = [[-210,0],[-130,125],[130,125],[210,0],[130,-125],[-130,-125]]

# Make buttons
for idx in range(0,6):
	# Buttons
	buttons.append(visual.Rect(win, width = 170, height = 75, fillColor = [.8,.8,.8],
		lineColor = [-1,-1,-1]))
	buttons[idx].setPos(button_pos[idx])
	# Text labels
	button_text.append(visual.TextStim(win, text = '', height = text_size,
		font = text_font, color = font_color, pos = button_pos[idx]))

# Make other interface content
# Conf button
conf_button = visual.Rect(win, width = 150, height = 75, fillColor = [.8,.8,.8],
		lineColor = [-1,-1,-1], pos = [0,-275])
conf_cover = visual.Rect(win, width = 151, height = 76, fillColor = [1,1,1],
		lineColor = [1,1,1], pos = [0,-275])
conf_text = visual.TextStim(win, text = 'CONFIRM', height = text_size,
		font = text_font, color = font_color, pos = [0,-275])

# Trial instructs
trial_ins = visual.TextStim(win, text = '', height = text_size,
		wrapWidth = 900, font = text_font, color = font_color, pos = [0,-240])
if condition == 1:
	trial_ins.setText(trial_instructs_1)
else:
	trial_ins.setText(trial_instructs_2)

trial_ins.setText(trial_instructs)

# Run Trials
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

for trial in trial_materials:
	idx_list = range(0,6)
	rnd.shuffle(idx_list)
	trial_list = [trial[i] for i in idx_list]

	for idx in idx_list:
		button_text[idx_list.index(idx)].setText(trial[idx])
	
	[key_responses, all_responses, rts] = trial_mgr(win, cursor, timer, 
		buttons, button_text, trial_list, fix_cross, conf_button, conf_text, 
		conf_cover, trial_ins)

	current_trial = [subject_number, (trial_materials.index(trial) + 1), trial, 
			         key_responses, item_key[trial.index(key_responses[0])],
			         item_key[trial.index(key_responses[1])], sum(rts), 
			         all_responses, rts]

	subject_data.append(current_trial)
	writefile(subject_file, subject_data, ',')


	print ''
	print [' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ']
	print ['   Trial Number: ', trial_materials.index(trial) + 1]
	print [' Trial Concepts: ', trial]
	print ['     All Clicks: ', all_responses]
	print ['        All RTs: ', rts]
	print [' Final Response: ', key_responses]
	print ['Response 1 Type: ', item_key[trial.index(key_responses[0])]]
	print ['Response 2 Type: ', item_key[trial.index(key_responses[1])]]
	print [' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ']
	print ''

	for idx in range(0,6):
		buttons[idx].setFillColor([.8,.8,.8])


# Wrap it up
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

instructions.setText(end_instructs)
instructions.draw()
win.flip()
event.waitKeys()

print '\nExperiment completed'
if gethostname() in ['klab1','klab2','klab3']:
    copy2db(subject_file,experiment_name)
    logfile.close()
    os.system("TASKKILL /F /IM pythonw.exe")











