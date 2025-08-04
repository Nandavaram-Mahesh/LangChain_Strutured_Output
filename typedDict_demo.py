from typing import TypedDict

class Drone(TypedDict):
    Category: str
    weight: int
    speed: int
    payload_type: str
    payload_weight: int

kamikaze: Drone = {
    "Category": "Bomber",
    "weight": 30,
    "speed": 200,
    "payload_type": "Kamikaze",
    "payload_weight": 25
}


print(kamikaze)