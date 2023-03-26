import modules.login
import tweepy
import pandas as pd 
from datetime import date


creds = modules.login.get_settings(r'.\settings.ini')

client = tweepy.Client(creds['bearer_token'])

## counter ##
x = 0
cter = 0

################ 14 of top 30 most followed news accounts on twitter############
# https://www.intelligencefusion.co.uk/insights/resources/article/top-30-most-followed-news-accounts-on-twitter/
################################################################################

news_handle = ['cnnbrk', 'CNN', 'nytimes', 'BBCWorld', 'TheEconomist', 
               'wsj', 'washingtonpost', 'abc', 'ChinaXinhuaNews', 'SkyNews', 'AJEnglish',
               'France24_en', 'RT_com', 'Reuters'] 
cnnbrk = []
CNN = []
nytimes= []
BBCWorld = []
TheEconomist =[]
wsj = []
washingtonpost = []
abc = []
ChinaXinhuaNews = []
SkyNews = []
AJEnglish = []
France24_en = []
RT_com = []
Reuters =[]
hndl_list = [cnnbrk, CNN, nytimes, BBCWorld, TheEconomist, wsj, washingtonpost, 
             abc, ChinaXinhuaNews, SkyNews, AJEnglish, France24_en, RT_com, Reuters]

#############################Tweet Fields to Lookup#############################
t_fields = ['Ukraine', 'Russia', 'Putin', 'Crimea', 'Invasion', 'nuclear weapons', 'war', 'Kremlin',
            'de-Nazify', 'Nazi', 'Russian Military', 'military', 'Beijing', 'China', 'Xi', 'NATO', 'kiev',
            'zelensky', 'donbass']
hashtags = ['ukraine', 'Ukraineconflict', 'ukrainewar', 'kiev', 'supportukraine', 'ukrainerussiawar', 'kremlin',
            'ukrainenews', 'zelensky', 'donbass']


acc_info = {}

for a in news_handle:
    acc = client.get_user(username=a)
    acc_info.update({acc.data.name : [acc.data.username, acc.data.id]} )


tweet_list = {}

for z in acc_info:
    for tweet in tweepy.Paginator(client.get_users_tweets, acc_info[z][1], 
                                    max_results=100).flatten(limit=3200):
        hndl_list[x].append({ tweet.id: tweet.text})
        print(cter)
        cter += 1
    x += 1

print(cter)
x = 0

        
today = date.today()
today = str(today)
outpath = 'C:\\Users\\Greg\\OneDrive\\Desktop\\LTU\\LTU_Capstone\\data\\news\\'

for a in news_handle:
    new_outpath = outpath + a + today + '.txt'
    with open(new_outpath, 'w', encoding='utf-8') as file:
        for item in hndl_list[x]:
            file.write(str(item) + '\n')
        print('writing to ', a)
    x += 1