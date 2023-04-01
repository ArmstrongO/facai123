import requests

def yiyan():
    # 要抓取链接的网站
    url = "http://api.btstu.cn/sjbz/"
    # url = "https://www.miyoushe.com/ys/home/49"
    # 要保存链接的文件名
    # filename = r"C:\Users\Administrator\Desktop\1\meib.txt"
    filename = r"C:\Users\Administrator\Desktop\1\mimi.txt"
    # 发送HTTP请求并获取响应
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/B08C390B",
            "Referer": url
        }
        response = requests.get ( url, headers=headers, timeout=10 )
        if response.status_code == 200:
            redirect_urls = []
            for url in response.history:
                if url.url.endswith ( ".jpg" ):
                    redirect_urls.append ( url.url )
            if response.url.endswith ( ".jpg" ):
                redirect_urls.append ( response.url )
            # 将所有以".jpg"结尾的URL保存到文件
            with open ( filename, "a" ) as f:
                for url in redirect_urls:
                    f.write ( url + "\n" )
                    print(url)
    except Exception as e:
        print ( e )


for n in range ( 1, 50 ):
    yiyan ()