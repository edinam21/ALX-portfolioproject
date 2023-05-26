from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__, template_folder='templates')


# Load initial data from JSON files

# Load user data from JSON file
with open(r'C:\PORTFOLIO PROJECT\data\users.json') as f:
    users = json.load(f)

# Rest of the code...


with open (r'C:\PORTFOLIO PROJECT\data\expenses.json') as f:
    expenses = json.load(f)

with open (r'C:\PORTFOLIO PROJECT\data\budget.json')as f:
    budgets = json.load(f)


# Home page
@app.route('/')
def index():
    return render_template('index.html')

# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already taken
        if username in users:
            return render_template('register.html', error='Username already taken')

        # Register the user
        users[username] = password

        # Save the updated users data
        with open('data/users.json', 'w') as f:
            json.dump(users, f)

        return redirect(url_for('login'))

    return render_template('register.html')


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password match
        if username in users and users[username] == password:
            return redirect(url_for('expense'))

        return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


# Expense tracking
@app.route('/expense', methods=['GET', 'POST'])
def expense():
    if request.method == 'POST':
        category = request.form['category']
        amount = float(request.form['amount'])
        description = request.form['description']

        # Create a new expense entry
        new_expense = {
            'category': category,
            'amount': amount,
            'description': description
        }

        expenses.append(new_expense)

        # Save the updated expenses data
        with open('data/expenses.json', 'w') as f:
            json.dump(expenses, f)

        return redirect(url_for('expense'))

    return render_template('expense.html', expenses=expenses)


# Budget management
@app.route('/budget', methods=['GET', 'POST'])
def budget():
    if request.method == 'POST':
        category = request.form['category']
        limit = float(request.form['limit'])

        # Create a new budget entry
        new_budget = {
            'category': category,
            'limit': limit
        }

        budgets.append(new_budget)

        # Save the updated budgets data
        with open('data/budgets.json', 'w') as f:
            json.dump(budgets, f)

        return redirect(url_for('budget'))

    return render_template('budget.html', budgets=budgets)


if __name__ == '__main__':
    app.run(debug=True)
