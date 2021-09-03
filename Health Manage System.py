import datetime
def getdate():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c = int(input("Choose 1 For Excersise And 2 For Food :"))
        if (c==1):
            value = input("Type Here \n")
            with open("Dev-exe.text", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
            print("Successfully Written")
        elif (c==2):
            value = input("Type Here \n")
            with open ("Dev-food.txt", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
            print("Successfully Written")

    elif k==2:
        c = int(input("Choose 1 For Excersise And 2 For Food :"))
        if (c==1):
            value = input("Type Here \n")
            with open("NRa-exe", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
            print("Successfully Written")
        elif (c==2):
            value = input("Type Here \n")
            with open ("NRa-food.text", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
                print("Successfully Written")

    elif k==3:
        c = int(input("Choose 1 For Excersisie And 2 For Food :"))
        if (c==1):
            value = input("Type Here \n")
            with open("Parth-exe.txt", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
            print("Successfully Written")
        elif (c==2):
            value = input("Type Here \n")
            with open("Parth-food.txt", "a") as op:
                op.write(str([str(getdate())]) + " : " + value + "\n")
            print("Successfully Written")
    else:
        ("Pls Add Valid input (1,(Dev),2(NRa),3(Meet)")

def retrieve(k):
    if k==1:
        c = int(input("Choose 1 For Excersise And 2 For Food :"))
        if c==1:
            with open("Dev-exe.txt") as op:
                for i in op:
                    print(i,end=" ")
        elif c==2:
            with open("Dev-food.txt") as op:
                for i in op:
                    print(i,end=" ")

    elif k==2:
        c = int(input("Choose 1 For Excersise And 2 For Food :"))
        if c==1:
            with open("NRa-exe.txt") as op:
                for i in op:
                    print(i,end=" ")
        elif c==2:
            with open("NRa-food.txt") as op:
                for i in op:
                    print(i,end=" ")

    elif k==3:
        c = int(input("Choose 1 For Excersise And 2 For Food :"))
        if (c==1):
            with open("Parth-exe.txt") as op:
                for i in op:
                    print(i,end=" ")
        elif (c==2):
            with open("Parth-food.txt") as op:
                for i in op:
                    print(i,end=" ")

    else:
        ("Pls Add Valid input (Dev, NRa, Parth)")
print("Health Management System: ")
a = int(input("Press 1 For Log And 2 For Retrieve :"))

if a==1:
    b = int(input("Press 1 For Dev, 2 For NRa & 3 For Parth"))
    take(b)
else:
    b = int(input("Press 1 For Dev, 2 For NRa & 3 For Parth"))
    retrieve(b)
