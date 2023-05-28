import math     #Compulsory task_finance_calculators.py

#Introduction of the program
print("Choose either 'investment' or 'bond' from the menu below to proceed")
print()
print("investment   -     to calculate the amount of interest you'll earn on your investment")
print("bond         -     to calculate the monthly payment on a home loan")
#Request user to select investment or bond
user_selection = input("Please enter your option, 'investment or 'bond' :")

#Method to make user input not case sensitive
investment = 'investment'
bond = 'bond'
if user_selection.lower() == investment.lower():
    #Request user to input deposit amount, interest rate and the term of investment
    deposit_amount = int(input("Please enter the deposit amount :R "))  
    interest_rate = int(input("Please enter the interest rate in percentage: "))
    term_of_investment = int(input("Please enter the number of years you plan on investing: "))
    #Request user to input compound or simple interest
    interest = input("please enter 'simple' or 'compound' interest: |simple|compound|: ")
    #Method to make user input not case sensitive
    simple_interest = 'simple'
    compound_interest = 'compound'
    if interest.lower() == simple_interest.lower() :
        #Method to calculate simple interest
        total_amount = deposit_amount * (1 + (interest_rate / 100) * term_of_investment)
        print(f"the total amount of simple interest earned is : {total_amount}")
        #Method to calculate compound unterest
    elif interest.lower() == compound_interest.lower():
         total_amount = deposit_amount * math.pow((1 + (interest_rate / 100)),term_of_investment)
         print(f"the total amount of compound interest earned is :R{total_amount} ") #output final result
    
    else:
        print("You have selected invalid input try again")
       #Method to make user input not case sensitive
elif user_selection.lower() == bond.lower():
     #Request user to input value of the house,interest rate of the bond and number of months for repayment of bond
     present_house_value = int(input("Please enter the present value of the house :R "))  
     interest_rate_bond = int(input("Please enter the interest rate in percentage. : "))
     i = interest_rate_bond / 100
     number_of_months = int(input("Please enter the number of months to repay the bond: ")) 
     #Method to calculate monthly payment on a home loan     
     monthly_payment = ((i/12) * present_house_value)/(1 - (1+(i/12))**(-number_of_months))
     print(f"the total monthly repayment amount of is : R{monthly_payment}")  #Output Result
else:
    print("You selected an invalid input, try again")# if user made an invalid selection.

