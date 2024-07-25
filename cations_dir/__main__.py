"""
┏┓   •
┃ ┏┓╋┓┏┓┏┓┏
┗┛┗┻┗┗┗┛┛┗┛
CATIONS by Alcryst
Version 1.0.1

See LICENSE.txt for license info.
"""

"""
If you want to contribute to this open source project feel free to do so.
Also please stick to the following guidelines which are not required but just preferences:
- add comments wherever helpful / don't delete comments
- don't add a bunch of random libraries/obscure functions unless they can be used to significantly improve some functionality
- prettifying / adding more info is always helpful :)
- when changing/adding features in the application, consider add them to the config menu if applicable
- be respectful and have fun
"""

import blessed
import time
import datetime
import os

def loadConfig():
	#try:
		f = open(os.path.dirname(os.path.abspath(__file__)) + "/user_data/config.txt", "r")
		# configlist = []
		# for line in f:
		# 	configlist.append(line.rstrip("\n"))
		# f.close()

		# return configlist
		configStr = ""
		for line in f:
			configStr = configStr + line
		f.close()
		configStr.rstrip()
		return configStr
	#except:
	#	return 1

def writeConfig(configStr):
	try:
		f = open(os.path.dirname(os.path.abspath(__file__)) + "/user_data/config.txt", "w")
		# for item in configlist:
		# 	f.write(item + "\n")
		# f.close()
		f.write(configStr)
		f.close()
		return 0
	except:
		return 1

"""
def loadConfigOpts():

	configOpts = [
		["Default", "Sleek", "Text-Only"],
		["Standout", "Invert", "None"],
		["Yes", "No"]
	]

	return configOpts

	# current config options:
	# logo style:
	# default/sleek/text-only
	# streak style:
	# standout/invert/none
	# show Anion the Cat (in the lower left corner):
	# yes/no
	# todo: add color scheme?

def editConfig():

	NUM_CONFIG_OPTIONS = 3
	CONFIG_OPTIONS = loadConfigOpts()
	# see loadConfig() for config options.

	configlist = loadConfig()
	if (configlist == 1):
		with term.location(y=term.height // 2):
			print(term.center("Error loading config file. Check if user_data/config.txt exists."))
			return 1
	inp = ''
	index = -1
	maxInd = NUM_CONFIG_OPTIONS - 1
	navList = [""] * NUM_CONFIG_OPTIONS

	while ((inp != 'q') and (inp != 'p')):

		# REFRESH SCREEN

		print(term.clear, end='')
		print(term.home + term.center(term.bold("CONFIG SETTINGS")) + term.normal)
		print(term.center("(Use Up/Down to move, Left/Right to select.)") + "\n")

		navList = ["  "] * NUM_CONFIG_OPTIONS
		if (index > -1):
			navList[index] = "> "

		print(term.center(navList[0] + "Logo Style: " + configlist[0]))
		print(term.center(navList[1] + "Streak Style: " + configlist[1]))
		print(term.center(navList[2] + "Show Anion the Cat: " + configlist[2]))
		print(term.center(term.standout("Press Q to save and quit or P to quit without saving.")) + term.normal)

		# HANDLE INPUT

		inp = term.inkey()

		if inp.is_sequence:
			if (inp.name == "KEY_DOWN"):
				index += 1
				if (index > maxInd): index = -1
				print(term.clear, end='')
			elif (inp.name == "KEY_UP"):
				index -= 1
				if (index < -1): index = maxInd
				print(term.clear, end='')

			elif((inp.name == "KEY_RIGHT") or (inp.name == "KEY_LEFT")):
				dir = -1
				if(inp.name == "KEY_RIGHT"):
					dir = 1

				if (index == 0):


				print(term.clear, end='')


	if (inp == 'q'):
		ok = writeConfig(configlist)
		if not ok: # heh
			with term.location(y=term.height // 2):
				print(term.center("Error saving to config file. Check if user_data/config.txt exists."))
				return 1
"""

