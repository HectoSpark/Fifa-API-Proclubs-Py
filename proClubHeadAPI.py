import urllib, json
import urllib.request

def findClubID(ClubName,Platform):
	json_url = urllib.request.urlopen("https://www.easports.com/iframe/fifa17proclubs/api/platforms/" + Platform + "/clubsComplete/" + ClubName.replace(" ", "%20"))
	data = json.loads(json_url.read())
	footballData = data["raw"]
	clubID = int(list(footballData.keys())[0])
	return clubID
	
