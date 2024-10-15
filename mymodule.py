class multiplefunctions():
    def subfields():
        print("Sub-Fields in AI are:")
        AI_subfields=["Machine Learning", "Neural Networks", "Vision",
                  "Robotics", "Speech Processing",
                  "Natural Language Processing"]
        for x in AI_subfields:
            print(x)
        return x 
        
    def oddEven():
        number=int(input("Enter a number: "))
        if (number%2==0):
            print(f"{number} is Even number")
        else:
            print(f"{number} is Odd number")
        return number
        
    def Eligible():
        gender = input("Enter your Gender: ").lower()
        age=int(input("Enter your age: "))
        if gender=='male'and age>=21:
            print("Eligible for marriage")
            cond = "Eligible"
        elif gender=='female' and age>=18:
            print("Eligible for marriage")
            cond = "Eligible"
        else:
            print("Not eligible for marriage")
            cond = "Not Eligible"
        return cond

    def percentage():
        subject_list=[]
        Total=0
        for  x in range(1, 6):
            mark = int(input(f"subject{x}= "))
            subject_list.append(mark)
            Total +=mark

        print(f"Total : {Total}")
        Percentage = Total / 5.0
        print("Percentage : ",format(Percentage, '.14f'))
        return Total
    def triangle():
        height=int(input("Height: "))
        breadth=int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        area_triangle = (height*breadth)/2
        print(f"Area of Triangle: {area_triangle}")
        height1=int(input("Height1: "))
        height2=int(input("Height2: "))
        breadth1=int(input("Breadth: "))
        print("Perimeter formula : Height1+Height2+Breadth")
        perimeter_triangle=height1+height2+breadth1
        print(f"Perimeter of Triangle:{perimeter_triangle}")
        return perimeter_triangle


        