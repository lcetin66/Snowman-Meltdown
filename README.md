# Snowman Meltdown ⛄️🔥

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Game Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

Welcome to **Snowman Meltdown**, a thrilling text-based word guessing game written in Python! Can you guess the secret word before your snowman friend completely melts under the pressure?

---

## 📂 Project Structure

Here is an overview of the project's layout:

```text
Snowman-Meltdown/
├── ascii_art.py      # Contains the visual representations of the snowman's stages
├── game_logic.py     # Main engine of the game (word selection, guess validation, loops)
├── snowman.py        # Entry point for the game
├── .gitignore        # Git ignore rules
└── README.md         # You are here!
```

---

## ⚙️ Requirements

This game is designed to run on **Python 3.8+**. It uses standard Python libraries, so no additional installations are strictly required to start playing immediately.

**Standard Libraries used:**
- `random`: For secret word selection.

---

## 🚀 Installation & Play

Follow these steps to get the game running on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lcetin66/Snowman-Meltdown.git
   cd Snowman-Meltdown
   ```

2. **Start the game:**
   ```bash
   python snowman.py
   ```

---

## 🎮 How to Play

1. **Start the game**: Launch the script using Python.
2. **Guess a Letter**: Enter a single letter when prompted.
3. **Correct Guess**: If the letter is in the word, it will be revealed!
4. **Incorrect Guess**: If it's not, your snowman will start to melt, progressing through its visual stages.
5. **Winning**: Reveal all the letters of the hidden word before the snowman has completely disappeared.
6. **Losing**: If your snowman melts completely, it's game over!
7. **Play Again**: After the game ends, you will be prompted to try again.

---

## 🎨 Visuals

The game features dynamic ASCII art that visually changes as you make mistakes. Keep an eye on the snowman!

```text
      ___  
     /___\ 
     (o o) 
     ( : ) 
     ( : )
    (  :  ) 
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for new words, features, or UI improvements.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) page for details.

Enjoy the meltdown! ❄️🔥
