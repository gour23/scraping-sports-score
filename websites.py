from mybot import chrome_driver
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import json
import re

class Websites:
    def __init__(self) :
        self.browser = chrome_driver()
        self.browser.maximize_window()

    def bets(self,link,sport):
        try:
            self.browser.get(link)
            data=[]
            print(sport)
    
            for m in self.browser.find_elements(By.CSS_SELECTOR,'.col-md-9'): 
                for e in m.find_elements(By.CSS_SELECTOR,'td'):
                    data.append(e.text.split('\n'))

            result_dicts = []
            for i in range(0, len(data), 4):
                # Create a dictionary for each set of four elements
                result_dict = {'a': data[i][0], 'b': data[i + 1][0], 'c': data[i + 2][0], 'd': data[i + 3][0]}
                result_dicts.append(result_dict)
            all_data = []
            for result in result_dicts:
                final_data = {}
                # print(result['a'][:5][0:2])
                if result['a'][:5][0:2]=="12" or result['a'][:5][0:2]=="11":
                    final_data['date_time']=result['a'][:5]+"/2023"
                else:
                    final_data['date_time']=result['a'][:5]+"/2024"

                # print(final_data['date_time'])
                home_team , away_team = result['c'].split(' v ')
                final_data['home_team']=re.sub(r'\[.*?\]', '', home_team)
                final_data['away_team']=re.sub(r'\[.*?\]', '', away_team)
        #         final_data['home_team'],final_data['away_team']=result['c'].split(' v ')
                if result['d']=="Retired" or result['d']=="away" or result['d']=="Walkover" or result['d']=="Postponed" or result['d']=="Cancelled":
                    final_data['result']=2
                    final_data['home_team_score'] = 0
                    final_data['away_team_score'] = 0
                else:
                    final_data['home_team_score'],final_data['away_team_score']=result['d'].split('-') 
                    if final_data['home_team_score']>final_data['away_team_score']:
                        final_data['result']=0
                    elif final_data['home_team_score']<final_data['away_team_score']:
                        final_data['result']=1
                    else:
                        final_data['result']=2

                final_data['source']="betsapi.com"
                
                all_data.append(final_data)

            self.browser.close()

            return all_data


        except Exception as e:
            print(e)

    def live24(self,link,sport):
        try:
            self.browser.get(link)
            all_data = []
            print(sport)
            for i in self.browser.find_elements(By.ID,"results"):

                for m in i.find_elements(By.CLASS_NAME,"table-sport__row"):

                    date = m.text.split("\n")[0].split(" ")[0]
                    if date[0:2]=="12" or date[0:2]=="11":
                        current_year = "2023"
                    else:
                        current_year = "2024"

                    # print(date[0:2])
                    input_format = "%m/%d"
                    full_input_string = f"{date}{current_year}"
                    parsed_datetime = datetime.strptime(full_input_string, input_format + "%Y")
                    final_date = parsed_datetime.strftime("%m/%d/%Y")

                    data = {}
                    if sport=="soccer":
                        try:
                            colon_index = m.text.split("\n").index(':')
                            
                            data["date_time"] = final_date
                            data["home_team"] = m.text.split("\n")[3]
                            data["away_team"] = m.text.split("\n")[-2]
                            data["home_team_score"] = m.text.split("\n")[colon_index - 1].strip()
                            data["away_team_score"] = m.text.split("\n")[colon_index + 1].strip()
                            
                        except:
                            data["date_time"] = final_date
                            data["home_team"] = m.text.split("\n")[4]
                            data["away_team"] = m.text.split("\n")[3]
                            data["home_team_score"] = m.text.split("\n")[6]
                            data["away_team_score"] = m.text.split("\n")[5]
                    else:
                        try:
                            colon_index = m.text.split("\n").index(':')
                            
                            data["date_time"] = final_date
                            data["home_team"] = m.text.split("\n")[-2]
                            data["away_team"] = m.text.split("\n")[3]
                            data["home_team_score"] = m.text.split("\n")[colon_index + 1].strip()
                            data["away_team_score"] = m.text.split("\n")[colon_index - 1].strip()
                            
                        except:
                            data["date_time"] = final_date
                            data["home_team"] = m.text.split("\n")[3]
                            data["away_team"] = m.text.split("\n")[4]
                            data["home_team_score"] = m.text.split("\n")[5]
                            data["away_team_score"] = m.text.split("\n")[6]
                    if data['home_team_score']>data['away_team_score']:
                        data['result']=0
                    elif data['home_team_score']<data['away_team_score']:
                        data['result']=1
                    else:
                        data['result']=2
                    data["source"] = "24Live.com"

                    all_data.append(data)
            self.browser.close()
 
            return all_data
        
        except Exception as e:
            print(e)

    def google(self,link):
        try:
            self.browser.get(link)
            all_data = []
            for i in self.browser.find_elements(By.CSS_SELECTOR,".KAIX8d"):
                if i.text.split("\n")[0] == 'Final' or i.text.split("\n")[0] =='FT' :
                    data = {}
                    data["date"]=i.text.split("\n")[1]
                    data["HomeTeam_name"]=i.text.split("\n")[-5]
                    data["HomeTeam_score"]=i.text.split("\n")[-6]
                    data["AwayTeam_name"]=i.text.split("\n")[-2]
                    data["AwayTeam_score"]=i.text.split("\n")[-3]

        except Exception as e:
            print(e)

    def flashscore(self,link,sport):
        try:
            self.browser.get(link)
            all_data = []
            print(sport)
            for i in self.browser.find_elements(By.CSS_SELECTOR,".event.event--results"):
                counter = 1
                for m in i.find_elements(By.CSS_SELECTOR,".event__match.event__match--static.event__match--twoLine"):
                    date = m.text.split("\n")[0].split(" ")[0]
                    if date[3:5]=="12" or date[3:5]=="11":
                        current_year = "2023"
                    else:
                        current_year="2024"

                    # print(date[3:5])

                    input_format = "%d.%m."
                    # current_year = datetime.now().year
                    full_input_string = f"{date}{current_year}"
                    parsed_datetime = datetime.strptime(full_input_string, input_format + "%Y")
                    final_date = parsed_datetime.strftime("%m/%d/%Y")

                    data = {}
                    
                    data['date_time'] = final_date
                    if sport=="Hockey" or sport=="Basketball":
                        if "AOT" in m.text.split("\n") or "Pen" in m.text.split("\n"):
                            data['home_team'] = m.text.split("\n")[3]
                            data['away_team'] = m.text.split("\n")[2]
                            data['home_team_score'] = m.text.split("\n")[5]
                            data['away_team_score'] = m.text.split("\n")[4]
                        else:
                            data['home_team'] = m.text.split("\n")[2]
                            data['away_team'] = m.text.split("\n")[1]
                            data['home_team_score'] = m.text.split("\n")[4]
                            data['away_team_score'] = m.text.split("\n")[3]
                    else:
                        data['home_team'] = m.text.split("\n")[1]
                        data['away_team'] = m.text.split("\n")[2]
                        data['home_team_score'] = m.text.split("\n")[3]
                        data['away_team_score'] = m.text.split("\n")[4]

                    if data['home_team_score']>data['away_team_score']:
                        data['result']=0
                    elif data['home_team_score']<data['away_team_score']:
                        data['result']=1
                    else:
                        data['result']=2
                    data["source"] = "flashscore.com"
                    time.sleep(0.5)
                    counter = counter+1
                    all_data.append(data)
                    if counter>20:
                        counter = 1
                        break

            self.browser.close()
    
            return all_data

        except Exception as e:
            print(e)


