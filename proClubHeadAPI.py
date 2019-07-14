import urllib, json
import urllib.request

#Find club ID
def findClubID(ClubName,Platform):
	json_url = urllib.request.urlopen("https://www.easports.com/iframe/fifa17proclubs/api/platforms/" + Platform + "/clubsComplete/" + ClubName.replace(" ", "%20"))
	data = json.loads(json_url.read())
	footballData = data["raw"]
	clubID = int(list(footballData.keys())[0])
	return clubID

#Find club members
def getClubMembers(ClubID, Platform):
	json_url = urllib.request.urlopen("https://www.easports.com/iframe/fifa17proclubs/api/platforms/" + Platform + "/clubs/" + str(ClubID) + "/membersComplete")
	data = json.loads(json_url.read())
	footballData = data["raw"]
	#print(footballData)
	Keys = list(footballData.keys())
	#print(Keys)
	PlayerData = []
	for playerKey in Keys:
		player = footballData[playerKey]
		PlayerData.append(player)
	#Players = footballData[Raw]
	#print(PlayerData[0]["name"])
	return PlayerData
	
def getClubStats(ClubName, Platform):
	pass
	
def getClubMembersNames(ClubID, Platform):
	Data = getClubMembers(ClubID,Platform)
	Names = []
	for player in Data:
		name = player["name"]
		Names.append(name)
	return Names
	
#requires PlayerName and ClubName
def findPlayerBlazeID(Player, ClubName, Platform):
	ClubID = findClubID(ClubName, Platform)
	ClubData = getClubMembers(ClubID, Platform)
	BlazeID = "0"
	for player in ClubData:
		if player["name"] == Player:
			BlazeID = player["blazeId"]
	return BlazeID
	
def findPlayerStats(BlazeID, Name, Platform):
	json_url = urllib.request.urlopen("https://www.easports.com/iframe/fifa17proclubs/api/platforms/" + Platform + "/members/'" + BlazeID + "'/stats")
	data = json.loads(json_url.read())
	footballData = data["raw"]
	Key = str(list(footballData.keys())[0])
	playerData = footballData[Key]
	string = "Name: " + Name + "\n" + "Pro Pos:" + str(playerData["proPos"]) + "\n" + "Favourite Position:" + str(playerData["favoritePosition"]) + "\n" + "Games Played:" + str(playerData["gamesPlayed"]) + "\n"
	string = string + "Goals:" + str(playerData["goals"]) + "\n" + "Assists:" + str(playerData["assists"]) + "\n" + "Man of the Match:" + str(playerData["manOfTheMatch"]) + "\n" + "Average Rating:" + str(playerData["ratingAve"])
	print(string)
	return string
	
def findPlayerClubStats(Name,ClubName, Platform):
	BlazeID = findPlayerBlazeID(Name, ClubName, Platform)
	ClubID = findClubID(ClubName,Platform)
	json_url = urllib.request.urlopen("https://www.easports.com/iframe/fifa17proclubs/api/platforms/" + Platform + "/clubs/"+ str(ClubID) +"/members/'" + BlazeID + "'/stats")
	print("https://www.easports.com/iframe/fifa17proclubs/api/platforms/" + Platform + "/clubs/"+ str(ClubID) +"/members/'" + BlazeID + "'/stats")
	data = json.loads(json_url.read())
	footballData = data["raw"]
	Key = str(list(footballData.keys())[0])
	playerData = footballData[Key]
	string = "Pro Name: " + playerData["proName"] + "\n"
	string = string + "Overall: " + playerData["proOverall"] + "\n"
	string = string + "Games Played: " + playerData["gamesPlayed"] + "\n"
	string = string + "Win Rate: " + playerData["winRate"] + "\n"
	string = string + "Goals: " + playerData["goals"] + "\n"
	string = string + "Assists: " + playerData["assists"] + "\n"
	string = string + "Pass Success Rate: " + playerData["passSuccessRate"] + "%\n"
	string = string + "Tackles Made: " + playerData["tacklesMade"] + "\n"
	string = string + "tackleSuccessRate: " + playerData["tackleSuccessRate"] + "%\n"
	string = string + "Man of the Match: " + playerData["manOfTheMatch"] + "\n"
	string = string + "Red Cards: " + playerData["redCards"] + "\n"
	print(string)
	return string
