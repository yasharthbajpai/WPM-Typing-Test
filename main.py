"""
Title          : Speed Typing Test
Author         : Yasharth Bajpai
Created        : 20th January 2025
Last Modified  : 13th February 2025
Version        : 1.0

Description    : A terminal-based speed typing test game that measures typing speed 
                 in words per minute (WPM). The player types a randomly loaded text 
                 and receives feedback on accuracy and speed.

Dependencies   : 
    - Python 3.x
    - curses module
    - random module
    - time module

Usage          : Run the script to start the game. Follow prompts to:
                 1. Begin the typing test
                 2. Type the displayed text as quickly and accurately as possible
                 3. View your WPM score upon completion

Features       :
    - Randomly loads text from a file for typing
    - Real-time WPM calculation based on typing speed and elapsed time
    - Color-coded feedback for correct (green) and incorrect (red) characters
    - Option to exit the game at any time using the ESC key

Game Rules     :
    - Type the displayed text as accurately as possible
    - Backspace can be used to correct mistakes
    - The game ends when the entire text is typed correctly

License        : CC0 1.0 Universal

Copyright (c) [2025] [Yasharth Bajpai]
"""



import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
	stdscr.clear()
	stdscr.addstr("Welcome to the Speed Typing Test!")
	stdscr.addstr("\nPress any key to begin!")
	stdscr.refresh()
	stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
	stdscr.addstr(target)
	stdscr.addstr(1, 0, f"WPM: {wpm}")

	for i, char in enumerate(current):
		correct_char = target[i]
		color = curses.color_pair(1)
		if char != correct_char:
			color = curses.color_pair(2)

		stdscr.addstr(0, i, char, color)

def load_text():
	with open("test.txt", "r") as f:
		lines = f.readlines()
		return random.choice(lines).strip()

def wpm_test(stdscr):
	target_text = load_text()
	current_text = []
	wpm = 0
	start_time = time.time()
	stdscr.nodelay(True)

	while True:
		time_elapsed = max(time.time() - start_time, 1)
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

		stdscr.clear()
		display_text(stdscr, target_text, current_text, wpm)
		stdscr.refresh()

		if "".join(current_text) == target_text:
			stdscr.nodelay(False)
			break

		try:
			key = stdscr.getkey()
		except:
			continue

		if ord(key) == 27:
			break

		if key in ("KEY_BACKSPACE", '\b', "\x7f"):
			if len(current_text) > 0:
				current_text.pop()
		elif len(current_text) < len(target_text):
			current_text.append(key)


def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	start_screen(stdscr)
	while True:
		wpm_test(stdscr)
		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		key = stdscr.getkey()
		
		if ord(key) == 27:
			break

wrapper(main)