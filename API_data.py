import json
import requests

sport_id = 1
response = requests.get(f"https://sitapi.pulsewager.io/v1/sport/scraper/games?sportId={sport_id}&accessToken=60c3b642-f22e-4e9b-8e78-9b9d66abdd62")
data =response.json()
# print(data)
if len(data['results'])==0:
        print("yess")
else:
    final_data = []
    for p in range(1,data['totalPages']+1):
        print(f"page {p}")
        response = requests.get(f"https://sitapi.pulsewager.io/v1/sport/scraper/games?sportId={sport_id}&accessToken=60c3b642-f22e-4e9b-8e78-9b9d66abdd62&page={p}")
        data =response.json()
  
        for i in range(0,len(data['results'])):  
            data_dict = {}
            date = data['results'][i]['startDateTime'].split("T")
            data_dict["Date"] = date[0]
            data_dict["HomeTeam_Name"] = data['results'][i]['homeTeam']['name']
            data_dict["AwayTeam_Name"] = data['results'][i]['awayTeam']['name']
            data_dict["HomeTeam_ID"] = data['results'][i]['homeTeam']['id']
            data_dict["AwayTeam_ID"] = data['results'][i]['awayTeam']['id']
            if 'resultFromAPIs' in data['results'][i]:   
                data_dict["HomeTeam_Score"] = data['results'][i]['resultFromAPIs']['score'][0]
                data_dict["AwayTeam_Score"] = data['results'][i]['resultFromAPIs']['score'][2]
            
            data_dict["League"] = data['results'][i]['league']['name']
            
            final_data.append(data_dict)
    
    file_path = "API_DATA.json"
    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    for item in final_data:
        league = item['League']
        if league not in existing_data:
            existing_data[league] = []

        match_data_exists = any(match['Date'] == item['Date'] and match['HomeTeam_Name'] == item['HomeTeam_Name'] and match['AwayTeam_Name'] == item['AwayTeam_Name'] for match in existing_data[league] )

        if not match_data_exists:
            existing_data[league].append({
                'Date': item['Date'],
                'HomeTeam_Name': item['HomeTeam_Name'],
                'AwayTeam_Name': item['AwayTeam_Name'],
                'HomeTeam_ID': item['HomeTeam_ID'],
                'AwayTeam_ID': item['AwayTeam_ID'],
                'HomeTeam_Score': item['HomeTeam_Score'],
                'AwayTeam_Score': item['AwayTeam_Score']
            })
        
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)
        print("done")