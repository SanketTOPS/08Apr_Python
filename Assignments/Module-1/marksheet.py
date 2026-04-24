s1=int(input("Enter Subject1 Marks:"))
s2=int(input("Enter Subject2 Marks:"))
s3=int(input("Enter Subject3 Marks:"))
s4=int(input("Enter Subject4 Marks:"))

total=s1+s2+s3+s4
pr=total/4

print("Total:",total)
print("PR:",pr)

if pr>=70:
    print("Result:A+")
elif pr>=60:
    print("Result:A")
elif pr>=50:
    print("Result:B")
elif pr>=40:
    print("Result:C")
else:
    print("Result:FAIL")

