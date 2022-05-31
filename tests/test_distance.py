from mlproject.distance import haversine
import math

def test_valid_distance_from_haversine():
    distance = haversine(0.1, 0.1, 0.1, 0.1)
    assert distance >= 0

def test_distance_type_from_haversine():
    distance = haversine(0.1, 0.1, 0.1, 0.1)
    assert type(distance) == float
