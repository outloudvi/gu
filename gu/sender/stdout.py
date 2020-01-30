from .default import DefaultSender
import requests


class StdoutSender(DefaultSender):
    def sendText(self, text):
        print(text)
