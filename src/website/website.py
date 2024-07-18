from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
from datetime import datetime, timedelta
import logging
import userInfo
import bookInfo
import csv
import os
from threading import Thread


app = Flask(__name__)
CORS(app, supports_credentials=True)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app.secret_key = 'super_secret_key'

passwords = userInfo.load_passwords()

# Login function
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = data.get('user')
    identity = data.get('identity')
    password = data.get('password')
    
    if identity in passwords and passwords[identity] == password:
        session['identity'] = identity
        session['name'] = user
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid identity or password'})


# Check session cookies
@app.route('/session', methods=['GET'])
def get_session():
    if 'identity' in session:
        return jsonify({'loggedIn': True, 'identity': session['identity'], 'name': session['name']})
    else:
        return jsonify({'loggedIn': False})


# Logout function
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True})


# Create new record
@app.route('/signup', methods=['POST'])
def signup():
    global passwords
    data = request.get_json()
    identity = data.get('identity')
    password = data.get('password')

    if identity in passwords:
        return jsonify({'success': False, 'message': 'Admin No. already used'})
    
    userInfo.createAcc(identity, password)
    passwords = userInfo.load_passwords()
    passwords[identity] = password
    return jsonify({'success': True, 'message': 'Account created successfully'})


# Create book reservation
@app.route('/reserve', methods=['POST'])
def reserve():
    if 'identity' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'})

    data = request.get_json()
    name = data.get('name')
    identity = session['identity']
    book_title = data.get('bookTitle')
    location = data.get('location')
    reserveTime = data.get('reserveTime')

    reserveDate = datetime.fromisoformat(reserveTime.replace('Z', '+00:00')) + timedelta(hours=8)
    dateTime = reserveDate.strftime('%Y-%m-%d %H:%M:%S')

    print(f'Reservation made by {name} ({identity}) for the book "{book_title}" at {location}, {dateTime}')
    info = name + '&' + identity
    
    booklist = bookInfo.loadBooks()

    if info not in booklist or len(booklist[info]) <= 10:
        bookInfo.addBook(info, book_title, location, dateTime)

    return jsonify({'success': True})




@app.route('/reservations', methods=['GET'])
def get_reservations():
    booklist = bookInfo.loadBooks()
    return jsonify(booklist)

'''@app.route('/fines', methods=['GET'])
def get_fines():
    getReserve('http://192.168.50.170:5001')
    fineList = userInfo.loadFine()
    return jsonify(fineList)'''

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/createAcc')
def createAcc():
    return render_template('createAcc.html')

@app.route('/browse')
def browse():
    return render_template('browse.html')

@app.route('/account')
def account():
    return render_template('account.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
