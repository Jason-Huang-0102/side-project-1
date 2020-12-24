#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
@desc:  
@author: TsungHan Yu  
@contact: nick.yu@hzn.com.tw  
@software: PyCharm  @since:python 3.6.0 on 2017/7/13
"""

import os
import requests
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

ACCESS_TOKEN = 'y6LvPoZcy4C+SUEJWUDJOL3sQL/dEyf/+oHnaSyDqPZcfLIqrvroV5+79S6dxwB8KdZKBhxnLHuMRBGXwHYKXFAp6mtRgUdATbhxK66DnVmuYU3FXUoUy6lsjOx30MnHrX6S8YOJgN9ceeA9WCGyTAdB04t89/1O/w1cDnyilFU='
SECRET = 'fc4db154528f249104b54628de42203f'

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    # msg = msg.encode('utf-8')
    # app.logger.info("msg: " + msg)
    if msg=='123':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='哈囉'))
    else :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='不哈囉'))



if __name__ == "__main__":
    app.run()
