# Tic-Tac-Toe AI Web Game

Welcome! This project is a modern, web-based Tic-Tac-Toe game where you can challenge a smart AI opponent. Built with Python Flask on the backend and sleek HTML/CSS/JavaScript on the frontend, it’s designed to be fun, responsive, and visually appealing.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Code Details](#code-details)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

This is a classic Tic-Tac-Toe game where you (playing as **X**) go head-to-head against an AI (**O**). The interface is clean and intuitive, with smooth animations, a handy instructions modal, undo functionality, and fun win celebrations. The app is fully responsive, so it works great on both desktop and mobile.

---

## Features

- **Player vs AI:** Play as X, while the AI (O) uses smart logic to challenge you.
- **Responsive UI:** Looks great on any device—desktop, tablet, or phone.
- **Glassmorphism Style:** Subtle backgrounds, gradients, and soft shadows for a modern look.
- **Animations:** Enjoy animated clicks, transitions, and lively win celebrations.
- **Undo Move:** Undo your last move (and the AI’s) before the game ends.
- **Instructions Modal:** Quick “How to Play” guide with emojis for clarity.
- **Win Celebration:** Confetti, emojis, and board animations when you win.
- **Footer:** Fun credits with links to the GitHub repo and developer portfolio.
- **No Vertical Scrolling:** Everything fits neatly on your screen.

---

## Folder Structure

Here’s a quick look at how the project is organized:

```
tic_tac_toe_ai/
│
├── templates/
│   └── index.html         # Main frontend file (HTML, CSS, JS)
│
├── __pycache__/           # Python cache (auto-generated)
│
├── ai.py                  # AI logic for the game
├── app.py                 # Flask app entry point
├── game.py                # Game state and logic
├── main.py                # Main controller (may initialize app)
├── utils.py               # Helper functions
├── README.md              # This file!
├── .gitignore             # Files/folders to ignore in git
├── 529232.png             # Project logo/image
```

---

## Installation & Setup

**Prerequisites:**

- Python 3.8+
- Flask

**Clone the repository:**

```bash
git clone https://github.com/innovatewithkishlay/Tic-Tac-Toe-AI.git
cd Tic-Tac-Toe-AI
```

**(Recommended) Create a virtual environment:**

```bash
python -m venv venv
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run the app:**

```bash
python app.py
```

**Open your browser and visit:** [http://localhost:5000](http://localhost:5000)

---

## Usage

- **Start Game:** Click on any empty cell to make your move as X.
- **Undo Move:** Hit the Undo button to revert your last move (and the AI’s), as long as the game isn’t over.
- **Restart Game:** Use the Restart button to reset the board and scores anytime.
- **How to Play:** Click the instructions button for a quick guide.
- **Win Celebration:** Win the game and enjoy the confetti and animations!

---

## Code Details

**Frontend:**

- `templates/index.html` contains all the HTML, CSS (with glassmorphism), and JavaScript for the UI, animations, and game logic.
- Fully responsive for mobile and desktop.
- Features undo, animated wins, modal instructions, and dynamic status updates.

**Backend:**

- `app.py` runs the Flask server and serves the frontend.
- `ai.py` handles the AI’s move logic (using simple heuristics to win or block).
- `game.py` manages the game state and rules.
- `utils.py` provides helper functions.
- `main.py` may act as the main entry point or orchestrator.

---

## Contribution Guidelines

Contributions are welcome! Here’s how you can help:

- **Issues & Requests:**  
    Open an issue for bugs or feature ideas. Please describe the problem or suggestion clearly.
- **Pull Requests:**  
    - Fork the repo and create a feature branch.
    - Follow the existing code style.
    - Add comments and update docs if needed.
    - Test your changes.
    - Submit a pull request with a description of your changes.
- **Code Quality:**  
    - Keep code readable and modular.
    - Don’t break existing features.
    - Enhance the UI or AI logic thoughtfully.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

Made with ☕️ and grit by **Kishlay Kumar**

- **Portfolio:** [https://kishlaykumar.onrender.com/](https://kishlaykumar.onrender.com/)
- **GitHub Repo:** [https://github.com/innovatewithkishlay/Tic-Tac-Toe-AI](https://github.com/innovatewithkishlay/Tic-Tac-Toe-AI)

Feel free to reach out for collaborations, questions, or feedback!

---

Thanks for checking out Tic-Tac-Toe AI! Have fun challenging the AI and enjoy the smooth, creative gameplay experience. 🎮🤖
