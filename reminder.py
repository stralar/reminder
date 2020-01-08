# Main file, execution file
# TODO add logging

import os
import datetime
import json
import module.mailing as mail
import random
from copy import copy

events_file_name = "events_real.json"
configs_path = "/module/config/"


save_file_name = "save_file.json"
save = {}
events = {}
mail_client = mail.Mail()


# TODO logging what happen
def _Load():
    global save_file_name
    global save
    global events

    # Check the existence of the events file
    events_exists = os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + configs_path + events_file_name)

    if events_exists:
        with open(os.path.dirname(os.path.abspath(__file__)) + configs_path + events_file_name) as json_data_file:
            events = json.load(json_data_file)
    else:
        print("events file not found")
        raise


    # Check the existence of the save file
    save_exists = os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + '/saves/' + save_file_name)

    if save_exists:
        with open(os.path.dirname(os.path.abspath(__file__)) + '/saves/' + save_file_name) as json_data_file:
            save = json.load(json_data_file)
    else:
        save["events"] = []
        for i in range(len(events["events"])):

            save["events"].append(None)
        save["queue_bath"] = []
        save["queue_kitchen"] = []


def _Save():
    global save

    json_data_file = open(os.path.dirname(os.path.abspath(__file__)) + '/saves/' + save_file_name, "w+")

    json_data_file.write(json.dumps(save))

    json_data_file.close()

def _Send_event_notification():
    global save
    global events

    for i in range(len(events["events"])):

        actual_time = datetime.datetime.now()
        send_notification = False
        # if a new event added
        if i >= len(save["events"]):
            save["events"].append(datetime.datetime.strftime(actual_time, "%Y-%m-%d"))
            send_notification = True
        elif save["events"][i] == None:
            save["events"][i] = datetime.datetime.strftime(actual_time, "%Y-%m-%d")
            send_notification = True
        else:
            # Time check
            last_send_time = datetime.datetime.strptime(save["events"][i], "%Y-%m-%d")

            if actual_time >= last_send_time + datetime.timedelta(weeks=events["events"][i]["repeat_per_week"]):
                save["events"][i] = datetime.datetime.strftime(actual_time, "%Y-%m-%d")
                send_notification = True
        if send_notification:
            random_email = []
            try:
                if events["events"][i]["info"] == "bath":
                    if len(save["queue_bath"]) <= 0:
                        save["queue_bath"] = copy(events["receivers"])

                    random_int = (random.randint(0, len(save["queue_bath"])-1))

                    random_email.append(save["queue_bath"][random_int])
                    save["queue_bath"].pop(random_int)

                if events["events"][i]["info"] == "kitchen":
                    if len(save["queue_kitchen"]) <= 0:
                        save["queue_kitchen"] = copy(events["receivers"])
                    random_int = (random.randint(0, len(save["queue_kitchen"])-1))

                    random_email.append(save["queue_kitchen"][random_int])
                    save["queue_kitchen"].pop(random_int)

            except:
                random_email = events["receivers"]
                pass

            #mail_client.send_without_file(events[i]["text"])
            print(random_email)


if __name__ == '__main__':
    _Load()
    _Send_event_notification()
    _Save()

    mail_client.shutdown_smtp()