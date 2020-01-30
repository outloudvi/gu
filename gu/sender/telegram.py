from .default import DefaultSender
import requests


class TelegramSender(DefaultSender):

    _REQUIERD_PARAMS = {
        "username_or_userid": "Your telegram @username, or user ID",
        "bot_token": "Bot token, like 123:RandomString"
    }

    _OPTIONAL_PARAMS = {
        "parse_mode": "Style. Markdown or HTML."
    }

    def __init__(self, obj):
        self.settings = obj
        if self.settings.get("parse_mode") != "markdown":
            self.settings["parse_mode"] = "html"

    def sendText(self, text):
        r = requests.post(
            "https://api.telegram.org/bot{}/sendMessage".format(self.settings["bot_token"]), json={
                "chat_id": self.settings["username_or_userid"],
                "text": text,
                "parse_mode": self.settings["parse_mode"]
            })
        if r.status_code != 200:
            return (False, r.json()["description"])
        else:
            return True
