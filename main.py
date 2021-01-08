import os
import base64
import hashlib
import hmac

from flask import abort

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


def main(request):
    """This is a LINE Bot function

    Args:
        request (flask.Request): [description]

    Returns:
        Response|HTTPException: [description]
    """

    # LINEアプリ設定（環境変数）
    channel_secret = os.environ.get('LINE_CHANNEL_SECRET')
    channel_access_token = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')

    # LINE Bot(Messaging) API
    line_bot_api = LineBotApi(channel_access_token)
    parser = WebhookParser(channel_secret)

    # WebhookリクエストからBODYを取得
    body = request.get_data(as_text=True)

    # チャネルの秘密鍵からシグネチャを取得
    hashcode = hmac.new(
        channel_secret.encode('utf-8'),
        body.encode('utf-8'),
        hashlib.sha256).digest()
    signature = base64.b64encode(hashcode).decode()

    # シグネチャの合致判定
    if signature != request.headers['X_LINE_SIGNATURE']:
        return abort(405)

    # リクエストボディからWebhookイベントオブジェクト（Payload）を取得
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        return abort(405)

    # Webhookイベントオブジェクトを処理
    for event in events:
        if not isinstance(event, MessageEvent):  # メッセージイベント以外は未処理
            continue
        if not isinstance(event.message, TextMessage):  # テキスト以外は未処理
            continue

        if event.message.text == u'おわり':  # エコーバックしないワードの処理
            # 「おわり」というメッセで「ほんとに？」を返す
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=u"ほんとに？")
            )
        else:
            # 上記以外のメッセはそのままオウム返し
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=event.message.text)
            )

    return ("", 200)
