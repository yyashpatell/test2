class LargestValue():
    num1 = float(input("please enter first number:"))
    num2 = float(input("please enter second number:"))
    num3 = float(input("please neter third number:"))

    if num1 > num2:
      if num1 > num3:
        LNo=num1
      else:
        LNo=num3
    else:
        if num2 > num3:
            LNo=num2
        else:
            LNo=num2
        
        print("number 1:",num1)
        print("number 2",num2)
        print("number 3:",num3)
        print("largest number is:",LNo)
    
        
        
