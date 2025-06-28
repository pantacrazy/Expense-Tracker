import argparse
from cvi_handler import data_processing
commands=['add','list','summary','delete','update','save']
class just_parse:
    def __init__(self):
        parser =argparse.ArgumentParser(prog="Expense Tracker",description="A simple expense tracker to manage your finances")
        parser.add_argument('command')
        parser.add_argument('--description')
        parser.add_argument('--amount')
        parser.add_argument('--id')
        parser.add_argument('--month')
        parser.add_argument('--name')
        self.args=parser.parse_args()
    def identify_command(self):
        if self.args.command not in commands:
            print("Incorrect Command")
        else:
            match self.args.command:
                case 'add':
                    self.add_expense()
                case 'list':
                    self.list()
                case 'summary':
                    self.summary()
                case 'delete':
                    self.delete()
                case 'save':
                    self.save()
    def add_expense(self):
        if not (self.args.id or self.args.month or self.args.name):
            if not self.args.description:
                print("Missing description")
            else:
                if not self.args.amount:
                    print('Missing amount')
                else:
                    data=data_processing()
                    data.add(self.args.description,self.args.amount)
        else:
            print("Command not allowed")
    def list(self):
        data=data_processing()
        data.list()
    def summary(self):
        data=data_processing()
        if self.args.month:
            data.summary(self.args.month)
        else:
            data.summary()
    def delete(self):
        if not self.args.id:
            print("Missing id")
        else:
            data=data_processing()
            data.delete(self.args.id)
    def save(self):
        data=data_processing()
        data.save(self.args.name)