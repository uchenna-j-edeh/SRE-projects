import requests
import json
import pandas as pd
from dotenv import load_dotenv
import time
import collections

import os
# from pprint import pprint as pp

load_dotenv()

class G_APIs:
    """_summary_
    """
    def __init__(self, config_path):
        # set up config file
        self.source_path = None
        self.api_key = None
        self.output_dir = None

        self.config_path = config_path

        self.load_config()

    def load_config(self):
        """_summary_
        """
        with open(self.config_path) as fh:
            jfile = json.load(fh)

            self.source_path = jfile["source_path"]
            self.api_key = jfile["api_key"]
            self.output_dir = jfile["output_dir"]

    def get_latitude_longitude(self, address, api_key):
        """given address generate longitude/latitude

        Args:
            address (_type_): _description_
            api_key (_type_): _description_

        Returns:
            _type_: _description_
        """
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "address": address,
            "key": api_key
        }

        response = requests.get(base_url, params=params, timeout=5)
        data = response.json()

        if data['status'] == 'OK':
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            return latitude, longitude
        else:
            print("Geocoding was not successful. Status:", data['status'])
            return "NA", "NA"

    def process_csv(self):
        """process csv using pandas lib
        """
        output_file = os.path.join(self.output_dir, "output_file.csv")
        # fh = open(output_file, "w")
        data_frame = pd.read_csv(self.source_path, header=1)
        phone_number = []
        address = []
        state_locale = []
        lats =[]
        lngs = []
        for index, row in data_frame.iterrows():
            print(f"Row {index + 1}:")
            row_data = []
            latitude = "NA"
            longitude = "NA"
            count = 0
            for _, value in row.items():
                if isinstance(value, str):
                    row_data.append(value)

                    # if count == 0:
                    #     phone_number.append(value)
                    if count == 1:
                        # address.append(value)
                        # row_data.append(value)
                        latitude, longitude = self.get_latitude_longitude(value, self.api_key)
                        time.sleep(0.1)
                        # lats.append(latitude)
                        # lngs.append(longitude)
                        row_data.append(latitude)
                        row_data.append(longitude)

                    # if count == 2:
                    #     state_locale.append(value)
                else:
                    print(f"Data is undefined: {value}")
                    row_data.append("N/A")
                    # if count == 0:
                    #     phone_number.append("N/A")
                    if count == 1:
                        #  address.append("N/A")
                        #  lats.append("N/A")
                        row_data += ["N/A", "N/A"]
                    # if count == 2:
                    #     state_locale.append("N/A")

                count += 1

            if len(row_data) == 5:
                for i, val in enumerate(row_data):
                    if i == 0:
                        phone_number.append(val)
                    elif i == 2:
                        address.append(val)
                    elif i == 3:
                        lats.append(val)
                    elif i == 4:
                        lngs.append(val)
                    else:
                        state_locale.append(val)
            else:
                print(f'Data is invalid: {row_data}')

        dict_obj = {
            'phone': phone_number,
            'Address': address,
            'state': state_locale,
            'latitude': lats,
            'longitude': lngs
            }
        # pp(dict_obj, indent=4)
        
        df = pd.DataFrame(dict_obj)
        df.to_csv(output_file)


if __name__ == '__main__':
    gapi = G_APIs(os.environ['CONFIG_PATH']) # set your env variables
    gapi.process_csv()


# # Set your address and API key
# address = "1600 Amphitheatre Parkway, Mountain View, CA"
# api_key = "YOUR_API_KEY"

# latitude, longitude = get_latitude_longitude(address, api_key)

# if latitude and longitude:
#     print("Latitude:", latitude)
#     print("Longitude:", longitude)

# >>> from googleapi import G_APIs
# >>> address = '1600 Amphitheatre Parkway, Mountain View, CA'
# >>> api_key = 'SET_YOUR_API_KEY'
# >>> G_APIs.get_latitude_longitude(address, api_key)
# (37.4223878, -122.0841877)
# >>> 
