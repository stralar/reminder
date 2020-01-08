# This module load if exists the save file, else it creates a new one
# TODO add logging


import json
import os
import sys
import datetime
import time

save_file_name = "save_file.json"

class Load:
    def __init__(self, events):
        # Check the existence of the save file
        save_exists = os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + '/config/' + save_file_name)

        # TODO what happen logging
        if save_exists:
            with open(os.path.dirname(os.path.abspath(__file__)) + '/config/' + save_file_name) as json_data_file:
                self.config = json.load(json_data_file)
        else:
            json_data_file = open(os.path.dirname(os.path.abspath(__file__)) + '/config/' + save_file_name, "w+")

            data = {}
            events_save = []
            datetime_obj = datetime.datetime.now()

            for i in range(len(events)):
                events_save.append(str(datetime_obj))


            data["events"] = events_save

            json_data_file.write(json.dumps(data))

            json_data_file.close()

'''
if __name__ == '__main__':
    with open(os.path.dirname(os.path.abspath(__file__)) + '/config/events_real.json') as json_data_file:
        jdata = json.load(json_data_file)

    loading = Load(jdata["events"])
'''