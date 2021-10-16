import webbrowser
import time
import random
import urllib.request
import re
from random_word import RandomWords
import requests


# url = 'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252Fresults%253Fsearch_query%253Dmyquery&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#ascii_char = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# webbrowser.open(url)
#webbrowser.get(chrome_path).open(url)
# time.sleep(5)


for k in range(10):
    
    r = RandomWords()
    str = r.get_random_word()
    if str == None: str = "None"
    str_list = list(str.split(" "))
    str = '-'.join(str_list)
    
    print("search term = " + str)
    
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+str)
    video_ids = re.findall(r'watch\?v=(\S{11})', html.read().decode())
    
    link = 'https://www.youtube.com/watch?v=' + video_ids[random.randint(0,5)]
    
    # webbrowser.open(link)
    r = requests.get(link)
    print(link)
    time.sleep(3)
