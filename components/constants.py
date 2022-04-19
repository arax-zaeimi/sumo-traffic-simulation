
import os
import sys


PREFIX = "demo"
OCCUPATION_PROBABILITY = 0.5
SIMULATION_DELAY = "0"
SIMULATION_CLIENTS = "1"
SIMULATION_STEP_LENGTH = "0.001"
ALLOWED_VEHICLES = ('public_emergency', 'public_authority', 'public_army', 'public_transport', 'transport', 'private', 'emergency', 'authority',
                    'army', 'vip', 'passenger', 'hov', 'taxi', 'bus', 'coach', 'delivery', 'truck', 'trailer', 'motorcycle', 'moped', 'bicycle', 'evehicle')
MAX_SEARCH_RADIUS = 20

# this is the id of vType that is defined in route files.
SERVICE_VEHICLE_TYPE = 'service_vehicle'


PORT = 8883
SUMO_HOME = os.path.realpath(os.environ.get(
    "SUMO_HOME", os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")))
sys.path.append(os.path.join(SUMO_HOME, "tools"))
try:
    from sumolib import checkBinary  # noqa
except ImportError:
    def checkBinary(name):
        return name
NETCONVERT = checkBinary("netconvert")
SUMO = checkBinary("sumo")
SUMOGUI = checkBinary("sumo-gui")


class change_types:
    NEW_VEHICLE = 'add_one'
    NEW_VEHICLES = 'add_multiple'
    NEW_DESTINATION = 'update_destination'
