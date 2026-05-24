""" toOpen is used to view the to-do list """

def toOpen():
 with open("Storage","r") as f :
    content = f.read()
    print("\n")
    print("Your to-do are : ")
    for i, list in enumerate(content.split("\n"),1):
        print(f"{i} {list}")




""" toWrite function is use to add new to-do in the file """

def toWrite(content):
 with open("Storage","a") as f :
    f.write("\n"+content)
    print("\n")
    print("The new to-do is added to your to-do list:  "+content)





def toDelete():
    with open("storage","r") as f :
        # converting content in list.
        content = list(f.read().split("\n"))

        # ask choise to delete whole to-do or single one
        print("\n")
        print(" to delete all to-do's press -> 1 \n"
              "to delete a single to-do press -> 2")

        i=int(input("Enter your choice: "))

        if i ==1:
            content.clear()

            with open("storage", "w") as f:
                f.writelines(content)

        elif i==2:
            j=int(input("Enter your choice: "))
            del content[j]

            with open("storage", "w") as f:
                for i in content:
                    f.write(str(i)+"\n")


        print("your to-do list has been deleted")