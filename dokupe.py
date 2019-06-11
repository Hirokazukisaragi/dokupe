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

    def setLimit(self,Limitter):
        self.limitTime = Limitter

    def complete(self):
        print("完了しました")
        pass
class Maid(timer):
    def complete(self):
        print("お疲れ様です。")
        self.setLimit(60*30)
        self.count()
        print("ありがとうございます")
    def rest(self):
        print("休憩しませんか?")
    limit2 = 0
    def setLimit2(self,limit):
        self.limit2 = limit
print("hello")
m = Maid()
m.setLimit(1)
m.count()
m.complete()