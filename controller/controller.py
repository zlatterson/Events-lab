from flask import render_template, request

from app import app
from models.event_list import *
from models.event import Event


@app.route("/events")
def index():
    return render_template("index.html", title="Home", events=events)


@app.route("/events", methods=["POST"])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["title"]
    event_num_guests = request.form["Number of Guests"]
    event_location = request.form["location"]
    event_description = request.form["description"]
    event_done = False
    if "done" in request.form.keys():
        event_done = True
    event_recurring = False
    if "recurring" in request.form.keys():
        event_recurring = True

    new_event = Event(
        event_date,
        event_name,
        event_num_guests,
        event_location,
        event_description,
        event_done,
        event_recurring,
    )
    add_new_event(new_event)
    return render_template("index.html", title="Home", events=events)
