#	Author:Sin_Geek
#	Date:20150414

from datetime import *
import csv

### �����ڸ�ʽ��Ϊ�ɼ����ʽ
def parse_date(raw_date):
	entry_date = raw_date.split("-")
	year = int(entry_date[0])
	month = int(entry_date[1])
	day = int(entry_date[2].split()[0])
	return year, month, day

### �������	
def generate_result(raw_file, seperate_day, begin_date):
	with open("validation.csv", "wb") as validation,open("result1.csv", "wb") as result:
		writer = csv.writer(result)
		writer.writerow(['user_id','item_id'])
		raw_file.readline()
		for line in raw_file.readlines():
			entry = line.strip().split(",")
			entry_date = date(*parse_date(entry[5]))
			date_delta = (entry_date - begin_date).days
			if date_delta >= seperate_day:      
				if (int(entry[2]) < 4 and entry[1] in list):  #�ж��û���Ϊ�ʹ���Ʒ�Ƿ�����Ʒ�Ӽ���
					writer.writerow([entry[0],entry[1]])
					
### ����Ʒ�Ӽ�����list    
def item_in():
    with open("tianchi_mobile_recommend_train_item.csv", 'rt') as handle:
        for ln in handle:
            list.append(ln.strip().split(",")[0])
	
	
SEPERATEDAY = date(2014, 12, 18)	#��֮�������Ϊ���Ե�����
BEGINDAY = date(2014, 11, 18)
list = []
item_in()
with open("tianchi_mobile_recommend_train_user.csv") as raw_file:
    generate_result(raw_file, (SEPERATEDAY - BEGINDAY).days, BEGINDAY)
