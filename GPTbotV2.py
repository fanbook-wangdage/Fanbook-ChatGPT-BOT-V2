import requests#http请求
import json#json数据处理
import traceback#错误捕获
import urllib.request
import time#延时
import platform
import psutil
import ctypes
import subprocess
import sys#系统组件
import os#系统组件
import datetime
import chardet
import websocket#ws接口链接
import base64#请求体编码
import threading
import queue
import tkinter as tk#图形界面
from tqdm import tqdm#进度条
from pygments import highlight#高亮
from pygments.lexers import JsonLexer#高亮
from pygments.formatters import TerminalFormatter#高亮
from colorama import init, Fore, Back, Style#高亮
from tkinter import filedialog#窗口
import urllib.request
import librosa

def get_audio_duration(url):
    try:
        # 要下载的文件的URL
        file_url = url

        # 从URL中提取文件名
        file_name = os.path.basename(file_url)

        # 构建文件的保存路径
        save_path = os.path.join(os.getcwd(), file_name)
        filename=r"C:\Users\Administrator\Desktop\output\\"+file_name
        # 下载文件并保存到程序根目录
        urllib.request.urlretrieve(url, filename)
        print(f"文件已下载到：{filename}")
    except Exception as e:
        print(f"下载出错：{e}")
    # 获取音频文件的时长
    filepath = filename
    duration = librosa.get_duration(filename=filepath)
    # 获取到的时长单位为秒
    return duration

'''
url = "https://speech.ai.xiaomi.com/speech/1.0/tts_token?token=eyJ2IjoiVjAiLCJuIjoiU1oifQ.AAAXUkp9P1QAFgBdFAwbZ24VTkoaRRsPG2AFFhgAQgBIRyIvRw4PfR9GGBh0VUBPEQhHWxBrPkBITxBDEFhHb1RHT0FXEw0QY20QRU4AWgBZTTJVQQ4YTE9KEXF2AAkUSRNMGBh0XUdeQRtQQ31hahBOGRJPQwlGMwUXHBFdQV5ANmhBTk0UTkEPFW4BQXMUWUECR2A-QEtIEkJHXBM3VRtKFQsSAxpgYxceGBVFEBRPJgMAAAAKR0xLMD99FB8ATABeR2NVQBlHWw8KEjE7D0kaERcPAkBlBA8YR1tEDkBqbxQcQhNUDhhLN0QAFhNYGwkTY2IVSkMOVEdCUnQKExobXRACE2ZtGgA.EO5fMqpLGoC6LrZI3pQP5w"
audio_duration = get_audio_duration(url)
print(f"音频时长：{audio_duration} 秒")
'''
ms='0'
lingpai='50357763a9034c9b8e16911c3319a7'
pdid=433212507046281216
sycyid=[]#使用成员id
cysycs=[]#成员使用次数
jgczsj=0#警告重置时间
gjc=''#绘图关键词

init(autoreset=True)    #  初始化，并且设置颜色设置自动恢复
def addmsg(msg, color="white"):
    if color == "white":
        print(msg)
    elif color == "red":
        print("\033[31m" + msg + "\033[39m")
    elif color == "yellow":
        print("\033[33m" + msg + "\033[39m")
    elif color == "green":
        print("\033[32m" + msg + "\033[39m")
    elif color == "aqua":
        print("\033[36m" + msg + "\033[39m")

def colorprint(smg2,pcolor):
    if pcolor=='red':
      print(Fore.RED + smg2)
    elif pcolor=='bandg':
      print(Back.GREEN + smg2)
    elif pcolor=='d':
      print(Style.DIM + smg2)
    # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
    #print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True
    
def colorize_json(smg2,pcolor=''):
    json_data=smg2
    try:
        parsed_json = json.loads(json_data)  # 解析JSON数据
        formatted_json = json.dumps(parsed_json, indent=4)  # 格式化JSON数据

        # 使用Pygments库进行语法高亮
        colored_json = highlight(formatted_json, JsonLexer(), TerminalFormatter())

        print(colored_json)
    except json.JSONDecodeError as e:
        print(json_data)
