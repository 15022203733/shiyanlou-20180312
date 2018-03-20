#!/usr/bin/env python3

import sys


insurance = 0.165
point = 3500

def Singal_Wage(before_tax,deductions,tax_rate):
  
    try:
        ins_amount = before_tax * insurance
        payable = before_tax - ins_amount - point 
        tax = payable * tax_rate - deductions
        salary = format((before_tax - ins_amount - tax),".2f")
        return salary
    except:
        print("Paramenter Error")

def calc(Id,before_tax):
    salary = before_tax - point 
    before_tax_dict = {}
    if salary <= 0:
        wage_amount = Singal_Wage(before_tax,0,0)
    elif salary <= 1500:
        wage_amount = Singal_Wage(before_tax,0,0.03)
    elif salary <= 4500 and salary > 1500:
        wage_amount = Singal_Wage(before_tax,105,0.1)
    elif salary <= 9000 and salary > 4500:
        wage_amount = Singal_Wage(before_tax,555,0.2)
    elif salary <= 35000 and salary > 9000:
        wage_amount = Singal_Wage(before_tax,1005,0.25)
    elif salary <= 55000 and salary > 35000:
        wage_amount = Singal_Wage(before_tax,2555,0.3)
    elif salary <= 80000 and salary > 55000:
        wage_amount = Singal_Wage(before_tax,5505,0.35)
    elif salary > 80000:
        wage_amount = Singal_Wage(before_tax,13505,0.45)
    print(Id ,end = "")
    print(':',end = "")
    print(wage_amount)

# ????
for arg in sys.argv[1:]:
    deployee_list = arg.split(':')
    calc(int(deployee_list[0]),int(deployee_list[1]))
