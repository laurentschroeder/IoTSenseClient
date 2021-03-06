import json
from terminaltables import SingleTable
import os
import io

sensors_dictionary = {}


def parse_json(received_bytes):
    # Convert received bytes to a string
    json_string = received_bytes.decode("utf-8")

    # Use json library to convert the json string into a python dictionary
    sensor_dictionary = json.loads(json_string)

    # Create a tuple from the dictionary to gain order
    sensor_values = (sensor_dictionary["Art der Messung"], sensor_dictionary["Messwert"], sensor_dictionary["Einheit"],
                     sensor_dictionary["Raum"], sensor_dictionary["Sensor ID"], sensor_dictionary["Sensor Sub ID"],
                     sensor_dictionary["Sensor"], sensor_dictionary["Zeitstempel"])

    write_to_file(sensor_values)

    # Create another dictionary that holds the sensor data as a tuple
    # key: tuple of sensor id and sub id
    # value: sensor data as tuple
    sensor_id = sensor_dictionary["Sensor ID"]
    sensor_sub_id = sensor_dictionary["Sensor Sub ID"]
    sensors_dictionary[(sensor_id, sensor_sub_id)] = sensor_values

    draw()


def draw():


    table_data    = [('Messung', 'Wert', 'Einheit', 'Raum', 'SensorID', 'SubID', 'Bezeichnung', 'Zeitstempel')]

    for e in sensors_dictionary:
        table_data.append(sensors_dictionary[e])

    table_instance = SingleTable(table_data, "IoT Sensors")
    table_instance.justify_columns[8] = 'left'
    os.system('cls' if os.name == 'nt' else 'clear')
    print(table_instance.table, end='\r')


def write_to_file(sensor_tuple):
    file = open('log.txt', 'a')
    file.write(str(sensor_tuple) + ';')

