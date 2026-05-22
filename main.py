""" toOpen is used to view the to-do list """

def toOpen():
 with open("Storage","r") as f :
    content = f.read()
    print("\n")
    print("Your to-do are : \n" +content)

""" toWrite function is use to add new to-do in the file """

def toWrite(content):
 with open("Storage","a") as f :
    f.write("\n"+content)
    print("\n")
    print("The new to-do is added to your to-do list:  "+content)



"Main code"
while True:
 print("\n")
 chh=int(input(" Press 1 to view all to-dos "
          "\n Press 2 to add a new to-do "
          "\n Enter Your choice: "))

 def main(x):
    match x:
        case 1:
            toOpen()

        case 2:
            new_line = input("Enter new line to write: ")
            toWrite(new_line)
            

        case _:
            print("\n Enter a valid choice")

 main(chh)

