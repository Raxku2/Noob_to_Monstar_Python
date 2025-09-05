from requests import get
from time import sleep
from notifypy import Notify
from dotenv import load_dotenv
from os import getenv

load_dotenv()
API = getenv('API_ENV_VAR')
notification = Notify()

def getNotice() -> list:
    """
    Makaut er notice API tekhe Latest Notice niye asche
    """
    res = get(API)
    latestNotices: list = []
    allData = res.json().get("data")
    for data in allData[:12]:
        latestNotices.append(
            [data.get("notice_date"), data.get("notice_title"), data.get("file_path")]
        )
    return latestNotices


def noticePrint(allNotices: list) -> None:
    for index,notice in enumerate(allNotices):
        print(f"{index+1:<3}. {notice[1]:<114} | Published: {notice[0]} | url: {notice[2]} \n")


def main():
    # print(allNotices)
    # noticePrint(allNotices)

    while True:
        lastReleasedNotice: str = ''
        with open("lastNotice.txt",'r') as file:
            lastReleasedNotice = file.read()

    # print(lastReleasedNotice)
        allNotices = getNotice()
        latestNotice = allNotices[0][1]

        if latestNotice == lastReleasedNotice:
            # purononotice, notun release koreni
            print('New notice Not released')
            
        elif latestNotice != lastReleasedNotice:

            notification.title = "New notice released"
            notification.message = f"{latestNotice}. view pdf: {allNotices[0][2]}"
            notification.send()

            # notun notice relesed
            # notification debe
            noticePrint(allNotices)
            # ei notice ta purono hoye jabe
            lastReleasedNotice = latestNotice

            with open("lastNotice.txt",'w') as file:
                file.write(latestNotice)
        
        else:
            print("error")
            exit()
    
        sleep(10)

main()
