import requests
import json

base_url = "https://api.data.charitynavigator.org/v2"
data = {"app_id": "36f7e58b", "app_key": "5b7e63cbf53729f850317094a8e79575"}

def get_rating_info(ein):
	r = requests.get(base_url + "/Organizations/" + ein + "/Ratings", params=data)
	rating_id = r.json()[0]["ratingID"]

	r = requests.get(base_url + "/Organizations/" + ein + "/Ratings/" + str(rating_id), params=data)
	return r.json()
