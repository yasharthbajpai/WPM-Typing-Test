
# Speed Typing Test

## Description
The **Speed Typing Test** is a terminal-based game that measures your typing speed in words per minute (WPM). The game displays a randomly selected text for you to type, providing real-time feedback on accuracy and speed. It's a fun way to practice typing and improve your skills!

## Features
- Randomly loads a text snippet from a file (`test.txt`) for typing.
- Real-time WPM calculation based on typing speed and elapsed time.
- Color-coded feedback:
  - **Green** for correct characters.
  - **Red** for incorrect characters.
- Option to exit the test at any time using the **ESC** key.
- Backspace support for correcting mistakes.

## How to Play
1. Run the script in your terminal.
2. Follow the on-screen instructions to start the typing test.
3. Type the displayed text as quickly and accurately as possible.
4. View your WPM score upon completion.

## Installation
### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone this repository or download the script file.
2. Ensure you have a `test.txt` file in the same directory containing text snippets (one per line).
3. Run the script using Python:
   ```
   python3 speed_typing_test.py
   ```

## Dependencies
This project uses the following Python modules:
- `curses` (for terminal-based UI)
- `random` (for selecting random text)
- `time` (for tracking elapsed time)

## Game Rules
- Type the displayed text as accurately as possible.
- Use **Backspace** to correct mistakes.
- The game ends when you type the entire text correctly.
- Press **ESC** to exit at any time.



## Author
**Yasharth Bajpai**

## License
This project is licensed under the [Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) license.

---

Enjoy improving your typing skills with this fun and interactive game!
