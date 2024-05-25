import socket
import geocoder
import json

HOST, PORT = "localhost", 9999


def welcome():
    lat_long = geocoder.ip('me').latlng
    comma_separated_lat_long = ' '.join(str(x) for x in lat_long)
    user_input = input(
        f"Welcome to the Weather CLI interface.\nYour latitude and longitude was detected as: "
        f"{comma_separated_lat_long}. Would you like to requesst the weather at that location? [Y/n]: "
    )
    decision = "y" if user_input == "" else "n"

    if decision.lower() == 'y':
        connect_to_server(lat_long)
    else:
        while decision == "n":
            lat = input('Please provide the latitude of the desired location: ')
            long = input('Please provide the longitude of the desired location: ')
            user_lat_long = [lat, long]
            comma_separated_lat_long = ' '.join(str(x) for x in user_lat_long)

            user_input = input(
                f"Is this the correct latitude and longitude {comma_separated_lat_long}? [Y/n]: "
            )
            decision = "y" if user_input == "" else "n"
            if decision.lower() == 'y':
                connect_to_server(user_lat_long)


def connect_to_server(lat_long):
    data = json.dumps(lat_long)

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")

    print(received)


if __name__ == "__main__":
    welcome()
