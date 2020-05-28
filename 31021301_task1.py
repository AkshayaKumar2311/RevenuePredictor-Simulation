# Student id: 31021301
# Student Name : Akshaya Kumar Chandrasekaran
# TASK 1, FIT9136 Python Assignment
# Started working on TASK 1 : 20-Apr-2020
# Last modifies : 01-MAY-2020
# Compute the revenue and total stock remaining for one year from the given year,revenue and stock


#read_data is a function that reads a file and stores the
#value from the file in a dictionary format and returs the same

#AU_INV_START.txt is the file name , file is closed upon exit

def read_data():
#Reads the file
    my_file = open("AU_INV_START.txt","r")
    input_year = int(my_file.readline())            #reads the first line
    input_stock = int(my_file.readline())           #reads the second line
    input_revenue = float(my_file.readline())       #reads the third line
#writes the content of the file in dictionary format
    start_input = {"start_year":input_year,"start_stock":input_stock,"start_revenue":input_revenue}
    my_file.close()
#retuns the dictionary object
    return start_input

# perform calculation function takes in 7 aruguments to calculate the revenue
# based on the given condition in question and criteria and returns the list of
# required value to the calling function.

def perform_calculation(months,quantity,defective_items,revenue,rrp,total_stock,year):

#months is a dictionary that contains month num as key and its corresponding days as value
#quantity is the number of quantity that is being sold per day
#defective_items is the total number of defective times
#revenue is revenue of the company
#rrp is the price of the product
#total_stock is the total number of stock that is remaining during the function call
#year is the year in which the revenue is asked. To find if the year is a leap year or not.

    for key, value in months.items():
        temp_inc = 0
        sold_stock = 1
#checks if the month is in 1,3, 5, 7, 8, 10, 12 to iterate it 31 times
        if (key in (1, 3, 5, 7, 8, 10, 12)):
            for i in range(months[key]):

#During the start of the month, if the defective items are
#more than the quantity required per day, sell those products at
#80 % of the original cost.

                while ((i == temp_inc) and (defective_items >= quantity)):
                    if (key in (11, 12, 1, 2)):
                        revenue = revenue + (((rrp + rrp * 0.20) * 0.8) * int(quantity + quantity * 0.35))
                        defective_items = defective_items - int(quantity + quantity * 0.35)
                        temp_inc = temp_inc + 1
                    elif (key in (3, 4, 5, 6, 7, 8, 9, 10)):
                        revenue = revenue + (rrp * 0.8 * int(quantity))
                        defective_items = defective_items - int(quantity)
                        temp_inc = temp_inc + 1

#Check for each month to compute the revenue and the rrp
#and total stock remaining.
                else:
                    if (key == 1 or key == 12):
# Calculates revenue
                        revenue = revenue + ((rrp + rrp * 0.20) * int(quantity + quantity * 0.35))
# Calculates the remaining stock
                        total_stock = total_stock - int(quantity + quantity * 0.35)
# Calculates the sold stock per day to calculate the number of defective items
                        sold_stock = sold_stock + int(quantity + quantity * 0.35)
# Final defective items by the end of the month is returned
                        defective_items = int(sold_stock * 0.05)
# refill of stock by 600 is done if the total stock is less than 400
                        if (total_stock < 400):
                            total_stock = total_stock + 600
# Same calculation as above for every month is done...!
                    elif (key in (3, 5, 8, 10)):
                        revenue = revenue + (rrp * int(quantity))
                        total_stock = total_stock - int(quantity)
                        sold_stock = sold_stock + int(quantity + quantity * 0.35)
                        defective_items = int(sold_stock * 0.05)
                        if (total_stock < 400):
                            total_stock = total_stock + 600
                    elif (key == 7):
# during the month of july, on first day, increase the
# rrp by 5% and quantity by 10% every year
                        if (i == 0):
                            rrp = rrp + (rrp * 0.05)
                            quantity = int(quantity + (quantity * 0.1))
                            #company_found_year = company_found_year + 1
                        revenue = revenue + (rrp * int(quantity))
                        total_stock = total_stock - int(quantity)
                        sold_stock = sold_stock + int(quantity + quantity * 0.35)
                        defective_items = int(sold_stock * 0.05)
                        if (total_stock < 400):
                            total_stock = total_stock + 600
