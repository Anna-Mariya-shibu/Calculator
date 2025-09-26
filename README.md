

````markdown
# Flask Calculator

A simple web-based calculator built using Flask. This app allows users to perform basic arithmetic operations like addition, subtraction, multiplication, and division.

---

## Features

- User-friendly interface with clean and modern styling
- Supports decimal inputs
- Basic operations: Addition, Subtraction, Multiplication, and Division
- Handles division by zero gracefully

---

## Requirements

- Python 3.x
- Flask

---

## Installation

1. Clone this repository or download the source code.

```bash
git clone https://github.com/your-username/flask-calculator.git
cd flask-calculator
````

2. (Optional but recommended) Create a virtual environment and activate it:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install Flask:

```bash
pip install flask
```

---

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your browser and go to:

```
http://127.0.0.1:5000/
```

3. Use the calculator interface to input numbers, select an operation, and view the result.

---

## File Structure

```
/project-root
  ├── app.py            # Flask application script
  ├── templates/
      └── hello.html    # HTML template for the calculator UI
  └── README.md         # This file
```

---

## Notes

* The form performs server-side calculation and displays the result without page refresh using Flask templating.
* Division by zero is handled with an error message.

---

## License

This project is open source and free to use.

---

