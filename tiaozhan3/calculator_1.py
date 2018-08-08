#!/usr/bin/env python3

import sys
import csv

#dingzhi canshu shunxu 
class Args(object):
	def __init__(self):
		self.args = sys.argv[1:]

		index_c = self.args.index('-c')
		self.c = self.args[index_c + 1]
		index_d = self.args.index('-d')
		self.d = self.args[index_d + 1]
		index_o = self.args.index('-o')
		self.o = self.args[index_o + 1]
filepath = Args()

#duqu peizhiwenjian
class Config(object):

	def __init__(self):
		self.config = self._read_config()

	def _read_config(self):
		config = {'s_total':0}
		with open(filepath.c) as file:
			for config_row in file.readlines():
				config_row_split = config_row.split('=')
				config_type = config_row_split[0].strip()
				config_num = config_row_split[1].strip()
				
				if config_type == 'JiShuL' or config_type == 'JiShuH':
					config[config_type] = float(config_num)
				else:
					config['s_total'] += float(config_num)
		return config
config = Config().config

#duqu yonghuxinxi
class UserData(object):
	
	def __init__(self):
		self.userdata = self._read_users_data()

	def _read_users_data(self):
		
		with open(filepath.d) as file:
			data_row = list(csv.reader(file))	
			return data_row

		
#gongzi jisuanlei
class IncomeTaxCalculator(object):
	
	

	def calc1(self,Id,before):
		before_tax = int(before)
		salary = before_tax - 3500 
		insurance = config.get('s_total')
		if before_tax < config.get('JiShuL'):
                	shebao = config['JiShuL'] * insurance
		elif before_tax > config.get('JiShuH'):
			shebao = config['JiShuH'] * insurance
		else:
			shebao = before_tax * insurance

		payable = before_tax - shebao - 3500 	

		if salary <= 0:
			tax = payable * 0 - 0
		elif salary <= 1500:
			tax = payable * 0.03 - 0
		elif salary <= 4500 and salary > 1500:
			tax = payable * 0.1 - 105
			
		elif salary <= 9000 and salary > 4500:
			tax = payable * 0.2 - 555			
	
		elif salary <= 35000 and salary > 9000:
			tax = payable * 0.25 - 1005
		
		elif salary <= 55000 and salary > 35000:
			tax = payable * 0.3 - 2555
			
		elif salary <= 80000 and salary > 55000:
			tax = payable * 0.35 - 5505
	
		elif salary > 80000:
			tax = payable * 0.45 - 13305

		salary = format((before_tax - shebao - tax),".2f")
		return [Id,before_tax,shebao,tax,salary]
#jisuan jieshu xieru wenjian
	def export(self):
		data = UserData().userdata

		with open(filepath.o,'w') as file:
			
			for i,w in data:
				
				biao = self.calc1(i,w)
				writer = csv.writer(file).writerow(biao)


if __name__ == '__main__':

	
	calc = IncomeTaxCalculator();
	calc.export()
