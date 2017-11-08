class PubTest:
    def register(self,notifyFunc):
        self.notifyFunc = notifyFunc

    def notify(self,msg):
        self.notifyFunc(msg)