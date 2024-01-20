from mybot import chrome_driver
from selenium.webdriver.common.by import By
import time
import json
from datetime import datetime
from websites import Websites

class Scraper:
    def __init__(self,api_data,leagues_with_link) :
        for league_name in api_data:
            if league_name in leagues_with_link.keys():
                links = leagues_with_link[league_name]
                counter = 1
                for link in links:

                    if "www.flashscore" in link:
                        all_data = Websites().flashscore(link)
                        file_path = f"{league_name}_{counter}.json"
                        self.save_data(all_data,file_path,league_name)

                    elif "24live" in link:
                        all_data = Websites().live24(link)
                        file_path = f"{league_name}_{counter}.json"
                        self.save_data(all_data,file_path,league_name)

                    elif "afc" in link:
                        pass

                    counter = counter + 1

    def save_data(self,data,path,league_name):
        """
        It Takes scraped data from the website ,
        path, where we wanna save the data and
        league-name
        
        """
        try:
            with open(path, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = {}

        for item in data:
            if league_name not in existing_data:
                existing_data[league_name] = []
            
            match_data_exists = any(match['Date'] == item['date_time'] and match['HomeTeam_Name'] == item['home_team'] and match['AwayTeam_Name'] == item['away_team'] for match in existing_data[league_name] )

            if not match_data_exists:
                existing_data[league_name].append({
                    'Date': item['date_time'],
                    'HomeTeam_Name': item['home_team'],
                    'AwayTeam_Name': item['away_team'],
                    'HomeTeam_Score': item['home_team_score'],
                    'AwayTeam_Score': item['away_team_score'],
                    'Source':item["source"]
                })
        
        with open(path, 'w') as file:
            json.dump(existing_data, file, indent=4)
            print("done")

with open ("API_DATA.json","r") as file:
    api_data = json.load(file)

with open ("leagues.json","r") as file:
    leagues = json.load(file)

obj = Scraper(api_data,leagues)