import requests,re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as soup

#cnn
def get_cnn_words():    
    url_cnn='https://www.cnn.com/'
    cnn_parser='''"headline":(.*?)","'''
    strip_string = '''[\[,\/\'\""\\\]'''
    req_cnn = requests.get(url_cnn).text
    cnn_result = re.findall(cnn_parser,req_cnn) #parse with regular expression 
    cnn_result = [cnn.replace("\\u003c/strong","") for cnn in cnn_result] 
    cnn_result = [cnn.replace("u003cstrong>","") for cnn in cnn_result]
    clean_cnn_result = str(re.sub(strip_string,'',str(cnn_result))) #clean up data 
    return clean_cnn_result

#msnbc 
def get_msnbc_words():
    url_msnbc='https://www.msnbc.com/'
    req_msnbc = requests.get(url_msnbc).content
    msnbc_soup = soup(req_msnbc,'html.parser')
    msnbc_headlines = msnbc_soup.find_all('span',class_="headline___38PFH")
    msnbc_headline_text = str([text.text for text in msnbc_headlines])
    return msnbc_headline_text

#fox     
def get_fox_words():
    url_fox ='https://www.foxnews.com/'
    req_fox = requests.get(url_fox).content
    fox_soup = soup(req_fox,'html.parser')
    fox_headlines = fox_soup.findAll('h2',{'class':'title'})
    fox_headline_text = str([headline.text for headline in fox_headlines])
    return fox_headline_text

def make_word_cloud():
    words = ''
    words += get_cnn_words()
    words += get_msnbc_words()
    words += get_fox_words()
    wc = WordCloud().generate(words)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()    

if __name__=='__main__':
    make_word_cloud()

#python3 practice = making word clouds - aggregating news headlines   Elliott Arnold  aka si3mshady 4-12-19



    