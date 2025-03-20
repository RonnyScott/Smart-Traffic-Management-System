from backend.models.car_detection import detect_cars

def test_car_detection():
    results = detect_cars("dataset/test.jpg")
    assert len(results) > 0  # Ensure cars are detected

test_car_detection()
