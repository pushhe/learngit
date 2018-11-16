import requests
import json
import urllib.parse
import os

DIR = 'S:\\群组资料库\\Billiards_APK\\normal'
url = 'https://oapi.dingtalk.com/robot/send?access_token=444814e3e36a01fae7c2170ddbaebcebf06155d8758c274340b0f4a14a533f00'


# 获得最新apk包的名字
def APK_NAME(DIR):
    len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    lists = os.listdir(DIR)
    lists.sort(key=lambda fn: os.path.getmtime(DIR + "\\" + fn))
    new_file_name = (lists[-1])
    return new_file_name + '\n'


# 获取最新的版本说明
def home():
    l = []
    res = []
    x = 0
    with open('S:\\群组资料库\\Billiards_wiki\\home.md', 'r', encoding='UTF-8') as h:
        H = h.readlines()
        s = ''
        for line in H:
            if line[0:3] == '## ':
                l.append(line)
        first = H.index(l[0])
        last = H.index(l[1])
        for i in H:
            x += 1
            if first < x < last:
                res.append(i)
        for n in res:
            s = s + n
        # print(str(s))
        return str(s)


# 通过钉钉第三方接口发送消息
Msg = {"msgtype": "markdown", "markdown": {"title": "重磅消息！", "text": '## 我有新版本啦！→' + APK_NAME(DIR) + home()},
       "at": {"atMobiles": 18717397262, "isAtAll": True}}
String_textMsg = json.dumps(Msg)


def send_ding(String_textMsg):
    HEADERS = {"Content-Type": "application/json ;charset=utf-8 "}
    requests.post(url, data=String_textMsg, headers=HEADERS)


# 通过版本库中文件数量判断是否有新版本更新
def APK_NUM(DIR):
    with open('D:\\num.txt', 'r') as f1:
        now = int(f1.read())
    num = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    if num > now:
        send_ding(String_textMsg)
        with open('D:\\num.txt', 'w') as f2:
            f2.write(str(num))
    else:
        pass


if __name__ == '__main__':
    APK_NUM(DIR)
