from bs4 import BeautifulSoup
import re
import urllib
import xlwt
import sqlite3


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }
    # req = urllib.request.Request(url, header=head)
    req = urllib.request.Request(url, head=head)
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式，表示规则（字符串的模式）
findImage = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        # 2.解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串形成列表
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImage, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)[0]
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                ottitle = titles[1].replace("/", "")
                data.append(ottitle)
            else :
                data.append(title[0])
                data.append(' ')
            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)
            if len(inq)!=0:
                inq=inq[0].replace("。 ","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            bd = re.sub('/', bd)
            data.append(bd.strip())

            datalist.append(data)

    return datalist


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影top250.xls"
    # saveData(savepath)


# def saveData(savepath):
#     print("save...")

if __name__ == "__main__":
    main()