allrw='空, 荧, 派蒙, 纳西妲, 阿贝多, 温迪, 枫原万叶, 钟离, 荒泷一斗, 八重神子, 艾尔海森, 提纳里, 迪希雅, 卡维, 宵宫, 莱依拉, 赛诺, 诺艾尔, 托马, 凝光, 莫娜, 北斗, 神里绫华, 雷电将军, 芭芭拉, 鹿野院平藏, 五郎, 迪奥娜, 凯亚, 安柏, 班尼特, 琴, 柯莱, 夜兰, 妮露, 辛焱, 珐露珊, 魈, 香菱, 达达利亚, 砂糖, 早柚, 云堇, 刻晴, 丽莎, 迪卢克, 烟绯, 重云, 珊瑚宫心海, 胡桃, 可莉, 流浪者, 久岐忍, 神里绫人, 甘雨, 戴因斯雷布, 优菈, 菲谢尔, 行秋, 白术, 九条裟罗, 雷泽, 申鹤, 迪娜泽黛, 凯瑟琳, 多莉, 坎蒂丝, 萍姥姥, 罗莎莉亚, 留云借风真君, 绮良良, 瑶瑶, 七七, 奥兹, 米卡, 夏洛蒂, 埃洛伊, 博士, 女士, 大慈树王, 三月七, 娜塔莎, 希露瓦, 虎克, 克拉拉, 丹恒, 希儿, 布洛妮娅, 瓦尔特, 杰帕德, 佩拉, 姬子, 艾丝妲, 白露, 星, 穹, 桑博, 伦纳德, 停云, 罗刹, 卡芙卡, 彦卿, 史瓦罗, 螺丝咕姆, 阿兰, 银狼, 素裳, 丹枢, 黑塔, 景元, 帕姆, 可可利亚, 半夏, 符玄, 公输师傅, 奥列格, 青雀, 大毫, 青镞, 费斯曼, 绿芙蓉, 镜流, 信使, 丽塔, 失落迷迭, 缭乱星棘, 伊甸, 伏特加女孩, 狂热蓝调, 莉莉娅, 萝莎莉娅, 八重樱, 八重霞, 卡莲, 第六夜想曲, 卡萝尔, 姬子, 极地战刃, 布洛妮娅, 次生银翼, 理之律者, 真理之律者, 迷城骇兔, 希儿, 魇夜星渊, 黑希儿, 帕朵菲莉丝, 天元骑英, 幽兰黛尔, 德丽莎, 月下初拥, 朔夜观星, 暮光骑士, 明日香, 李素裳, 格蕾修, 梅比乌斯, 渡鸦, 人之律者, 爱莉希雅, 爱衣, 天穹游侠, 琪亚娜, 空之律者, 终焉之律者, 薪炎之律者, 云墨丹心, 符华, 识之律者, 维尔薇, 始源之律者, 芽衣, 雷之律者, 苏莎娜, 阿波尼亚, 陆景和, 莫弈, 夏彦, 左然'
allrw=allrw.split(', ')
print(allrw)
xz=''
false=False
data_queue = queue.Queue()
def on_message(ws, message):
    global ms
    global xz
    global sycyid,cysycs,jgczsj
    global gjc
    # 处理接收到的消息
    addmsg('收到消息',color='green')
    colorize_json(message)
    message=json.loads(message)
    if message["action"] =="push":
        if message["data"]["author"]["bot"] == false:
            content = json.loads(message["data"]["content"])
            userid=message["data"]["user_id"]
            if "${@!469790724255502336}" in content['text']:
                if userid in sycyid:
                    sycy=sycyid.index(userid)
                    cysycs[sycy]+=1
                    print('用户id:',userid,'使用次数增加1,原本次数为：',cysycs[sycy])
                else:
                    sycyid.append(userid)
                    cysycs.append(1)
                    print('新使用用户：',userid)
                    print(sycyid)
                    print(cysycs)
                if int(cysycs[sycyid.index(userid)]) == 5:
                    print('用户：',userid,'第5次操作')
                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({
                    "chat_id":int(message["data"]["channel_id"]),
                    "text": '速率限制：\n你当前给机器人发送消息数超过每两分钟4次，请休息一下，两分钟后再来吧',
                    "reply_to_message_id":int(message["data"]["message_id"])
                    })
                    print(jsonfile)
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    colorize_json(smg2=postreturn.text,pcolor='d')
                elif int(cysycs[sycyid.index(userid)]) < 5:
                    if '模式切换' in content['text']:
                        if ms=='0':
                            ms='1'
                            xz=''
                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                            headers = {'content-type':"application/json;charset=utf-8"}
                            jsonfile=json.dumps({
                            "chat_id":int(message["data"]["channel_id"]),
                            "text": '回复模式已切换为语音回复模式(默认为派蒙[喵娘属性])\n可通过快捷指令[切换人物]切换，此操作对所有服务器均生效，请勿频繁操作',
                            "reply_to_message_id":int(message["data"]["message_id"])
                            })
                            print(jsonfile)
                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                            colorize_json(smg2=postreturn.text,pcolor='d')
                        else:
                            ms='0'
                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                            headers = {'content-type':"application/json;charset=utf-8"}
                            jsonfile=json.dumps({
                            "chat_id":int(message["data"]["channel_id"]),
                            "text": '回复模式已切换为文本模式，此操作对所有服务器均生效，请勿频繁操作',
                            "reply_to_message_id":int(message["data"]["message_id"])
                            })
                            print(jsonfile)
                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                            colorize_json(smg2=postreturn.text,pcolor='d')
                    elif '可选人物' in content['text']:
                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                        headers = {'content-type':"application/json;charset=utf-8"}
                        jsonfile=json.dumps({
                        "chat_id":int(message["data"]["channel_id"]),
                        "text": '所有可选人物列表：空, 荧, 派蒙, 纳西妲, 阿贝多, 温迪, 枫原万叶, 钟离, 荒泷一斗, 八重神子, 艾尔海森, 提纳里, 迪希雅, 卡维, 宵宫, 莱依拉, 赛诺, 诺艾尔, 托马, 凝光, 莫娜, 北斗, 神里绫华, 雷电将军, 芭芭拉, 鹿野院平藏, 五郎, 迪奥娜, 凯亚, 安柏, 班尼特, 琴, 柯莱, 夜兰, 妮露, 辛焱, 珐露珊, 魈, 香菱, 达达利亚, 砂糖, 早柚, 云堇, 刻晴, 丽莎, 迪卢克, 烟绯, 重云, 珊瑚宫心海, 胡桃, 可莉, 流浪者, 久岐忍, 神里绫人, 甘雨, 戴因斯雷布, 优菈, 菲谢尔, 行秋, 白术, 九条裟罗, 雷泽, 申鹤, 迪娜泽黛, 凯瑟琳, 多莉, 坎蒂丝, 萍姥姥, 罗莎莉亚, 留云借风真君, 绮良良, 瑶瑶, 七七, 奥兹, 米卡, 夏洛蒂, 埃洛伊, 博士, 女士, 大慈树王, 三月七, 娜塔莎, 希露瓦, 虎克, 克拉拉, 丹恒, 希儿, 布洛妮娅, 瓦尔特, 杰帕德, 佩拉, 姬子, 艾丝妲, 白露, 星, 穹, 桑博, 伦纳德, 停云, 罗刹, 卡芙卡, 彦卿, 史瓦罗, 螺丝咕姆, 阿兰, 银狼, 素裳, 丹枢, 黑塔, 景元, 帕姆, 可可利亚, 半夏, 符玄, 公输师傅, 奥列格, 青雀, 大毫, 青镞, 费斯曼, 绿芙蓉, 镜流, 信使, 丽塔, 失落迷迭, 缭乱星棘, 伊甸, 伏特加女孩, 狂热蓝调, 莉莉娅, 萝莎莉娅, 八重樱, 八重霞, 卡莲, 第六夜想曲, 卡萝尔, 姬子, 极地战刃, 布洛妮娅, 次生银翼, 理之律者, 真理之律者, 迷城骇兔, 希儿, 魇夜星渊, 黑希儿, 帕朵菲莉丝, 天元骑英, 幽兰黛尔, 德丽莎, 月下初拥, 朔夜观星, 暮光骑士, 明日香, 李素裳, 格蕾修, 梅比乌斯, 渡鸦, 人之律者, 爱莉希雅, 爱衣, 天穹游侠, 琪亚娜, 空之律者, 终焉之律者, 薪炎之律者, 云墨丹心, 符华, 识之律者, 维尔薇, 始源之律者, 芽衣, 雷之律者, 苏莎娜, 阿波尼亚, 陆景和, 莫弈, 夏彦, 左然\n请使用切换人物指令切换，仅在语音回复模式生效',
                        "reply_to_message_id":int(message["data"]["message_id"])
                        })
                        print(jsonfile)
                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                        colorize_json(smg2=postreturn.text,pcolor='d')
                    elif '切换人物' in content['text']:
                        xz=content['text'][31:-1]
                        print(xz)
                        if xz in allrw:
                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                            headers = {'content-type':"application/json;charset=utf-8"}
                            jsonfile=json.dumps({
                            "chat_id":int(message["data"]["channel_id"]),
                            "text": '人物已切换为:'+xz+'\n此操作对所有服务器均生效，请勿频繁操作',
                            "reply_to_message_id":int(message["data"]["message_id"])
                            })
                            print(jsonfile)
                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                            colorize_json(smg2=postreturn.text,pcolor='d')
                        else:
                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                            headers = {'content-type':"application/json;charset=utf-8"}
                            jsonfile=json.dumps({
                            "chat_id":int(message["data"]["channel_id"]),
                            "text": '找不到你选择的人物：'+xz+'\n请确认你输入的人物在可选人物列表中',
                            "reply_to_message_id":int(message["data"]["message_id"])
                            })
                            print(jsonfile)
                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                            colorize_json(smg2=postreturn.text,pcolor='d')
                    
                    elif 'testAI绘图' in content['text']:
                        gjc=content['text'][31:-1]
                        print('关键词:',gjc)
                        htmessage=requests.get('https://api.lolimi.cn/api/ai/mj1?key=sWlckPY0hlgaDryj7hnLewOjTU&msg='+str(gjc), stream=True)
                        htmessage=json.loads(htmessage.text)
                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                        headers = {'content-type':"application/json;charset=utf-8"}
                        jsonfile=json.dumps({
                        "chat_id":int(message["data"]["channel_id"]),
                        "text":str(htmessage.text['']),
                        "reply_to_message_id":int(message["data"]["message_id"])
                        })
                        print(jsonfile)
                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                        colorize_json(smg2=postreturn.text,pcolor='d')
                    
                    else:
                        if ms=='0':
                            #text=json.loads(content)
                            print('文本模式回复')
                            print(content['text'])
                            print(content['text'][23:])
                            chatmessage=requests.get('https://api.lolimi.cn/api/ai/a?key=sWlckPY0hlgaDryj7hnLewOjTU&msg='+content['text'][23:], stream=True)
                            chatmessage=json.loads(chatmessage.text)
                            print(chatmessage)
                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                            headers = {'content-type':"application/json;charset=utf-8"}
                            jsonfile=json.dumps({
                            "chat_id":int(message["data"]["channel_id"]),
                            "text": chatmessage['data']['output'],
                            "reply_to_message_id":int(message["data"]["message_id"])
                            })
                            print(jsonfile)
                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                            colorize_json(smg2=postreturn.text,pcolor='d')
                        elif ms=='1':
                            print('音频模式回复')
                            print(content['text'])
                            print(content['text'][23:])
                            if xz == '':
                                chatmessage=requests.get('https://api.lolimi.cn/api/ai/ya?key=sWlckPY0hlgaDryj7hnLewOjTU&msg='+content['text'][23:], stream=True)
                            else:
                                chatmessage=requests.get('https://api.lolimi.cn/api/ai/ya?key=sWlckPY0hlgaDryj7hnLewOjTU&msg='+content['text'][23:]+'&speaker='+xz, stream=True)
                            chatmessage=json.loads(chatmessage.text)
                            print(chatmessage)
                            print(chatmessage['data']['output'])
                            url = chatmessage['data']['output']
                            audio_duration = get_audio_duration(str(url))
                            print(f"音频时长：{audio_duration} 秒")
                            xx='{"type": "voice","url": "'+chatmessage['data']['output']+'","second": '+str(int(audio_duration))+',"isRead": false}'
                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                            headers = {'content-type':"application/json;charset=utf-8"}
                            jsonfile=json.dumps({
                            "chat_id":int(message["data"]["channel_id"]),
                            "text": xx,
                            "reply_to_message_id":int(message["data"]["message_id"])
                            })
                            print(jsonfile)
                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                            colorize_json(smg2=postreturn.text,pcolor='d')
                else:
                    print('用户：',userid,'已经操作过快，忽略输入')
        # 在这里添加你希望执行的操作
