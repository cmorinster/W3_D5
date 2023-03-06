def Income_Calculator():
    print("="*50)
    print("Let's calculate your monthly income.")
    rent = float(input("What is the monthly rent of the property?\n"))
    fees = float(input("What are the total other fees paid by the tenant? (example: parking)\n"))
    return (rent + fees)
def Expense_Calculator(income_value):
    print("="*50)
    print("Now let's calculate your monthly expenses.\n")
    taxes = float(input("What are the taxes that you are paying on the property?\n"))
    insurance = float(input("What is the insurance that you are paying on the property?\n"))
    print("Let's do Utilities!\n")
    electrical = float(input("What much do you pay for electrical on the property each month?\n"))
    gas = float(input("What much do you pay for gas on the property each month?\n"))
    garbage = float(input("What much do you pay for waste removal on the property each month?\n"))
    water = float(input("What much do you pay for water on the property each month?\n"))
    sewage = float(input("What much do you pay for sewage on the property each month?\n"))
    utilities = electrical + gas + garbage + water + sewage + electrical
    print(f"You are paying ${utilities:.2f} per month for utilities.\n")
    hoa = float(input("What do you pay towards the home owners association?\n"))
    lawn = float(input("What much do you pay for snow removal and lawn care on the property each month?\n"))
    vacancy = income_value*0.05
    print(f"You are paying ${vacancy} per month on vacancy costs\n")
    repairs = float(input("How much do you anticipate spending on repairs per month?\n"))
    capex = float(input("How much do you anticipate spending on capex projects per month?\n"))
    property_manager = (input("Will you require a property manager?(y or n)\n")).lower()
    if property_manager == 'y':
        prop_manager_cost = float(income_value*0.1)
        print(f"Your property manager cost is estimated to be {prop_manager_cost:.2f}.\n")
    else:
        prop_manager_cost = 0.00
    mortgage = float(input("How much do you pay for your mortgage per month?\n"))
    return(taxes+insurance+utilities+hoa+lawn+vacancy+repairs+capex+prop_manager_cost+mortgage)
    
    
def Total_Investment():
    print("We will now calculate your investment into the property")
    down_payment =  float(input("What was your down payment made on the property?\n"))
    closing_costs = float(input("What were the closing costs when purchasing the property?\n"))
    repair_money = float(input("How much did you spend on repairs during the initial purchase of the home?\n"))
    misc_costs = float(input("Did you pay and misc. costs when purchasing the property?\n"))
    return(down_payment + closing_costs + repair_money + misc_costs)
      

def ROI_Calculator ():
    while True:
        print("="*50)
        print("Hello, Let's calculate your ROI for your rental property\n")
        income = Income_Calculator()
        expenses = Expense_Calculator(income)
        cashflow = (income - expenses)*12
        if cashflow < 0:
            print("="*50)
            print("You are losing money on your unit, you need to charge more for rent before I will even bother calculating an ROI for you!\n")
            continue
        investment = Total_Investment()
        roi = (cashflow/investment)*100
        return (roi)
    
    
print(f"The ROI for your property is {ROI_Calculator()}%")    