def loadIons():
	# add each ion & details to ionlist as its own list
	try:
		f = open(os.path.dirname(os.path.abspath(__file__)) + "/user_data/ions.txt", "r")
		ionlist = []
		for line in f:
			chunks = line.rstrip("\n").split()
			ionlist.append(chunks)
		f.close()

		if (ionlist == [[]]):
			return []

		for ion in ionlist:
			ion[0] = ion[0].replace("_", " ")

		return ionlist
		# formatting:
		# [ion_name ion_streak last_compl_day_in_iso]
	except:
		return 1

def writeIons(ionlist):
	try:
		f = open(os.path.dirname(os.path.abspath(__file__)) + "/user_data/ions.txt", "w")
		for ion in ionlist:
			# i know hardcoding is bad practice but it's surely not that bad
			f.write(ion[0].replace(" ", "_") + " " + str(ion[1]) + " " + str(ion[2]) + "\n")
		f.close()
		return 0
	except:
		return 1

def displayControls(term):
	print(term.clear, end='')
	print(term.home + term.center(term.bold("CONTROLS")) + term.normal)
	print(term.center("C = show controls menu"))
	print(term.center("Up/Left = go back a page"))
	print(term.center("Down/Right = go forward a page"))
	print(term.center("N = new ion"))
	print(term.center("I = complete current ion"))
	print(term.center("M = modify current ion name"))
	print(term.center("X = delete current ion"))
	print(term.center("Q = save and quit"))
	print(term.center("P = quit without saving"))
	# print(term.center("E = edit configuration settings"))
	print(term.center("A = show/hide Anion the Cat ^w^"))
	print(term.center(term.standout("Press anything to exit this menu.")) + term.normal)
	term.inkey()
	print(term.clear, end='')

