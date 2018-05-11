"""
This is a bot that takes news headlines and casually rewrites them
"""
#Import all tools to be needed / Create dictionary to replace words

from random import randint
from functools import reduce
from authentication import api
#Use this dictionary to replace words
from replace_dic import rpls_dic
import feedparser
import random

#Setup for feedparser
sources = ['http://rss.cnn.com/rss/cnn_us.rss', 'https://abcnews.go.com/abcnews/topstories']
d = feedparser.parse(random.choice(sources))

#Set a random number so that each time it takes info from a different article each time
art_num = randint(0,25)
#art_num = 12
#GET original string from a news headline or a tweet from CNN
orig_headline = d.entries[art_num].title
#Get the link to the news article
art_link = d.entries[art_num].link
#Turn orig_headline to lowercase to avoid checking for lower and uppders
orig_headline_low = orig_headline.lower()
#Replace some words using reduce and store it to new var
new_headline_low = reduce(lambda a, kv: a.replace(*kv), rpls_dic.items(), orig_headline_low)
#make the first letter uppercase
new_headline_upp = new_headline_low.capitalize()

tweet_this = new_headline_upp + "\n" + art_link
#Publish the new string to Twitter + add a link to the news article at the endswith
api.update_status(tweet_this)

print("Now printing the original tittle:", orig_headline)
print("Now printing what should appear on Twitter:", "\n", tweet_this)
print(art_num)
