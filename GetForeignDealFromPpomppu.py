from bs4 import BeautifulSoup
import requests
from datetime import datetime

def GetCurrentPPDay():
    now = datetime.now()
    nowYear = now.strftime('%Y')
    temp = int(nowYear) - 2000
    nowYear = str(temp)
    current = nowYear + "." + now.strftime('%m.%d')
    return current

def GetPPompuFeedFilterWord(word):
    ppUrl = 'http://www.ppomppu.co.kr/zboard/zboard.php'
    queryStr1 = "?id=ppomppu4&page="
    queryStr2 = "&divpage=20"

    listRet = []

    print("Search [" + word + "] in Hae PPom")

    for i in range(1, 5):
        queryStr = queryStr1 + str(i) + queryStr2
        url = ppUrl + queryStr

        res = requests.get(url)
        bs = BeautifulSoup(res.text, 'html.parser')

        # 게시판의 각 페이지당 20개의 List가 있는데 이 List Class Value가 List0, 1 이렇게 두 가지로 번갈아 가면서 있음
        # 따라서 각 페이지의 모든 리스트 아이템을 순회 하기 위해 2개의 Loop를 사용.
        list0 = bs.findAll('tr', class_='list0')
        list1 = bs.findAll('tr', class_='list1')

        # 뽐뿌에서 사용하는 날짜 양식에 맞게 현재 날짜 형태를 가공해서 가져옴.
        today = GetCurrentPPDay()

        for item in list0:
            # <td> 태그를 사용하여 현재 날짜를 파악 후 오늘이 아닌경우 Pass
            td = item.findAll('td')
            for tditem in td:
                # 유일하게 날짜를 표기하는 영역에서 title Attr을 사용하기에 구분자로 사용
                # [날짜 시간] 형태로 내려오기 때문에 날짜만 비교하기 위한 파싱 처리.
                if 'title' in tditem.attrs:
                    uploadTime = tditem.attrs['title']
                    spStr = str(uploadTime).split(' ')
                    if spStr is None:
                        continue
                    else:
                        if today == spStr[0]:
                            # 오늘 등록된 게시물일 경우 <font> 태그의 Class 명으로 게시물의 제목을 가져온다.
                            tt = item.find('font', class_='list_title')
                            # 내가 필터링 하고자 하는 단어가 포함 되어 있는지 체크
                            if word in tt.text:
                                print(tt.text)
                                listRet.append(tt.text)

        for item in list1:
            td = item.findAll('td')
            for tditem in td:
                if 'title' in tditem.attrs:
                    uploadTime = tditem.attrs['title']
                    spStr = str(uploadTime).split(' ')
                    if spStr is None:
                        continue
                    else:
                        if today == spStr[0]:
                            tt = item.find('font', class_='list_title')
                            if word in tt.text:
                                print(tt.text)
                                listRet.append(tt.text)



