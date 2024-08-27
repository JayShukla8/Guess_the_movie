# Mini Arcade (A CS50 Python Project)
Welcome to **Mini Arcade**, a Python project featuring a collection of three simple and fun games. This project demonstrates basic game development and interaction using Python.

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Dependencies](#dependencies)
5. [Contributing](#contributing)
6. [Acknowledgments](#acknowledgments)
7. [License](#license)
   
## Overview

Mini Arcade is a collection of three fun interactive games.
- **Rock, Paper, Scissors**: Classic game. Compete with computer.
- **Magic 8 Ball**: The infamous ball answers your questions. (make sure they are yes/no type)
- **Dad Joke Machine**: That's what it literally does. Tells you a dad joke.

## Installation

To get started with Mini Arcade, you need to have Python installed on your system. Follow these steps to set up the project:

1. **Clone the repository:**

   run in git bash:
   ```
   git clone https://github.com/JayShukla8/mini_arcade.git
   ```

3. **Navigate to project directory:**
   ```
   cd mini_arcade
   ```

4. **Install the required dependencies:**

   download the requirements.txt file from the git repo and install the dependencies using
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main program to start the arcade:
```
python project.py
```
You will see a menu with options to play Rock, Paper, Scissors, ask the Magic 8 Ball, or get a dad joke. Follow the on-screen instructions to interact with the games.

## Dependencies

The project requires the following Python packages:

- requests: For making HTTP requests to fetch dad jokes.
- pyfiglet: For creating styled text banners.
- colorama: For colored terminal text.
- pytest: For running the unit tests.

## Contributing

If you'd like to contribute to Mini Arcade, please fork the repository and create a pull request with your changes. Contributions are welcome!


## Acknowledgments

- [icanhazdadjoke](https://icanhazdadjoke.com/): For providing the API used to fetch dad jokes in the Dad Joke Machine.
- [David Malan](https://www.linkedin.com/in/malan/): For being an awesome teacher.
- [freeCodeCamp](https://www.youtube.com/c/Freecodecamp): For making the course available.

## License

MIT License

Copyright (c) 2024 Jay Shukla

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Enjoy your games! 🎮

