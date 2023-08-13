import pandas as pd 
import ast

def makecsv(my_list):
    df = pd.DataFrame(columns=['ID', 'Content'])

    for i in range(len(my_list)):
        for key, val in my_list[i].items():
            df.loc[i] = [key, val]

    return df


if __name__ == '__main__':

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
    hndl_list = [abc, AJEnglish, BBCWorld, CNN, cnnbrk, France24_en, 
                 nytimes, Reuters, RT_com, SkyNews,  TheEconomist, washingtonpost, wsj]
    
    str_list = ['abc2023-03-26.txt', 'AJEnglish2023-03-26.txt', 'BBCWorld2023-03-26.txt',
                'CNN2023-03-26.txt', 'cnnbrk2023-03-26.txt', 'France24_en2023-03-26.txt', 'nytimes2023-03-26.txt',
                'Reuters2023-03-26.txt','RT_com2023-03-26.txt','SkyNews2023-03-26.txt','TheEconomist2023-03-26.txt',
                'washingtonpost2023-03-26.txt', 'wsj2023-03-26.txt']
    
    inpath = 'C:\\Users\\Greg\\OneDrive\\Desktop\\LTU\\LTU_Capstone\\data\\news\\'
    outpath = 'C:\\Users\\Greg\\OneDrive\\Desktop\\LTU\\LTU_Capstone\\data\\news_csvs\\'
    abc_path = inpath + 'abc2023-03-26.txt'
    my_df = pd.DataFrame(columns=['Tweet ID', 'Tweet Contents'])

    for a in range(len(str_list)):
        r_path = inpath + str_list[a]

        with open(r_path, encoding='utf-8') as f:
            for line in f:
                line = ast.literal_eval(line)
                hndl_list[a].append(line)
            
        
        print(str_list[a])

    

    for a in range(len(str_list)):
        df = makecsv(hndl_list[a])
        df.to_csv(outpath + str_list[a])
