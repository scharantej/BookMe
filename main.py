 
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

# Create a Flask app
app = Flask(__name__)

# Database (in-memory for simplicity)
registered_slots = []
booked_slots = []

# Landing page
@app.route('/')
def index():
    return render_template('index.html')

# Register open office slots
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        time = request.form['time']

        # Save slot information
        registered_slots.append({
            'name': name,
            'email': email,
            'date': date,
            'time': time
        })

        # Redirect to confirmation page
        return redirect(url_for('confirmation'))

    return render_template('register.html')

# Book available office slots
@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        slot_id = request.form['slot_id']

        # Update database to mark slot as booked
        booked_slots.append(registered_slots[int(slot_id)])
        registered_slots.pop(int(slot_id))

        # Redirect to confirmation page
        return redirect(url_for('confirmation'))

    return render_template('book.html', registered_slots=registered_slots)

# Confirmation page
@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

# User profile
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Edit user profile
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Update user information
        user = {'name': name, 'email': email}

        # Redirect to profile page
        return redirect(url_for('profile'))

    return render_template('edit.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
