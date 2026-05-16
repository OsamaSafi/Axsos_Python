# Dojo Fruit Store (Flask Web Application)

A simple and fun fruit store web application built using the **Flask** framework and **Python**, with a clean frontend styled via **Bootstrap**. This application allows users to submit an order, store their information dynamically using sessions, and view a collective real-time dashboard of all customer orders.

---

## Features

* **Session Management:** Utilizes Flask sessions to securely hold the current user's form data across routes.
* **Dynamic Visual Display:** Leverages **Jinja2** templating loops to dynamically repeat fruit images based on the specific quantities ordered.
* **Global Order Dashboard:** Stores and displays a running list of *all* customer orders submitted on the server in a single, organized view.
* **Fully Responsive UI:** Styled with Bootstrap cards and grid systems to look great on desktop and mobile screens alike.

---

## Tech Stack

* **Backend:** Python 3 & Flask Framework
* **Frontend:** HTML5, Bootstrap 4, Jinja2 Templating Engine
* **Storage:** In-memory Python Data Structures (Global List)

---

## Project Structure

```text
Dojo-Fruit-Store/
│
├── static/
│   ├── css/
│   │   └── bootstrap.css
│   └── img/
│       ├── apple.png
│       ├── raspberry.png
│       └── strawberry.png
│
├── templates/
│   ├── index.html
│   ├── fruits.html
│   └── checkout.html
│
├── server.py          # Main Flask application file
└── README.md          # Project documentation