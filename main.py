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
                    # 'cookie': 'ak_bmsc=36A56F8C1157B194D8CEB507D1C0E1A417D46C1E6D7F0000D5F1445BEFE2801E~plwGWb0mfd0F4i7wRkErtKiDTCChPMHul9emboMKqJj7v73R6qvPeFqlcCXWlIqQO9aooW6Oac+ccVq29t8f2GQV0BGosMlKHdI8V3cjNwDgn+RLqOzCvbFpnD19JDLrtiVVENwc+DYmyv4Nu/+VcnLBpe/MR7y4xO5l5cJQSiY/O0+AK1/+u81HGeNLOcvgFx/L2BcgMi9hZXupTc8Y38fQjFTp5tuX3TulNlDl0YmXI=; language=en; AKA_A2=A; session.present=1; session.ID=EB7BDEFFC0644BEC80857C44BD4CFDC7; bm_mi=C3E0A7EA1635CC414308EE01E48D544A~0eX/HUCP33Va1LPGX8ReejiYkdaVX6LuvCk+xQN/hF3lurJUe6xmBvnIzzAq/dXHtAAtie4CvuxymYQ/U7qbrztu88Ffl/Z+ISGgnIMKvb28ByhunUuJ6HD4lmj4pBEE47HVvHYH24cAkmKCTpRdgHIFnIhjdtHLavCQTaugkOzsx0lSMuO92tTnPbH+8ILhnMpE7dH0L5pKcDmBA5yeqw0PnSLs49EdyTWrNEhagIJD6kgWIiaQEgpAoE4hVQaXrmXiDPyWGcpikUbpdM3lHvzDtE0lXY4k2IJVDnEo5uM=; bm_sv=05B5F71155E14BF26F1665A58DAFD73A~tliDbA0Ollz5wgobz0w97Sym20M5tDLvi+IV+1n4K+yCWhFIhyghhfH39aon9TPzQZ4qUSCrvaokcuWPaWfCFdltaLPPQO5Cm1gP//XQqKu9NYtNeYpjrm+MSEc8ALlA58df+t/AEQeIazVHklJAR3Ex/TA//KSoYwcFiWfptfI=',
                    'if-none-match': 'ee4a1278e0f74b4981e0abee4f207a3c',
                    'if-modified-since': 'Tue, 10 Jul 2018 17:12:55 GMT',
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
                    #print newOrder
                    orderStatus1 = datetime.now().strftime('%H:%M:%S | ') + 'Status of your purchase ['+str(customerInfo)+'] is: ' + str(newOrder)
                    print orderStatus1
                    #break
                except IndexError:
                    orderStatus2 = datetime.now().strftime('%H:%M:%S | ') + 'Status of your purchase ['+str(customerInfo)+'] is: CANCELLED!'
                    #orderStatus2 = datetime.now().strftime('%H:%M:%S | ') + 'Status of your purchase is: CANCELLED!'
                    print orderStatus2

                infoLine = infoLine + 1


# main code below


print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print datetime.now().strftime('%H:%M:%S | ') + 'Size? Previews Order Checker by @donjawn(s)'
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print
print
userAnswer = raw_input(datetime.now().strftime('%H:%M:%S | ') + 'Would you like to check your Previews orders? Enter Y or N: ').lower()
if userAnswer == 'y':
    order_checker()
else:
    print "See ya later."
             

                
                

