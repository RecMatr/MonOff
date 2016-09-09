'''
	Title: MonOff
	Coder: RecMatr
	Version: 0.2
	Date: 07.07.2014
	Reason: When my video would go off before bed, sometimes the screen would be left on all night. 
			I decided to make something simple to specify a length of time before turning the monitor off.
			(and to learn since I am a noob.)'''
#For sleep and Windows control (if anyone knows of a multi-platform way to accomplish this, let me know.)
import time, win32gui, win32con
#For pretty bright green
from colorama import Fore, init, Style
init()
print(Fore.GREEN + Style.BRIGHT + '				  MonOff')
#inputs string to n
n = input('	       How many minutes until your monitor turns off?:  ')
#t converts n to integer 
t = int(n)
#Primary function armed.
def monoff():
	#Since sleep has an upper limit (as it was spitting errors at me for excessively high values), I decided to do t in minutes with while.
	i = 0
	#Simple incremental loop.
	while i < t:
		time.sleep(60)
		i = i + 1
		cd = t - i
		print('	               ', cd, 'minute(s) remaining.')
	#Variable for setting state of the display
	SC_MONITORPOWER = 0xF170
	''' Sends message, with a timeout option of 15 seconds (probably overkill), to broadcast to all windows that the display is to be set to '2' (which is off)
		If timeout is reached, app is considered hung and exits.
		More info here: http://msdn.microsoft.com/en-us/library/windows/desktop/ms644952%28v=vs.85%29.aspx '''
	win32gui.SendMessageTimeout(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2, 0x0002, 15000)
#Activate!
monoff()
