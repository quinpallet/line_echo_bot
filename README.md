# line_echo_bot
Echo BOT on LINE

## Requirements

- [Google Cloud Functions](https://cloud.google.com/functions/)
- [LINE Developers (Messaging API)](https://developers.line.biz/ja/)

## Prerequisites

- Python >= 3.7
- line-bot-sdk >= 1.16.0

## Deployment

- [Google Cloud SDK](https://cloud.google.com/sdk/docs?hl=ja)

``` bash
$ gcloud functions deploy <function-name> --trigger-http
```

## Settings

- Environment Variables on *Google Cloud Functions*

    - **LINE_CHANNEL_ACCESS_TOKEN**: from Channel access token in Messaging API on LINE Developers Console
    - **LINE_CHANNEL_SECRET**: from Channel secret in Basic Settings on LINE Developers Console

- Webhook URL on *LINE Developer Console*

    - **Webhook URL**: from Google Cloud Functions

- Confirmation

``` bash
$ gcloud functions describe <function-name>
```

## License

&copy; 2020 [Ken Kurosaki](https://github.com/kenqlo).<br>
This project is [MIT](https://github.com/kenqlo/line_echo_bot/blob/master/LICENSE) licensed.