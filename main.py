import turtle
import json
import urllib.request


# Setup the world map
win_size = 800
screen = turtle.Screen()
screen.setup(win_size, win_size)

# Load the images into turtle module
screen.bgpic('map.gif')
screen.register_shape('iss.gif')

# Setup iss object, Turtle instance
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.penup()


api_url = "http://api.open-notify.org/iss-now.json"

while True:
    # Get data from API
    with urllib.request.urlopen(api_url) as url:
        data = json.loads(url.read())

        # Extract location of ISS
        longitude = float(data['iss_position']['longitude'])
        latitude = float(data['iss_position']['latitude'])
        iss.setpos(longitude * (win_size / 2) / 180,
                   latitude * (win_size / 2) / 180)

        # Terminal output prints every fifth value to prevent spam
        print(longitude, latitude)
