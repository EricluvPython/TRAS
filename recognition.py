import requests
import json
import base64
import os
import logging
import speech_recognition as sr
import wx
import threading


def get_token():  # connect to BaiduCloud Voice Recognition API
    logging.info('Retrieving token...')
    baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    client_id = "EUON57v2pcpk5CDQnet6AN6s"
    client_secret = "oHb0INPt5MGSC4LfoQ9hd7W2oSR6GLmV"
    url = f"{baidu_server}grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}"
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    return token


def audio_baidu(filename):  # upload audio file and save result into history.txt
    if not os.path.exists('record'):
        os.makedirs('record')
    filename = 'record/' + filename
    logging.info('Analysing audio file...')
    with open(filename, "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf-8')
    size = os.path.getsize(filename)
    token = get_token()
    headers = {'Content-Type': 'application/json'}
    url = "https://vop.baidu.com/server_api"
    data = {
        "format": "wav",
        "rate": "16000",
        "dev_pid": 1737,  # 17372=enhanced english, 15372=enhanced chinese
        "speech": speech,
        "cuid": "3.141592653589793238462643383279502884197169399375105820",
        "len": size,
        "channel": 1,
        "token": token,
    }

    req = requests.post(url, json.dumps(data), headers)
    result = json.loads(req.text)

    if result["err_msg"] == "success.":
        message = ''.join(result['result'])
        print('RETURNED: ' + message)
        return result['result']
    else:
        print("RETURNED: Recognition failure")
        return -1


def main():  # Thread 2: voice recognition
    logging.basicConfig(level=logging.INFO)

    wav_num = 0
    while True:
        r = sr.Recognizer()
        mic = sr.Microphone()
        logging.info('Recording...')
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=1000)
        with open('record/' + f"00{wav_num}.wav", "wb") as f:
            f.write(audio.get_wav_data(convert_rate=16000))
        message = ''.join(audio_baidu(f"00{wav_num}.wav"))
        history = open('record/' + f"history.txt", "a")
        history.write(message + '\n')
        history.close()

        wav_num += 1


def update_content(win, height=200, width=800):
    f = open('record/' + f"history.txt", "r")
    try:
        last_line = f.readlines()[-1]
    except IndexError:
        last_line = ''
    if last_line.strip('\n') in ['key point', 'Yahoo']:  # Emphasize when heard words
        logging.info('Emphasized')
        ft = wx.Font(80, wx.MODERN, wx.NORMAL, wx.BOLD, False, '')
    else:
        ft = wx.Font(50, wx.MODERN, wx.NORMAL, wx.NORMAL, False, '')
    richText = wx.TextCtrl(win, value='', pos=(0, 0), size=(width, height))
    richText.SetInsertionPoint(0)
    richText.SetFont(ft)
    richText.SetValue(last_line)
    f.close()
    return last_line


def show_win(x=320, y=550, height=200, width=800):  # create GUI
    win = wx.Frame(None, title="Zimujun v1.0.0", pos=(x, y), size=(width, height), style=wx.STAY_ON_TOP)
    win.SetTransparent(1000)
    win.Show()

    return win


# here starts main function
if __name__ == "__main__":
    history = open('record/' + f"history.txt", "w+")
    history.close()

    thread = threading.Thread(target=main)
    thread.start()

    global app
    app = wx.App()
    while True:
        win = show_win()
        v = update_content(win)
        wx.CallLater(2000, win.Destroy)
        app.MainLoop()
