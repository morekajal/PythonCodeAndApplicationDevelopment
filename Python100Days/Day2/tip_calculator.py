print("Welcome to the Tip Calculator")

bill = float(input("What was the Total Bill? $ "))
tip = int(input("What percentage of tip would you like to give? 10, 12, 15 ?"))
split_share = int(input("How many people to split the bills?"))

bill_with_tip = (tip / 100 ) * bill + bill
print(f"Bill with Tip :{bill_with_tip}")

bill_split = bill_with_tip/split_share
print(f"Each person should pay $:{bill_split}")