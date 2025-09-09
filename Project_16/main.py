from requests import get
from bs4 import BeautifulSoup
from time import sleep
from notifypy import Notify


URL = input("Enter Product Url : ")

old_price = 0
notification = Notify()


def main():
    res = get(URL)
    res_html = res.text
    soup = BeautifulSoup(res_html, "html.parser")
    product_title = soup.find("span", id="productTitle").get_text(strip=True)

    print(f"Tracking Start for : {product_title}\n")

    current_price = soup.find("span", class_="a-price-whole").get_text()
    current_price_num = int(current_price.replace(".", "").replace(",", ""))

    print("Price : ", current_price_num)
    old_price = current_price_num
    notification.title = "Price Tracker"
    notification.message = f"Tracking Start for : {product_title}"
    notification.send()

    while True:
        res = get(URL)
        res_html = res.text
        soup = BeautifulSoup(res_html, "html.parser")
        current_price = soup.find("span", class_="a-price-whole").get_text()
        current_price_num = int(current_price.replace(".", "").replace(",", ""))

        if current_price_num != old_price:
            if old_price > current_price_num:
                print("Price Drop Alert!! ")
            else:
                print("Price Increase Alert!!")

            print(f"New Price : {current_price_num}")
            notification.title = "Price Tracker"
            notification.message = f"New Price : {current_price_num}"
            notification.send()
            old_price = current_price_num

            # new price
        else:
            print("no change")

        sleep(5)


main()
