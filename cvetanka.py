import requests
telegram_auth_token = "6368401381:AAHfDYoZrdflss1Xgb66RgGc4DGNUwFy_i0"
telegram_group_id = "statisticki_podatoci"

msg = "Imajte prekrasen den :) "
    
def send_msg_on_telegram(message):
    telegram_api_url = f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}&text={message}"
    telegram_resp =requests.get(telegram_api_url)

    if telegram_resp.status_code ==200:
        print("INFO: notification has been sent to telegram")
    else:
        print("ERROR: could not send a message")
    send_msg_on_telegram(msg)