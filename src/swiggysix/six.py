import time

import requests
import json

from webpush import send_group_notification

player_six_count = dict()
player_four_count = dict()

def send_alert():
    requests.get("http://localhost:8000/sendsixalerthidden")

def fetch_scores():
    text = requests.get("https://www.cricbuzz.com/match-api/livematches.json").text
    text_parsed = json.loads(text)
    matches = text_parsed["matches"]
    match_to_track = None

    for match in matches:
        match = matches[match]
        if match["series"]["type"] == "IPL":
            current_time = int(time.time())
            if current_time > int(match["start_time"]) and current_time < int(match["exp_end_time"]):
                match_to_track = match

    if match_to_track == None:
        return

    batsmen = match_to_track["score"]["batsman"]
    for batsman in batsmen:
        if batsman["id"] not in player_six_count.keys():
            player_six_count[batsman["id"]] = batsman["6s"]
        if batsman["id"] not in player_four_count.keys():
            player_four_count[batsman["id"]] = batsman["4s"]

        if player_six_count[batsman["id"]] != batsman["6s"]:
            player_six_count[batsman["id"]] = batsman["6s"]
            print("6")
            send_alert()
        if player_four_count[batsman["id"]] != batsman["4s"]:
            player_four_count[batsman["id"]] = batsman["4s"]
            print("4")
            send_alert()

while True:
    fetch_scores()
    time.sleep(15)
    print(player_four_count,player_six_count)