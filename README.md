# Overview

A python server for providing the weekly weather to a client. This project designed to build a sever that both provided
data to a client, and read data from another source.

This program includes both a client and a server. The client gets the user's latitude and longitude, and then sends it
to the server. The server takes in the latitude and longitude and makes a request to an open weather api. After
transforming the data from the api the server sends back the weather to the client. The client can be run with
python: `python ./client.py` and the server can be run in a similar fashion: `python ./server.py`. The server has to be
running in order for the client code to work properly.

The purpose of this project wss to learn more about servers. I wanted to learn how to connect to other people's severs
and preform read and writes to an open server connection.

[Software Demo Video](https://www.youtube.com/watch?v=4ZLNx34g7eg)

# Network Communication

The networking requests are done with a client to server architecture. The sever connects over TCP on port 9999. The
server expects to receive a stringified list containing the latitude and longitude. The server then responds with a
palin test string.

# Development Environment

The server and client are written in python 3.11.6. The following libraries were also used:

- json
- requests
- socketserver
- socket
- geocoder

# Useful Websites

* [Python Socket Server](https://docs.python.org/3/library/socketserver.html)
* [Geocoder](https://geocoder.readthedocs.io/)
* [Requests](https://requests.readthedocs.io/en/latest/)

# Future Work

* Ensure that the weather is formatted correctly (day/night is always the format)
* Add an option to keep the socket open and updated the weather on an interval