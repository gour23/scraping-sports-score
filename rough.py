
# from mybot import chrome_driver
# from selenium.webdriver.common.by import By
# import re
# from datetime import datetime
# import time
# current_year = datetime.now().year

# def get_scores(link,league):
#     browser = chrome_driver()
#     browser.maximize_window()
#     browser.get(link)
#     browser.refresh()
#     data=[]
#     all_data = []
    
#     for m in browser.find_elements(By.CSS_SELECTOR,'.col-md-9'): 
#         for e in m.find_elements(By.CSS_SELECTOR,'td'):
#             data.append(e.text.split('\n'))
# #     print(data)
#     result_dicts = []
#     for i in range(0, len(data), 4):
#         # Create a dictionary for each set of four elements
#         result_dict = {'a': data[i][0], 'b': data[i + 1][0], 'c': data[i + 2][0], 'd': data[i + 3][0]}
#         result_dicts.append(result_dict)
    
# #         print(result_dict)

#     final_data = {}
#     for result in result_dicts:
# #         try:
#         final_data['date']=result['a'][:5]+"/2023"
#         home_team , away_team = result['c'].split(' v ')
#         final_data['home_team']=re.sub(r'\[.*?\]', '', home_team)
#         final_data['away_team']=re.sub(r'\[.*?\]', '', away_team)
# #         final_data['home_team'],final_data['away_team']=result['c'].split(' v ')
#         if result['d']=="Retired" or result['d']=="away" or result['d']=="Walkover" or result['d']=="Postponed" :
#             final_data['result']=result['d']
#         else:
#             final_data['home_team_score'],final_data['away_team_score']=result['d'].split('-') 
#             if final_data['home_team_score']>final_data['away_team_score']:
#                 final_data['result']=f"Winner {final_data['home_team']}"
#             elif final_data['home_team_score']<final_data['away_team_score']:
#                 final_data['result']=f"Winner {final_data['away_team']}"
#             else:
#                 final_data['result']="Draw"
#         # print(final_data)
    
#         all_data.append(final_data)
#     return all_data
# #         except Exception as e:
# #             print(e)
        
# link1 = "https://betsapi.com/le/11235/CPBL"
# league1= "xyz"
# d = get_scores(link1,league1)
# print(d)

############################################################################################################
# import os
# file_path = "folder1/folder2/folder3/"
# file_path = file_path+"folder4/"
# print(file_path)
# # if not os.path.exists(file_path):
# #     os.mkdir(file_path)

#################################################################################################################

from mybot import chrome_driver
from selenium.webdriver.common.by import By
import time
import json
from datetime import datetime
from websites import Websites
import os

browser = chrome_driver()
browser.maximize_window()

link = "https://www.google.com/search?q=Brasileiro+S%C3%A9rie+A&rlz=1C1RXQR_enIN1025IN1025&oq=Brasileiro+S%C3%A9rie+A&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBBzQxM2owajmoAgCwAgA&sourceid=chrome&ie=UTF-8#sie=lg;/g/11jspy1hvm;2;/m/0fnk7q;mt;fp;1;;;"
browser.get(link)
all_data = []
for i in browser.find_elements(By.CLASS_NAME,"KAIX8d"):
    pass







##########################################################################################################################




# link = "https://24live.com/page/sport/event/basketball-6/1940#results"
# browser.get(link)

# all_data = []
# for i in browser.find_elements(By.ID,"results"):
#     for m in i.find_elements(By.CLASS_NAME,"table-sport__row"):
#         date = m.text.split("\n")[0].split(" ")[0]
#         input_format = "%m/%d"
#         current_year = datetime.now().year
#         full_input_string = f"{date}{current_year}"
#         parsed_datetime = datetime.strptime(full_input_string, input_format + "%Y")
#         final_date = parsed_datetime.strftime("%Y-%m-%d")

#         data = {}
#         colon_index = m.text.split("\n").index(':')
        
#         data["date_time"] = final_date
#         data["home_team"] = m.text.split("\n")[3]
#         data["away_team"] = m.text.split("\n")[-2]
#         data["home_team_score"] = m.text.split("\n")[colon_index - 1].strip()
#         data["away_team_score"] = m.text.split("\n")[colon_index + 1].strip()
#         data["source"] = "24Live.com"
#         all_data.append(data)

# print(all_data)
