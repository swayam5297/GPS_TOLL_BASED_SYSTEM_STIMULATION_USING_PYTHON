from flask import Flask, render_template
from flask_socketio import SocketIO
import simpy
from geopy.distance import geodesic
import random
import json
import warnings
import urllib3

app = Flask(__name__)
socketio = SocketIO(app)

# Define the highway route and toll gates
toll_gates = {
    "Delhi Toll": {"location": (28.7041, 77.1025), "charge": {"car": 120, "truck": 220, "bus": 320}},
    "Agra Toll": {"location": (27.1767, 78.0081), "charge": {"car": 130, "truck": 230, "bus": 330}},
    "Gwalior Toll": {"location": (26.2183, 78.1828), "charge": {"car": 110, "truck": 210, "bus": 310}},
    "Nagpur Toll": {"location": (21.1458, 79.0882), "charge": {"car": 140, "truck": 240, "bus": 340}},
    "Hyderabad Toll": {"location": (17.3850, 78.4867), "charge": {"car": 150, "truck": 250, "bus": 350}},
    "Bangalore Toll": {"location": (12.9716, 77.5946), "charge": {"car": 160, "truck": 260, "bus": 360}},
    "Chennai Toll": {"location": (13.0827, 80.2707), "charge": {"car": 170, "truck": 270, "bus": 370}},
}

route = [
    ("Mumbai", 19.0760, 72.8777),
    ("Amravati", 20.7002, 77.0082),
    ("Nagpur", 21.1458, 79.0882),
    ("Raipur", 21.2514, 81.6296),
    ("Kolkata", 22.5726, 88.3639),
    ("Guwahati", 26.1445, 91.7362),
    ("Dispur", 26.1433, 91.7898),
]

class Vehicle:
    def __init__(self, env, name, vehicle_type, start_index, end_index):
        self.env = env
        self.id = name
        self.vehicle_type = vehicle_type
        self.route = route[start_index:end_index + 1]
        self.position = self.route[0][1:]
        self.start_point = self.route[0][0]
        self.end_point = self.route[-1][0]
        self.total_charge = 0
        self.distance_traveled = 0
        self.action = env.process(self.drive())

    def drive(self):
        for i in range(1, len(self.route)):
            next_position = self.route[i][1:]
            distance = geodesic(self.position, next_position).km
            travel_time = distance / 60  # assuming average speed is 60 km/h
            yield self.env.timeout(travel_time)
            self.position = next_position
            self.distance_traveled += distance
            self.check_toll()
            socketio.emit('vehicle_update', {
                'id': self.id,
                'position': self.position,
                'type': self.vehicle_type,
                'start': self.start_point,
                'end': self.end_point,
                'distance_traveled': self.distance_traveled,
                'distance_to_next': distance if i < len(self.route) - 1 else 0  # Next distance if any
            })

    def check_toll(self):
        for gate_name, gate_info in toll_gates.items():
            if geodesic(self.position, gate_info["location"]).km < 10:  # Increased range to 10km for demonstration
                charge = gate_info["charge"][self.vehicle_type]
                self.total_charge += char
