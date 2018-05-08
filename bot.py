"""
This is a bot that takes news headlines and casually rewrites them
"""
#Import all tools to be needed / Create dictionary to replace words
#To make the replacements to the string
from functools import reduce
from authentication import api
import feedparser
from newspaper import Article
#Use this dictionary to replace words
repls_dic = {
	"witnesses":"these dudes I know", "allegedly":"kinda probably", "new study": "Tumblr post",
	"rebuild":"avenge", "space":"spaaaace", "google glass":"Virtual Boy", "smartphone":"Pokédex",
	"video":"low-budget movie", "electric":"Atomic", "senator":"Elf-Lord", "car": "Cat",
	"election": "Eating contest", "Congress":"Clown-house", "Leader":"dude in charge (that supposedly knows what to do)",
	"congressional leaders":"River spirits", "homeland security":"Homestar Runner",
	"could not be reached for comment": "is guilty and everybody knows it", "reveals":"shows off", "unveils":"Flexes",
	"breaking news":"Yo! Check this out!", "prosecute":"search like crae-zee",
	"fined":"grounded", "bitcoin":"Bitconeeeeeeeeeeect!!", "bit-coin":"Digital BLING", "america":"'MURICA",
	"airline":"Flying-bus stations", "google":"Googol", "strongest":"MOST BUFFED",
	"deadly":"maybe dangerous", "announces":"yells out loud", "secrets":"Gossip", "healthy":"questionable",
	"unhealthy":"questionable", "tumor":"lil' ball'o flesh", "best":"not-so-bad", "stunning":"irrelevant", "lava": "earth-soup",
	"tips":"weird thoughts I had while on the restroom", "comedian":"Clown-Lord", "melania trump":"Trumpy's Waifu",
	"italy":"Spaghettiland"}

#GET original string from a news headline or a tweet from CNN
orig_headline = "Placeholder"
#Get the link to the news article
art_link = "link"
#Turn orig_headline to lowercase to avoid checking for lower and uppders
orig_headline_low = orig_headline.lower()
#Replace some words using reduce and store it to new var
new_headline_low = reduce(lambda a, kv: a.replace(*kv), repls_dic.items(), orig_headline_low)
#make the first letter uppercase
new_headline_upp = new_headline_low.capitalize()
#Test?
print ("Now publishing to Twitter", new_headline_upp)
#Publish the new string to Twitter + add a link to the news article at the endswith
api.update_status(new_headline_upp)
print ("Success!")