def on_error(ws, error):
    # 处理错误
    addmsg("发生错误:"+str(error),color='red')
    error=traceback.format_exc()
    print(error)
def on_close(ws):
    # 连接关闭时的操作
    addmsg("连接已关闭",color='red')
def on_open(ws):
    # 连接建立时的操作
    addmsg("连接已建立",color='green')
    # 发送心跳包
    def send_ping():
        print('发送：{"type":"ping"}')
        ws.send('{"type":"ping"}')
    send_ping()  # 发送第一个心跳包
    # 定时发送心跳包
    def schedule_ping():
        send_ping()
        # 每25秒发送一次心跳包
        websocket._get_connection()._connect_time = 0  # 重置连接时间，避免过期
        ws.send_ping()
        websocket._get_connection().sock.settimeout(70)
        ws.send('{"type":"ping"}')
    websocket._get_connection().run_forever(ping_interval=25, ping_payload='{"type":"ping"}', ping_schedule=schedule_ping)
# 替换成用户输入的BOT令牌
lingpai = lingpai
url = f"https://a1.fanbook.mobi/api/bot/{lingpai}/getMe"
# 发送HTTP请求获取基本信息
response = requests.get(url)
data = response.json()
def send_data_thread():
    global sycyid,cysycs,jgczsj
    while True:
        # 在这里编写需要发送的数据
        time.sleep(25)
        ws.send('{"type":"ping"}')
        addmsg('发送心跳包：{"type":"ping"}',color='green')
        jgczsj+=1
        print('当前警告重置时间：',str(jgczsj))
        if jgczsj >= 10:
            print('警告重置')
            jgczsj=0
            sycyid=[]#使用成员id
            cysycs=[]#成员使用次数
