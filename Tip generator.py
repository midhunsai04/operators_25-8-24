print("===Tip Calculator===")
spend=float(input("How much do you wan to spend? "))
people=int(input("How many people are in your group? "))
answer=spend/people
answer=round(answer,2)
print("you all owe:",answer)
tip=int(input("What percentage do you want to tip? "))
answer1=tip/100*spend
answer1=round(answer1,2)
print("The tip is:",answer1)