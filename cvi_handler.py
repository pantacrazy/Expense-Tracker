import csv,time
csv_file_name='csv_basic'
field_names=['id','description','amount','date']
class data_processing:
    def __init__(self):
        self.csv_data=[]
        with open(csv_file_name,encoding='utf8') as csvfile:
            reader=csv.DictReader(csvfile,fieldnames=field_names)
            for row in reader:
                self.csv_data.append(row)
    def add(self,description,amount):
        if len(self.csv_data)==0:
            id=1
        else:
            id=int(self.csv_data[len(self.csv_data)-1]['id'])+1
        date=time.strptime('%Y-%m-%d')
        self.csv_data.append({'description':description,'amount':amount,'id':str(id),'dates':date})
        self.save()
    def list(self):
        print(f'{'ID':<10} {'Date':<10} {'Description':<20} {'Amount':<5}')
        for row in self.csv_data:
            print(f'{row["id"]:<10} {row["dates"]:<10} {row["description"]:<20} {row["amount"]:<5}')
    def summary(self,month=0):
        total_amount=0
        for row in self.csv_data:
            if month==0:
                total_amount+=float(row['amount'])
            else:
                if self.get_month(row['dates'])==month:
                    total_amount+=float(row['amount'])
        return total_amount
    def delete(self,id):
        for i in range(len(self.csv_data)):
            if self.csv_data[i]['id']==str(id):
                self.csv_data.pop(i)
                break
        self.save()
    def save(self):
        with open(csv_file_name,'w',encoding='utf8') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=field_names)
            writer.writeheader()
            for row in self.csv_data:
                writer.writerow(row)
    def get_month(self,date_time):
        actual_date=time.strptime(date_time,'%Y-%m-%d')
        return time.strftime('%m',actual_date)