# 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler


token = '1001744474:AAEYkSP8P9mIUcsPT_Pzx8pPIbKpuw1Pr_8'
bot = telegram.Bot(token=token)
sched = BlockingScheduler()


def extract_links():
        # 해당 url의 html문서를 soup 객체로 저장
    url = 'https://paypaymall.yahoo.co.jp/store/zozo/item/51309849/?subcode_img=849/52309849/52309849b_18_d&img_type=z&subcode=GDID82867651'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    search_result = soup.select('div.ItemFKU_option')

    count=0
    stocks = []


    for i in search_result:
        count=count +1
        print(count)
        color = i.select('span.ItemFKU_text')[0].text
        value = i.select('span.Icon')[0].attrs['class'][1]
        
        print(color)
        if(value=='Icon-radioOff'):
            stocks.append(color + ". 재고 있음")
        elif(value=='Icon-close'):
            stocks.append(color + ". 재고 없음")
        else:
        #    print(str(count) + ". site확인 요 : "+ url)
        #    bot.sendMessage(chat_id='1020617783', text=str(count)+"site확인 요 : "+ url)
            stocks.append(color + ". site확인 요 : "+ url)

    bot.sendMessage(chat_id='1020617783', text=url)
    for stock in stocks:
        print(stock)
        bot.sendMessage(chat_id='1020617783', text=stock)


    
extract_links()
sched.add_job(extract_links, 'interval', hours=1)
# 시작
sched.start()



  




#for i in news_links:
#  print(i.get_text())
