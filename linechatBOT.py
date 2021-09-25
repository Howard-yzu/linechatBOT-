#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
app = Flask(__name__)
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction

line_bot_api = LineBotApi('PUT_YOUR_LINE_TOKEN')
handler = WebhookHandler('PUT_YOUR_HEROKU_TOKEN')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '@傳送文字':
        try:
            message = TextSendMessage(
                text = "1073513 王辰豪"
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤'))
    
    elif mtext == "@傳送圖片":
        try:
            message = ImageSendMessage(
                original_content_url = "https://i.imgur.com/kYDpOEQ.jpg",
                preview_image_url = "https://i.imgur.com/kYDpOEQ.jpg"
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤'))    
    elif mtext == "@傳送貼圖":
        try:
            message = StickerSendMessage(
                package_id='1',
                sticker_id='2'
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤'))
    elif mtext == "@多項傳送":
        try:
            message = [
                StickerSendMessage(
                package_id='1',
                sticker_id='2'
                ),
                ImageSendMessage(
                original_content_url = "https://i.imgur.com/kYDpOEQ.jpg",
                preview_image_url = "https://i.imgur.com/kYDpOEQ.jpg"
                ),
                TextSendMessage(
                text = "1073513 王辰豪"
                )
            ]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤'))
    elif mtext == "@傳送位置":
        try:
            message = LocationSendMessage(
                title='元智大學',
                address='桃園市中壢區遠東路135號',
                latitude=24.970152,
                longitude=121.267498
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤'))
    elif mtext == "@快速選單":
        try:
            message = TextSendMessage(
                text='請選擇你最喜歡的課程',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="雲端運算", text="雲端運算")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="計算機網路概論", text="計算機網路概論")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="經典導讀", text="經典導讀")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="木球", text="木球")
                        ),
                    ]
                )
                
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤'))        
if __name__ == '__main__':
    app.run()


# In[ ]:




