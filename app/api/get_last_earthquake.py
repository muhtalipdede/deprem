from app.api.get_earthquake import get_earthquake

def get_last_earthquake():
    earthquake = get_earthquake(1)
    return earthquake[0:1]