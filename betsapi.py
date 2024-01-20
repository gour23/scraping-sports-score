from mybot import chrome_driver
from selenium.webdriver.common.by import By
import time
import json
from datetime import datetime
from websites import Websites
import os

class Scraper:
    def __init__(self,sport_name,leagues_with_link) :
        for league_name in leagues_with_link:
            print(league_name)
            links = leagues_with_link[league_name]

            counter = 1
            for link in links:
                print(link)

                if "betsapi" in link:
                    all_data = Websites().bets(link)
                    # file_path = f"{sport_name}/{league_name}/"
                    # if not os.path.exists(file_path):
                    #     os.makedirs(file_path)

                    # file_path = f"{sport_name}/{league_name}/betsapi.json"
                    # print(file_path)
                    # self.save_data(all_data,file_path,league_name)

    def save_data(self,data,path,league_name):
        """
        It Takes scraped data from the website ,
        path (where we wanna save the data) and
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
            
            match_data_exists = any(match['Date'] == item['date'] and match['HomeTeam_Name'] == item['home_team'] and match['AwayTeam_Name'] == item['away_team'] for match in existing_data[league_name] )

            if not match_data_exists:
                existing_data[league_name].append({
                    'Date': item['date'],
                    'HomeTeam_Name': item['home_team'],
                    'AwayTeam_Name': item['away_team'],
                    'HomeTeam_Score': item['home_team_score'],
                    'AwayTeam_Score': item['away_team_score'],
                    'Result':item['result'],
                    'Source':item["source"]
                })

        with open(path, 'w') as file:
            json.dump(existing_data, file, indent=4)
            print("done")


sports = ["soccer"]
for s in sports:
    with open (f"{s}/leagues.json","r") as file:
        leagues = json.load(file)

    obj = Scraper(s,leagues)
# s="soccer"
# with open (f"{s}/leagues.json","r") as file:
#     leagues = json.load(file)

# obj = Scraper(s,leagues)