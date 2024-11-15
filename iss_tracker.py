#!/usr/bin/env python3
import datetime
import requests

def main():

    iss_api = " http://api.open-notify.org/iss-now.json"
    iss_pos = requests.get(iss_api).json()
    print("CURRENT LOCATION OF THE ISS:")
    epoch_time = iss_pos['timestamp']
    dt_object = datetime.datetime.fromtimestamp(epoch_time)
    print(f"Timestamp: {dt_object}")
    print(f"Lat: {iss_pos['iss_position']['latitude']}")
    print(f"Lon: {iss_pos['iss_position']['longitude']}")










main()
