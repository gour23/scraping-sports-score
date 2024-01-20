import json
from difflib import SequenceMatcher
import os

class Mapping:
    def __init__(self,api_data,scraped_data,path):
        api_teams = self.teams(api_data)
        scraped_teams = self.teams(scraped_data)
        matches = {}
        for element1 in api_teams:
            match = self.find_partial_match(element1, scraped_teams)
            if match:
                matches[element1] = match
            else:
                matches[element1]="Empty"

        self.add_data_to_json_file(path, matches)


    def teams(self,data):
        teams = set()
        for league_name,matches in data.items():
            for match in matches:
                teams.add(match["HomeTeam_Name"])
                teams.add(match["AwayTeam_Name"])

        return teams

    def find_partial_match(self,element, candidate_set):
        match_ratios = [(candidate, SequenceMatcher(None, element, candidate).ratio()) for candidate in candidate_set]
        
        # Sort by ratio in descending order
        match_ratios.sort(key=lambda x: x[1], reverse=True)
        
        # Return the best match (if any)
        if match_ratios and match_ratios[0][1] > 0.5:  # You can adjust the threshold as needed
            return match_ratios[0][0]
        else:
            return None
        
    def add_data_to_json_file(self,file_path,data):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_data = json.load(file)

            for key, value in data.items():
                if key not in existing_data or existing_data[key] != value:
                    existing_data[key] = value
            
            with open(file_path, 'w') as file:
                json.dump(existing_data, file, indent=2)
        else:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=2)



with open ("API_DATA.json","r") as file:
    api_data = json.load(file)

scraped_data_list = []

with open ("AFC Champions League_2.json","r") as file:
    scraped_data = json.load(file)
    scraped_data_list.append(scraped_data)

with open ("AFC Cup_1.json","r") as file:
    scraped_data = json.load(file)
    scraped_data_list.append(scraped_data)

json_file_path = "MAPPED_TEAMS.json"

for scraped_data in scraped_data_list:
    obj = Mapping(api_data,scraped_data,json_file_path)

##########################################################################################
# Manual Maintanence  Required