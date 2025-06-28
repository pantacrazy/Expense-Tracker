from CLI import just_parse
class Main:
    def __init__(self):
        pass
    def start(self):
        self.current=just_parse()
        self.current.identify_command()
if __name__=="__main__":
    main=Main()
    main.start()