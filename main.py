from fuxn import *

"Main code"

while True:

 print("\n")
 Input=int(input(" Press 1 to view all to-dos "
          "\n Press 2 to add a new to-do "
          "\n Press 3 to delete a to-do "    
          "\n Enter Your choice: "))


 def main(x):
     match x:
         case 1:
             toOpen()

         case 2:
             new_line = input("Enter new line to write: ")
             toWrite(new_line)


         case 3:
             toDelete()


         case _:
             print("\n Enter a valid choice")
 main(Input)

