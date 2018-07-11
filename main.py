###### size? Order Checker by @donjawn [@donjawns on Twitter]
import requests
from bs4 import BeautifulSoup as bs
import time
from datetime import datetime

datetime.now().strftime('%H:%M:%S') # time



def order_checker():
    with open('orderinfo.txt', 'r') as myfile:
            #fixedList = myfile.read().replace("@", "%40") # in accordance w/ link format
            info = myfile.read().split('\n')
            #info = fixedList.split('\n')
            emails = [information.split(':')[0] for information in info if information != '']
            order_numbers = [information.split(':')[1] for information in info if information != '']
            infoLine = 0
            for i in range(len(info)):
                fixedEmail = emails[infoLine].replace("@", "%40")
                customerInfo = order_numbers[infoLine]
                main_url = 'https://www.size.co.uk/track-my-order/?orderID='+str(customerInfo)+'&email='+str(fixedEmail)+'&postcode='
               
                
                headers = {
                    'authority': 'www.size.co.uk',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'referer': 'https://www.size.co.uk/track-my-order/',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'if-none-match': 'ee4a1278e0f74b4981e0abee4f207a3c',
                    }
                
                params = (
                    ('type', 'userAction'),
                    ('data', 'eyJjaGFubmVsIjoid2ViX3dpZGdldCIsInVzZXJBY3Rpb24iOnsiY2F0ZWdvcnkiOiJhcGkiLCJhY3Rpb24iOiJoaWRlIiwibGFiZWwiOm51bGwsInZhbHVlIjpudWxsfSwiYnVpZCI6IjM0MjZlZDhhOGQ4MzFiZTFjZDViNjVhY2ZjNjdkNmQ1Iiwic3VpZCI6IjE0MTI5MGNhMzY4YTUxN2FhMDdjZDM2NDBhZDdjYzMxIiwidmVyc2lvbiI6ImUyMWE5NzE3MyIsInRpbWVzdGFtcCI6IjIwMTgtMDctMTBUMTg6MTQ6MzMuMDUxWiIsInVybCI6Imh0dHBzOi8vd3d3LnNpemUuY28udWsvdHJhY2stbXktb3JkZXIvP29yZGVySUQ9ODQ1OTMxMjAmZW1haWw9Zm9vdHBhdHJvbCU0MHJhbWlyZXptYXJrLmNvbSZwb3N0Y29kZT0ifQ=='),
                    )
                response = requests.get(main_url, headers=headers, params=params)
                session = requests.Session()
                session.headers.update(headers)

                response = session.get(main_url)
                soup = bs(response.text, 'html.parser')
                #print soup # <-checks page status
                orderStatus =  str(soup.find("p", {"class":"longDescription"}))
                start = '<p class="longDescription">'
                end = '</p>'
                #while True:
                try:
                    newOrder = orderStatus.split(start)[1].split(end)[0]
                    orderStatus1 = datetime.now().strftime('%H:%M:%S | ') + 'Status of your purchase ['+str(customerInfo)+'] is: ' + str(newOrder)
                    print orderStatus1
                    #break
                except IndexError:
                    orderStatus2 = datetime.now().strftime('%H:%M:%S | ') + 'Status of your purchase ['+str(customerInfo)+'] is: CANCELLED!'
                    print orderStatus2

                infoLine = infoLine + 1


# main code below


print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print datetime.now().strftime('%H:%M:%S | ') + 'Size? Previews Order Checker by @donjawn(s)'
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print
userAnswer = raw_input(datetime.now().strftime('%H:%M:%S | ') + 'Would you like to check your Previews orders? Enter Y or N: ').lower()
if userAnswer == 'y':
    order_checker()
else:
    print "See ya later."
             

                
                

