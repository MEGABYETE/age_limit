score = int(input("Enter Your Score:"))
'''70-100 print A
60 - 69 print B 
50 - 59 print C
45 - 48 print D
40 - 44 print E
0 - 39 print F '''
if score >= 70 and score <= 100:
    print("Your Grade is A")
elif score >=60 and score <= 69:
    print("Your Grade is B")
elif score >= 50 and score <= 59:
    print("Your Grade is C")
elif score >= 45 and score<= 49:
    print("Your Grade is D")
elif score >= 40 and score<= 44:
    print("Your Grade is E")
elif score >= 0 and score<= 39:
    print("Your Grade is F")
else:
    print("Not eligible")
