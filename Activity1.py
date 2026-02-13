number = int(input("Enter any number:"))

if number>=50:
  print("Number is greater than 50...")
  if number% 2==0:
    print("Number is even ..")
  else:
    print("Number is odd ...")
else:
    print("Number is less than 50...")
    if number% 2==0:
     print("Number is even ..")
    else:
     print("Number is odd ...")