import socketserver
import requests
import json


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        lat_long = json.loads(self.data)
        print("Received from {}:".format(self.client_address[0]))
        print(lat_long)
        # just send back the same data, but upper-cased
        weather = get_weather(lat_long[0], lat_long[1])
        self.request.sendall(bytes(weather + "\n", "utf-8"))


def get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Error fetching the weather from from api.weather.gov")


def format_weather(periods):
    forcast = ''
    evening_data = {}
    for idx, period in enumerate(periods):
        # if the index is event the period represents the evening weather data
        if idx % 2 == 0:
            # save the evening data to use later in conjunction with the morning data
            evening_data = period
        else:
            forcast += f"{period['name']}: {period['temperature']}/{evening_data['temperature']} "

    return forcast


def get_weather(lat, long):
    location_information = get_data(f'https://api.weather.gov/points/{lat},{long}')
    if location_information:
        forcast_url = location_information['properties']['forecast']
        forcast = get_data(forcast_url)

        return format_weather(forcast['properties']['periods'])

    else:
        return "Weather Forcast Could Not Be Generated"


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f'Listening on {HOST}:{PORT}')
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
