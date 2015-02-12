# -*- coding: cp949 -*-

__author__ = 'MuzikPooh'

import urllib, httplib
from bs4 import BeautifulSoup

rtnResult = []

class kyoboSearch():

    def search(key):

        param = urllib.urlencode({'vPejkGB':'EBK','vPreSearch':'1','vPviewCount':'1000','vPstrCategory':'DIG', 'vPplace':'top', 'vPsch':'1', 'vPstrKeyWord':key})
        headers = {"Content-type":"application/x-www-form-urlencoded"}
        conn = httplib.HTTPConnection("www.kyobobook.co.kr")
        conn.request("POST", "/search/SearchDigitoryMain.jsp", param, headers)
        response = conn.getresponse().read()
        resDec = response.decode('cp949')
        conn.close()

        rtn = []

        soup = BeautifulSoup(resDec)
        results = soup('ul', ['digital list-first','digital'])

        for result in results:

            resultTitle = result.find(class_='title list-center')
            rtnCategory = resultTitle.span.text
            rtnTitle = resultTitle.strong.text
            rtnLink = resultTitle.a['href']

            resultInfo = result.find(class_='addinfo01 list-center')
            rtnAuthor = resultInfo.find(class_='author').text
            rtnPublisher = resultInfo.find(class_='publisher').text
            rtnDate = resultInfo.find(class_='publisher').find_next('span').text

            rtnPrice = result.find(class_='real').text
            rtnType = result.find(class_='delivery list-center').text

            rtn = [rtnCategory, rtnTitle, rtnLink, rtnAuthor, rtnPublisher, rtnDate, rtnPrice, rtnType]
            rtnResult.append(rtn)
        #print rtnResult
        return rtnResult

    search('거실')