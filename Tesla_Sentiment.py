# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 23:53:38 2019

@author: Nick Bosio
"""
import os
import tweepy as tw
import requests
import pandas as pd

response=requests.get(r'https://api.twitter.com/1.1/search/tweets.json')
key='CPkdt6u4a5WMxv2fGlnSsXazw'
print(response)

CONSUMER_


search_word='#Tesla'
date_since="2019-10-15"