import csv,time,os
csv_file_name='csv_basic.csv'
field_names=['id','description','amount','date','category']
class data_processing:
    def __init__(self):
        self.csv_data=[]
        if os .path.exists(csv_file_name):
            with open(csv_file_name,encoding='utf8') as csvfile:
                reader=csv.DictReader(csvfile)
                for row in reader:
                    self.csv_data.append(row)
        else:
            self.save()
    def add(self,description,amount,category):
        if len(self.csv_data)==0:
            id=1
        else:
            id=int(self.csv_data[len(self.csv_data)-1]['id'])+1
        date=time.strftime('%Y-%m-%d')
        self.csv_data.append({'description':description,'amount':amount,'id':str(id),'date':date,'category':category})
        self.save()
        print(f"Expense added successfully (ID: {id})")
        month=self.get_month(date)
        budget=self.budget(month)
        if budget:
            summary=self.summary(month)
            percent=int(summary)/int(budget['amount'])*100
            print(f'You have reached {percent}% of your {month} month budget ({budget['amount']})')
    def list(self,category=''):
        print(f'{'ID':<10} {'Date':<10} {'Description':<20} {'Amount':<5} {'Category':<6}')
        for row in self.csv_data:
            if category=='':
                print(f'{row["id"]:<10} {row["date"]:<10} {row["description"]:<20} {row["amount"]:<5} {row["category"]:<6}')
            else:
                if row['category']==category:
                    print(f'{row["id"]:<10} {row["date"]:<10} {row["description"]:<20} {row["amount"]:<5} {row["category"]:<6}')
            
    def summary(self,month=0):
        total_amount=0
        for row in self.csv_data:
            if month==0:
                total_amount+=float(row['amount'])
            else:
                if int(self.get_month(row['date']))==int(month):
                    total_amount+=float(row['amount'])
        return total_amount
    def delete(self,id):
        for i in range(len(self.csv_data)):
            if self.csv_data[i]['id']==str(id):
                self.csv_data.pop(i)
                break
        self.save()
    def save(self,filename=csv_file_name):
        #print(filename)
        with open(filename,'w',encoding='utf8') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=field_names)
            writer.writeheader()
            for row in self.csv_data:
                writer.writerow(row)
    def get_month(self,date_time):
        actual_month=date_time[5:7]
        return actual_month
    def set_budget(self,month,amount):
        budgets=self.get_budgets()
        budgets.append({'month':month,'amount':amount})
        self.save_budget(budgets)
        print(f'Budget for {month} set to {amount}')
    def get_budgets(self):
        budget=[]
        budget_name='budget.csv'
        if os.path.exists(budget_name):
            with open(budget_name,'r',encoding='utf8') as csvfile:
                reader=csv.DictReader(csvfile)
                for row in reader:
                    budget.append(row)
        return budget
    def save_budget(self,budgets):
        with open('budget.csv','w',encoding='utf8') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=['month','amount'])
            writer.writeheader()
            for budget in budgets:
                writer.writerow({'month':budget['month'],'amount':budget['amount']})
    def budget(self,month):
        for budget in self.get_budgets():
            if int(month)==int(budget['month']):
                return budget
    def update(self,id,description,amount,category):
        find=False
        for data in self.csv_data:
            if data['id']==str(id):
                if description!=None:
                    data['description']=description
                if amount!=None:
                    data['amount']=amount
                if category!=None:
                    data['category']=category
                find=True
                break
        if not find:
            print("Expense not found")
        else:
            self.save()