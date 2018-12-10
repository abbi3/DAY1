# Control Structure Example

employee_id = 1001
salary = 15000.00
allowance = 6000.00
tax = 0

gross_salary = salary + allowance

if gross_salary <= 5000 :
    tax = 0
elif gross_salary >= 5001 and gross_salary <= 10000 :
    tax = 10
elif gross_salary >=10001 and gross_salary <= 20000 :
    tax = 20
elif gross_salary>=20000:
    tax = 30

it = gross_salary*tax/100
net_sal=gross_salary-it
print("Employee Id: %d"%employee_id)
print("Basic salary: %f"%salary)
print("Allowance: %f" %allowance)
print("GRoss pay: %f" %gross_salary)
print("Income Tax: %f" %it)
print("Net Pay: %f" %net_sal)