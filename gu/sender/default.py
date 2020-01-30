class DefaultSender(object):
    _REQUIERD_PARAMS = {}
    _OPTIONAL_PARAMS = {}

    def __init__(self, obj):
        self.settings = obj

    def validateParams(self):
        for i in self._REQUIERD_PARAMS.keys():
            if self.settings.get(i) == None:
                return False
        return True

    def sendText(self, text):
        raise NotImplementedError
