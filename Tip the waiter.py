def total_calc(bill_amount,tip_perc):
#define the function to calculate the tip on bill
    total = bill_amount*(1 + 00.1*tip_perc)
    total = round(total,2)
    print(f"Please Pay${total}")

#specify only bill_amount
#default vale of tip percentage is used

total_calc(150,20)