def deleteCurrIon(term, ionlist, index):
	with term.location(y=term.height // 2):
		print(term.center(term.standout("Delete this ion and all its progress? You cannot recover it once you save.")) + term.normal)
		print(term.center(term.standout("Press X again to confirm, or press C to cancel.")) + term.normal)
		ans = term.inkey(timeout=10)
		if (ans and (ans.lower() == "x")):
			del ionlist[index]
			print(term.clear + term.center("Successfully deleted."))
			print(term.center("(You can quit without saving to recover your ion.)"))

def createIon(term, ionlist): # there's an issue where term.cbreak() hides input so i'm just working
	# around that by putting the operation before save/quit.
	# see the big comment block in the while loop for more info.
	try:
		with term.location(y=term.height // 2):
			print(term.center("Enter the name of the ion you would like to create (WILL AUTOSAVE/QUIT):"))
	except:
		return 1
	with term.location(y=(term.height // 2) + 1, x=term.width // 3): # yes this breaks if the terminal height is extremely tiny but is that really gonna happen??
		newIon = ["", "0", "0"]
		newIon[0] = str(input())
		ionlist.append(newIon)

def modifyIonName(term, ionlist, index): # see createIon()
	try:
		with term.location(y=term.height // 2):
			print(term.center("Enter the new name of this ion (WILL AUTOSAVE/QUIT):"))
	except:
		return 1
	with term.location(y=(term.height // 2) + 1, x=term.width // 3):
		ionlist[index][0] = str(input())

def completeIon(term, ionlist, index):
	if (ionlist[index][2] != datetime.date.today().isoformat()):
		streak = int(ionlist[index][1]) + 1
		ionlist[index][1] = str(streak)
		oldDate = str(ionlist[index][2])
		ionlist[index][2] = datetime.date.today().isoformat()
		with (term.location(y=term.height // 2)):
			match (streak):
				case 1:
					if (oldDate == "0"):
						print(term.center(term.bold("Nice work getting started with your good habit!")) + term.normal)
					else:
						print(term.center(term.bold("Great job getting back on track! Keep up the momentum!")) + term.normal)
				case 2:
					print(term.center(term.bold("Two days in a row! You've got this!")) + term.normal)
				case 3:
					print(term.center(term.bold("That's a three-day streak! Keep on going!")) + term.normal)
				case 5:
					print(term.center(term.bold("You've made it to five days now! Great work!")) + term.normal)
				case 7:
					print(term.center(term.bold("You're at one whole week! Amazing!")) + term.normal)
				case 10:
					print(term.center(term.bold("Ten days in a row! Keep being awesome!")) + term.normal)
				case 14:
					print(term.center(term.bold("Two full weeks done! I believe in you!")) + term.normal)
				case 21:
					print(term.center(term.bold("You've kept it up for three weeks! Keep on moving forward!")) + term.normal)
				case 28:
					print(term.center(term.bold("One whole month! I'm proud of you. Continue doing great things!")) + term.normal)
				case 50:
					print(term.center(term.bold("Fifty days! Can you make it to 100? I believe in you!")) + term.normal)
				case 100:
					print(term.center(term.bold("Triple digits! You truly have inspiring dedication!")) + term.normal)
				case 365:
					print(term.center(term.bold("It's your streak's one-year anniversary! I'm proud of you!")) + term.normal)
				case 1000:
					print(term.center(term.bold("Woah... 1000 days?! I'm awestruck! Keep it up!!")) + term.normal)
				case _:
					print(term.center(term.bold("Congratulations on completing this ion today! See you tomorrow!")) + term.normal)
		return 1
	return 0

def checkStreak(ionlist):
	# returns vector giving:
	# index of lost streaks, difference in days
	today = datetime.date.fromisoformat(datetime.date.today().isoformat())
	lostStreakIndices = []
	for index in range(0, len(ionlist)):
		if (ionlist[index][2] == "0"): continue # never started before
		if (ionlist[index][1] == "0"): continue # streak not active (incl. never started)
		# ik the first statement is redundant
		difference = (datetime.date.fromisoformat(ionlist[index][2]) - today).days
		if (difference < -1):
			ionlist[index][1] = "0"
			lostStreakIndices.append([index, difference])
	return lostStreakIndices

def drawLn(term):
	print(term.truncate(term.center("––––––––––––––––––––––––––––––––––––––––––––––––––"), term.width))

def drawLogo(term, type):
	match (type):
		case 1:
			print(term.center(term.bold("Welcome to CATIONS.")))
		case 2:
			print(term.center(term.bold("┏┓   •     ")))
			print(term.center(term.bold("┃ ┏┓╋┓┏┓┏┓┏")))
			print(term.center(term.bold("┗┛┗┻┗┗┗┛┛┗┛")))
		case _: # same as case 1
			print(term.center(term.bold("Welcome to CATIONS.")))

def drawAnion(term, face, size):
	if (size == "small"):
		with term.location(y=term.height-8, x=0):
			match (face):
				case 1:
					print("  ██    █")
					print("  █ █  █ █")
					print("  █  ██   █")
					print(" █        █")
					print("█   █   █  █")
					print("█   █   █  █")
					print("█          █")
					print("█          █", end='')
				case 2:
					print("▒▒██▒▒▒▒█▒▒▒")
					print("▒▒█▒█▒▒█▒█▒▒")
					print("░░█░░██░░░█░")
					print(" █        █ ")
					print("█   ██  ██ █")
					print("█   ░    ░ █")
					print("█   ░    ░ █")
					print("█          █", end='')
				case 3:
					print("  ██    █")
					print("  █ █  █ █")
					print("  █  ██   █")
					print(" █        █")
					print("█   █   █  █")
					print("█  █ █ █ █ █")
					print("█          █")
					print("█          █", end='')
				case 4:
					print("  ██    █")
					print("  █ █  █ █")
					print("  █  ██   █")
					print(" █  ▄   ▄ █")
					print("█  ▐ ▌ ▐ ▌ █")
					print("█   ▀   ▀  █")
					print("█  ▐▀▀▀▀▀▌ █")
					print("█  ▐▄▄▄▄▄▌ █", end='')

	elif (size == "big"): # unused right now
		with term.location(y=term.height-11, x=0):
			match (face):
				case 1:
					print("       ██")
					print("        █████")
					print(" ████    █   ██")
					print(" █  ████ █    ██")
					print(" ██    ███     ██")
					print("  █          █  ███")
					print("  ██     █   █    ██")
					print("   █     █         █")
					print("  ██        █  █   ██")
					print(" ██     █  █ ██     █")
					print("██       ██         ██")
					print("█                    █", end='')
				case 2:
					print("       ██         ██")
					print("        █████    █ █")
					print(" ████    █   ██    █")
					print(" █  ████ █    ██   ███")
					print(" ██    ███     ██  ██")
					print("  █          █  ███")
					print("  ██   ███   █    ██")
					print("   █     █         █")
					print("  ██        █  █   ██")
					print(" ██     █  █ ██     █")
					print("██       ██         ██")
					print("█                    █", end='')


def main():
	term = blessed.Terminal()
	TODAY = datetime.date.today().isoformat()
	configStr = loadConfig()

	# anion = configList[0]
	anion = ("True" == configStr) # this took me a stackoverflow search to figure out ._.
	completedToday = False

	with(term.fullscreen()):
		print(term.clear, end='')
		with term.location(y=term.height // 3):
			if (term.height > 8):
				drawLogo(term, 2)
			else:
				drawLogo(term, 1)
			print(term.center(term.bold("Press enter to begin.")) + term.normal)
			term.inkey()

		print(term.clear, end='')

		if (term.height < 12):
			with term.location(y=term.height // 2):
				print(term.center("Your terminal window may be too small to display this application without errors."))
				print(term.center("It is recommended to resize your window to at least 12 lines high before continuing."))
				print(term.center("[Press enter to continue.]"))
				term.inkey()

			print(term.clear, end='')

		ionlist = loadIons()
		if (ionlist == 1):
			print("Data could not be read due to an error. Check if the file user_data/ions.txt exists.")
			print("Auto-exiting soon.")
			time.sleep(5)
			quit()

		if not (ionlist):
			print(term.home + term.center("You don't seem to have any ions yet."))
			print(term.center("Let's try making a new ion."))
			print(term.center("Enter the name of your ion: "))
			newIon = ["", "0", "0"]
			with term.location(x=term.width // 3, y=term.height // 2):
				newIon[0] = str(input())
			print(term.clear + term.home + term.center(term.bold("Creating the ion: " + newIon[0])) + term.normal)
			print(term.center("After each use of CATIONS make sure to save and quit so that your data is saved."))
			print(term.center("When you next run CATIONS your ion will appear on your dashboard."))
			print(term.center(term.bold("Press enter to save and quit now.")))
			term.inkey()
			print(term.normal + term.clear, end='')
			ionlist.append(newIon)
			writeIons(ionlist)
		else:
			with term.cbreak():
				pgNum = -1
				maxPg = len(ionlist) - 1
				inp = ''
				firstLogin = True
				while (inp.lower() != 'q') and (inp.lower() != 'm') and (inp.lower() != 'n'):

					# REFRESH SCREEN

					print(term.home + "Pg " + str(pgNum + 1))
					if (pgNum == -1):
						completedToday = False
						print(term.center("Welcome to your dashboard."))
						print(term.center("You currently have " + str(len(ionlist)) + " ion(s)."))
						print(term.center("Check controls by pressing C."))
						drawLn(term)
						if (firstLogin):
							firstLogin = False
							lostStreakIndices = checkStreak(ionlist)
							if (lostStreakIndices):
								if (len(lostStreakIndices) > 2):
									print(term.center("You've lost your streak for multiple ions!"))
								elif (len(lostStreakIndices) == 2):
									print(term.center(
										"You've lost your streak for these ions: \"" + ionlist[lostStreakIndices[0][0]][0]
										+ "\" and \"" + ionlist[lostStreakIndices[1][0]][0] + "\"!"))
								else:
									print(term.center(
										"You've lost your streak for the ion: \"" + ionlist[lostStreakIndices[0][0]][
											0] + "\"!"))

								if (lostStreakIndices[0][1] == -2):
									print(term.center("Make sure to never miss twice! You can do it!"))
								else:
									print(term.center("Good habits are built through persistence! You can do it!"))
					else:
						print(term.center(term.bold(ionlist[pgNum][0])))
						if (ionlist[pgNum][2] == TODAY):
							completedToday = True
							print(term.center(term.bold_standout("Streak: " + str(ionlist[pgNum][1]))) + term.normal)
							print(term.center("Last completed today!"))
						else:
							completedToday = False
							print(term.center(term.bold("Streak: " + str(ionlist[pgNum][1]))) + term.normal)
							if (ionlist[pgNum][2] == "0"):
								print(term.center("Not started yet"))
							else:
								print(term.center("Last completed on: " + str(ionlist[pgNum][2])))
						drawLn(term)

					if (pgNum == maxPg):
						# print(term.move_y(term.height - 2) + term.center(term.truncate("--> Dashboard", term.width)))
						print(term.center(term.truncate("--> Dashboard", term.width)))
					else:
						# print(term.move_y(term.height - 2) + term.center(term.truncate("--> " + ionlist[pgNum + 1][0], term.width)))
						print(term.center(term.truncate("--> " + ionlist[pgNum + 1][0], term.width)))

					if ((term.height > 15) and anion):
						if (lostStreakIndices):
							lostStreakIndices = []
							drawAnion(term, 2, "small")
						elif (completedToday):
							drawAnion(term, 3, "small")
						else:
							drawAnion(term, 1, "small")

					# HANDLE INPUT

					inp = term.inkey()
					if inp.is_sequence:
						if ((inp.name == "KEY_DOWN") or (inp.name == "KEY_RIGHT")):
							pgNum += 1
							if (pgNum > maxPg): pgNum = -1
							print(term.clear, end='')
						elif ((inp.name == "KEY_UP") or (inp.name == "KEY_LEFT")):
							pgNum -= 1
							if (pgNum < -1): pgNum = maxPg
							print(term.clear, end='')
					else:
						inp = inp.lower()
						if (inp == 'c'):
							displayControls(term)
						elif (inp == 'a'):
							anion = not anion
						# elif (inp == 'n'):
							# createIon(term, ionlist)
							# maxPg = len(ionlist) - 1
						# 		So the dilemma we have with new/modify is that cbreak obscures input,
						# which makes typing names for new/modify difficult.
						# My solution is to treat it as a save/quit with the rename operation performed right before.
						# 		This is kind of clumsy but the only other options I can think of are working around cbreak
						# (probably difficult), keeping the input hidden (not very good), isolating the new/rename features
						# entirely from the dashboard view (annoying), using goto to skip in and out of the cbreak
						# (le "bad practice"), or creating a bigger while loop around this one without the cbreak
						# for the sole purpose of handling input operations (too complicated to implement quickly).
						# 		I suspect that when this feature gets rewritten in the code (which it probably will be at
						# some point due to the current implementation being somewhat inconvenient) that the bigger
						# while loop option will end up being the one selected. I'm still opting to use the current
						# solution as a stopgap because it's good enough for most purposes and if you want to undo
						# you can always re-rename or delete.

						# I probably should've used a multiline comment for this lol.

						elif (inp == 'i'):
							wasCompleted = completeIon(term, ionlist, pgNum)
							if (wasCompleted and anion and (term.height > 15)):
								drawAnion(term, 3, "small")
						# elif (inp == 'm'):
							# modifyIonName(term, ionlist, pgNum)
						# see the gigantic comment block above
						elif (inp == 'x'):
							deleteCurrIon(term, ionlist, pgNum)
							maxPg = len(ionlist) - 1
							if (pgNum > maxPg): pgNum = -1
						elif (inp == 'p'):
							with term.location(y=term.height // 2):
								print(term.center(term.standout("Quit without saving? You will lose any unsaved changes/progress.")) + term.normal)
								print(term.center(term.standout("Press P again to confirm, or press C to cancel.")) + term.normal)
								ans = term.inkey(timeout=10)
								if (ans and (ans.lower() == "p")):
									print(term.clear)
									quit()
						elif (inp == 'q'):
							with term.location(y=term.height // 2):
								print(term.center(term.bold("Save and quit CATIONS? Your changes/progress will be saved.")) + term.normal)
								print(term.center(term.bold("Press Q again to confirm, or press C to cancel.")) + term.normal)
								inp = term.inkey(timeout=10)

			if (inp == 'm'):
				modifyIonName(term, ionlist, pgNum)
			elif (inp == 'n'):
				createIon(term, ionlist)
			writeIons(ionlist)
			configStr = str(anion)
			writeConfig(configStr)

if __name__ == '__main__':
	main()
