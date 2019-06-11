from time import sleep


class timer:
    counter = 0
    limitTime = 0
    def reset(self):
        self.counter = 0;
    def setLimit(self,limit):
        self.limitTime = limit
    def count(self):
        while True:
            self.counter+=1
            sleep(1)
            if(self.counter >= self.limitTime):
                break;
        self.complete()
    def setLimit(self,Limitter):
        self.limitTime = Limitter

    def complete(self):
        print("完了しました")
        pass
c = timer()
c.setLimit(10)
c.count()
