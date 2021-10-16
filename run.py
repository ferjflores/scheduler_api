from datetime import datetime

from dateutil.parser import parse, ParserError
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

appointments = []


@app.route('/api/user/<user_id>/')
def get_appointments(user_id):
    user_appointments = []
    for appointment in appointments:
        if appointment['user_id'] == user_id:
            del appointment['user_id']
            user_appointments.append(appointment)
    return jsonify(user_appointments)


@app.route('/api/appointment/', methods=["POST"])
def create_appointment():
    try:
        input_data = request.get_json(force=True)
    except BadRequest:
        return "No data", 400

    try:
        user_id = input_data['user_id']
    except KeyError:
        return 'Not user_id', 400

    try:
        requested_date = input_data['requested_date']
    except KeyError:
        return 'Not requested date specified', 400

    try:
        requested_date = parse(requested_date)
    except (ParserError, OverflowError):
        return "Requested date is unknown format or not a datetime string", 400

    if requested_date < datetime.now():
        return "Requested date is in the past", 400

    appointment = add_appointment(user_id, requested_date)
    if appointment:
        return jsonify(appointment)
    else:
        return f'This user_id already have an appointment for the date: {requested_date.date()}', 409


def add_appointment(user_id, requested_date):
    date = requested_date.strftime('%Y-%m-%d')
    for appointment in appointments:
        if appointment['date'] == date and appointment['user_id'] == user_id:
            return False
    new_appointment = {
        'user_id': user_id,
        'date': date,
        'time': convert_time(requested_date)
    }
    appointments.append(new_appointment)
    return new_appointment


def convert_time(date):
    time = date.time()
    hour = time.hour
    minutes = time.minute
    if 0 < minutes < 30:
        minutes = 30
    elif minutes > 30:
        minutes = 0
        hour += 1
    return f'{hour:02}:{minutes:02}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')