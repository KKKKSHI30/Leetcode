import pandas as pd
import numpy as np
import selenium
from selenium import webdriver
import bs4
from bs4 import BeautifulSoup
from instaloader import Instaloader, Profile
import instaloader
import requests
# from webdriver_manager.chrome import ChromeDriverManager
import lxml
import random
import collections

num_likes = []
num_comments = []
num_posts = []
ins_link =  ['donovanezeiruaku',
 'antwane3wells',
 'nolimitdall',
 'zachh.branch',
 'yk.d1perk',
 'malik_benson5',
 'will.campbell66',
 'djlagway',
 'amariusmims',
 'dedwards___']
loader = Instaloader()

for username in ins_link[0:10]:
    profile = Profile.from_username(loader.context, username)
    num_followers = profile.followers
    total_num_likes = 0
    total_num_comments = 0
    total_num_posts = 0

    for post in profile.get_posts():
        total_num_likes += post.likes
        total_num_comments += post.comments
        total_num_posts += 1

    if total_num_posts:
        num_likes.append(total_num_likes)
        num_comments.append(total_num_comments)
        num_posts.append(total_num_posts)

    else:
        print(f"User '{username}' does not exist.")
        num_likes.append(0)
        num_comments.append(0)
        num_posts.append(0)