#Check If the month is 4, 6, 9, 11 and iterate it to
# 30 times since these month has 30 days.
        elif (key in (4, 6, 9, 11)):
            temp_inc = 0
            for i in range(months[key]):
#During the start of the month, check for defective items is checked.
                while (i == temp_inc and defective_items >= quantity):
                    if (key in (11, 12, 1, 2)):
                        revenue = revenue + (((rrp + rrp * 0.20) * 0.8) * int(quantity + quantity * 0.35))
                        defective_items = defective_items - int(quantity + quantity * 0.35)
                        temp_inc = temp_inc + 1
                    elif (key in (3, 4, 5, 6, 7, 8, 9, 10)):
                        revenue = revenue + (rrp * 0.8 * int(quantity))
                        defective_items = defective_items - int(quantity)
                        temp_inc = temp_inc + 1
                else:
                    if (key in (4, 6, 9)):
                        revenue = revenue + (rrp * int(quantity))
                        total_stock = total_stock - int(quantity)
                        sold_stock = sold_stock + int(quantity + quantity * 0.35)
                        defective_items = int(sold_stock * 0.05)
                        if (total_stock < 400):
                            total_stock = total_stock + 600
                    else:
                        revenue = revenue + ((rrp + rrp * 0.20) * int(quantity + quantity * 0.35))
                        total_stock = total_stock - int(quantity + quantity * 0.35)
                        sold_stock = sold_stock + int(quantity + quantity * 0.35)
                        defective_items = int(sold_stock * 0.05)
                        if (total_stock < 400):
                            total_stock = total_stock + 600
# If the month is 2. check if the year is a leap year or not.
# if leap year, iterate by 29 days else 28 days
        else:
            if (year % 4 == 0 or year % 400 == 0):
                temp_inc = 0
                for i in range(months[key] + 1):
                    while (i == temp_inc and defective_items > quantity):
                        if (key in (11, 12, 1, 2)):
                            revenue = revenue + (((rrp + rrp * 0.20) * 0.8) * int(quantity + quantity * 0.35))
                            defective_items = defective_items - int(quantity + quantity * 0.35)
                            temp_inc = temp_inc + 1
                        elif (key in (3, 4, 5, 6, 7, 8, 9, 10)):
                            revenue = revenue + (rrp * 0.8 * int(quantity))
                            defective_items = defective_items - int(quantity)
                            temp_inc = temp_inc + 1
                    else:
                        revenue = revenue + ((rrp + rrp * 0.20) * int(quantity + quantity * 0.35))
                        total_stock = total_stock - int((quantity + quantity * 0.35))
                        sold_stock = sold_stock + int(quantity + quantity * 0.35)
                        defective_items = int(sold_stock * 0.05)
                        if (total_stock < 400):
                            total_stock = total_stock + 600
            else:
                temp_inc = 0
                for i in range(months[key]):
                    while (i == temp_inc and defective_items >= sold_stock):
                        if (key in (11, 12, 1, 2)):
                            revenue = revenue + (((rrp + rrp * 0.20) * 0.8) * int(quantity + quantity * 0.35))
                            defective_items = defective_items - int(quantity + quantity * 0.35)
                            temp_inc = temp_inc + 1
                        elif (key in (3, 4, 5, 6, 7, 8, 9, 10)):
                            revenue = revenue + (rrp * 0.8 * int(quantity))
                            defective_items = defective_items - int(quantity)
                            temp_inc = temp_inc + 1
                    else:
                        revenue = revenue + ((rrp + rrp * 0.20) * int(quantity + quantity * 0.35))
                        total_stock = total_stock - int((quantity + quantity * 0.35))
                        sold_stock = sold_stock + int(quantity + quantity * 0.35)
                        defective_items = int(sold_stock * 0.05)
                        if (total_stock < 400):
                            total_stock = total_stock + 600
#Returns the months, quantity, no of defective times, rrp at the end of the year, and the
#total stock that is left.
    return (months, quantity, defective_items, revenue, rrp, total_stock)

#cal_stock_revenue function takes in a dictionary variable
#read from the text file.


