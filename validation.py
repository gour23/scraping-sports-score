import json

with open("API_DATA.json","r") as file:
    api_data = json.load(file)

with open("SCRAPED_DATA.json","r") as file:
    scraped_data = json.load(file)
    
with open("MAPPED_TEAMS.json","r") as file:
    mapped_teams = json.load(file)

validated_data = []
for league in api_data:
    for i in range(0,len(api_data[league])):
        for j in range(0,len(scraped_data[league])):
            if mapped_teams[api_data[league][i]["HomeTeam_Name"]] == scraped_data[league][j]["HomeTeam_Name"] and mapped_teams[api_data[league][i]["AwayTeam_Name"]]== scraped_data[league][j]["AwayTeam_Name"]:
                if api_data[league][i]["HomeTeam_Score"]==scraped_data[league][j]["HomeTeam_Score"] and api_data[league][i]["AwayTeam_Score"]==scraped_data[league][j]["AwayTeam_Score"]:
                    # print(api_data[league][i]["HomeTeam_Score"])
                    validated_data.append(api_data[league][i])

                # print(api_data[league][i])
                # print(scraped_data[league][j])

            
print(validated_data) 

    