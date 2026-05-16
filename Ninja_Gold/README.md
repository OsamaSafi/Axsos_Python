# Ninja Gold Game (Flask)

A simple and interactive web-based mini-game built using **Flask** and **Python**. This project is designed to demonstrate key web development concepts such as session management, handling HTML forms, HTTP POST requests, and URL redirects.

---

## Features

* **Session Management:** Total gold and activity logs are stored inside the Flask session, ensuring data persists even when the page is refreshed.
* **Multiple Locations:** The ninja can visit 4 distinct places to gather gold (Farm, Cave, House, Casino).
* **Risk/Reward Mechanic:** The Casino offers an exciting twist where the ninja can either win or lose up to 50 gold.
* **Live Activity Log:** Displays a history of past activities sorted from newest to oldest, color-coding gains in green and losses in red.
* **Game Reset:** A dedicated button allows players to clear the session data and start the game over from scratch.

---

## Technologies Used

* **Backend:** Python 3.x, Flask Framework
* **Frontend:** HTML5, CSS3, Jinja2 Templating Engine

---

## Project Structure

The project follows the standard file structure required for Flask applications:

```text
ninja_gold/
│
├── app.py             # Main application logic and routing (Backend)
└── templates/            # HTML views directory
    └── index.html        # Main game interface and activity log (Frontend)