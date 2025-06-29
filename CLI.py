import argparse
from cvi_handler import data_processing
class just_parse:
    def __init__(self):
        parser =argparse.ArgumentParser(prog="Expense Tracker",description="A simple expense tracker to manage your finances")
        subparser=parser.add_subparsers(dest='command')
        #add parser
        add_parser=subparser.add_parser('add')
        add_parser.add_argument('--description',required=True)
        add_parser.add_argument('--amount',required=True,type=int)
        add_parser.add_argument('--category')
        #list parser
        list_parser=subparser.add_parser('list')
        list_parser.add_argument('--category')
        #summary parser
        summary_parser=subparser.add_parser('summary')
        summary_parser.add_argument('--month',type=self.int_1_12)
        #delete parser
        delete_parser=subparser.add_parser('delete')
        delete_parser.add_argument('--id',required=True,type=int)
        #budget parser
        budget_parser=subparser.add_parser('set_budget')
        budget_parser.add_argument('--month',type=self.int_1_12)
        budget_parser.add_argument('--amount',type=int)
        #save parser
        save_parser=subparser.add_parser('save')
        #update parser
        update_parser=subparser.add_parser('update')
        update_parser.add_argument('--id',required=True)
        update_parser.add_argument('--amount',type=int)
        update_parser.add_argument('--category')
        update_parser.add_argument('--description')
        #parse
        self.args=parser.parse_args()
    def identify_command(self):
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
            case 'set-budget':
                self.set_budget()
            case 'update':
                self.update()
    def add_expense(self):
        data=data_processing()
        if self.args.category:
            category=self.args.category
        else:
            category=None
        data.add(self.args.description,self.args.amount,category)
    def list(self):
        data=data_processing()
        if self.args.category:
            data.list(self.args.category)
        else:
            data.list()
    def summary(self):
        data=data_processing()
        if self.args.month:
            print (data.summary(self.args.month))
        else:
           print(data.summary())
    def delete(self):
        data=data_processing()
        data.delete(self.args.id)
    def save(self):
        data=data_processing()
        data.save(self.args.name)
    def set_budget(self):
        data=data_processing()
        data.set_budget(self.args.month,self.args.amount)
    def update(self):
        data=data_processing()
        if self.args.description or self.args.amount or self.args.category:
            if self.args.description:
                description=self.args.description
            else:
                description=None
            if self.args.amount:
                amount=self.args.amount
            else:
                amount=None
            if self.args.category:
                category=self.args.category
            else:
                category=None
            data.update(self.args.id,description,amount,category)
        else:
            print('Missing Arguments')
    def int_1_12(self,value):
        try:
            num=int(value)
        except ValueError:
            raise argparse.ArgumentTypeError('Not a number')
        if num<1 or num>12:
            raise argparse.ArgumentTypeError('Not a number between 1 and 12')
        return num