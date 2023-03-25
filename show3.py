from time import sleep
class Clock():
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    def timerun(self):
        self.second+=1
        if self.second>=60:
            self.minute+=1
            self.second-=60
            if self.minute>=60:
                self.minute-=60
                self.hour+=1
                if self.hour>=24:
                    self.hour-=24
    def timeprint(self):
        print(f"{self.hour}:{self.minute}:{self.second}")

def main():
    clock = Clock(0, 0, 0)
    while True:
        clock.timeprint()
        sleep(1)
        clock.timerun()


if __name__ == '__main__':
    main()