if response.ok and data.get("ok"):
    user_token = data["result"]["user_token"]
    device_id = "your_device_id"
    version_number = "1.6.60"
    super_str = base64.b64encode(json.dumps({
        "platform": "bot",
        "version": version_number,
        "channel": "office",
        "device_id": device_id,
        "build_number": "1"
    }).encode('utf-8')).decode('utf-8')
    ws_url = f"wss://gateway-bot.fanbook.mobi/websocket?id={user_token}&dId={device_id}&v={version_number}&x-super-properties={super_str}"
    threading.Thread(target=send_data_thread, daemon=True).start()
    # 建立WebSocket连接
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
else:
    addmsg("无法获取BOT基本信息，请检查令牌是否正确。",color='red')
'''
xx='{"type": "voice","url": "https://speech.ai.xiaomi.com/speech/1.0/tts_token?token=eyJ2IjoiVjAiLCJuIjoiU1oifQ.AAAXUkp9P1QAFgBdFAwbZ24VTkoaRRsPG2AFFhgAQgBIRyIvRw4PfR9GGBh0VUBPEQhHWxBrPkBITxBDEFhHb1RHT0FXEw0QY20QRU4AWgBZTTJVQQ4YTE9KEXF2AAkUSRNMGBh0XUdeQRtQQ31hahBOGRJPQwlGMwUXHBFdQV5ANmhBTk0UTkEPFW4BQXMUWUECR2A-QEtIEkJHXBM3VRtKFQsSAxpgYxceGBVFEBRPJgMAAAAKR0xLMD99FB8ATABeR2NVQBlHWw8KEjE7D0kaERcPAkBlBA8YR1tEDkBqbxQcQhNUDhhLN0QAFhNYGwkTY2IVSkMOVEdCUnQKExobXRACE2ZtGgA.EO5fMqpLGoC6LrZI3pQP5w","second": '+str(int(audio_duration))+',"isRead": false}'

url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
headers = {'content-type':"application/json;charset=utf-8"}
jsonfile=json.dumps({
"chat_id":int(pdid),
"text": xx
})
postreturn=requests.post(url,data=jsonfile,headers=headers)
colorize_json(smg2=postreturn.text,pcolor='d')
'''