def cal_stock_revenue(start_year_calc):
    current_year = start_year_calc['start_year']
# Even if more digits given, only first 4 digits is taken
    current_year = str(current_year)
    current_year = int(current_year[:4])
    total_stock_given = start_year_calc['start_stock']
    revenue_given = start_year_calc['start_revenue']
    peak_rrp = 705
    rrp = float(((peak_rrp/120)*100))
    peak_quantity = 36
    quantity = round(((peak_quantity/135)*100))
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    company_found_year = 2000
    revenue = 0
    total_stock = 1000
    defective_items = 0
    year_count = 0
    # for temp in range(company_found_year, current_year):
    #         year_count = year_count + 1
    #         rrp = rrp + (rrp * 0.05)
    #         quantity = int(quantity + (quantity * 0.1))
    for inc in range(company_found_year,current_year+1):
        year_count = year_count + 1
# Condition to check it the year count is not divisible by 9(for financial crisis)
# and if the year count is less than 9
        if(year_count % 9 !=0 and year_count<9):
# perform_calculation(months, quantity, defective_items, revenue, rrp, total_stock, company_found_year)
# calling the function perform_calculation to calculate the revenue
            updated_value = perform_calculation(months,quantity,defective_items,revenue,rrp,total_stock,inc)
            quantity = updated_value[1]
            defective_items = updated_value[2]
            revenue = updated_value[3]
            rrp = updated_value[4]
            total_stock = updated_value[5]
# checks for the condition if the year count is divisible by 9
# to change the value of rrp and quantity sold per day for that year alone
        elif (year_count % 9 == 0):
            quantity_year_9 = int(quantity - quantity * 0.2)
            rrp_year_9 = rrp + (rrp * .10)
            updated_value = perform_calculation(months, quantity_year_9, defective_items, revenue,
                                               rrp_year_9, total_stock, inc)
            quantity = int(quantity + (quantity * 0.1))
            defective_items = updated_value[2]
            revenue = updated_value[3]
            rrp = rrp + (rrp * 0.05)
            total_stock = updated_value[5]
# checks for the condition if the year count is divisible by 10
# to change the value of rrp and quantity sold per day for that year alone
        elif (year_count % 10 == 0):
            quantity_year_10 = int(quantity - quantity * 0.1)
            rrp_year_10 = rrp + (rrp * .05)
            updated_value = perform_calculation(months, quantity_year_10, defective_items, revenue,
                                                rrp_year_10,total_stock, inc)
            quantity = int(quantity + (quantity * 0.1))
            defective_items = updated_value[2]
            revenue = updated_value[3]
            rrp = rrp + (rrp * 0.05)
            total_stock = updated_value[5]
# checks for the condition if the year count is divisible by 11
# to change the value of rrp and quantity sold per day for that year alone
# resetting the year count to 1 to again start the iterations.
        elif ( year_count % 11 == 0):
            quantity_year_11 = int(quantity - quantity * 0.05)
            rrp_year_11 = rrp + (rrp * .03)
            updated_value = perform_calculation(months, quantity_year_11, defective_items, revenue,
                                                rrp_year_11,total_stock, inc)
            quantity = int(quantity + (quantity * 0.1))
            defective_items = updated_value[2]
            revenue = updated_value[3]
            rrp = rrp + (rrp * 0.05)
            total_stock = updated_value[5]
            year_count = 1
# storing the year asked, stock avaiable and the revenue as a dictionary
# and returning the same.
    end_output = {"end_year": current_year + 1, "end_stock": total_stock,
                  "end_revenue": float("{:.2f}".format(revenue))}
# to check if the rrp price is getting updated properly.
    # print("latest RRP : " + str(rrp))
    return end_output

# write data is a function that creates a new text file
# writes in the year, total stock remaining and revenue for that year.


def write_data(calc_output):
    out_file = open("AU_INV_END.txt","w")
    out_file.write(str(calc_output['end_year']) + "\n")
    out_file.write(str((calc_output['end_stock'])) + "\n")
    out_file.write(str(calc_output['end_revenue']) + "\n")
    out_file.close()


#Function call
start_year_calc = read_data()
calc_output = cal_stock_revenue(start_year_calc)
write_data(calc_output)
