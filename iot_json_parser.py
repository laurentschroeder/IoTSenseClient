import json
from terminaltables import SingleTable
import os


def parse_json(received_bytes):
    #print(received_bytes)
    #print(received_bytes.decode("utf-8"))
    json_data_string = received_bytes.decode("utf-8")
    sensor_dict = json.loads(json_data_string)
    draw_table(sensor_dict)


def draw_table(dict):
    TABLE_DATA = (
        ('Messung', 'Wert', 'Einheit', 'Raum', 'SensorID', 'SubID', 'Bezeichnung', 'Zeitstempel'),
        (dict["Art der Messung"], dict["Messwert"], dict["Einheit"], dict["Raum"], dict["Sensor ID"],
         dict["Sensor Sub ID"], dict["Sensor"], dict["Zeitstempel"])
    )

    table_instance = SingleTable(TABLE_DATA, "IoT Sensors")
    table_instance.justify_columns[8] = 'left'
    os.system('cls' if os.name == 'nt' else 'clear')
    print(table_instance.table, end='\r')


