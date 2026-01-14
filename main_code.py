to_do_list = ['hi','hii'] # This list will store to-do of user


while True:
     # code for options
   print( )
   print("""Press : 
   1 for View all To-Dos
   2 for Insert To-Dos
   3 for delete To-Dos """)

   n=int(input('Enter your choice: '))

#1st code for printing list
   if n==1:
    print("To Do's are: ")
    for index, todo in enumerate(to_do_list, start=1):
     print(index,todo)
    ii=input("Press 'y' to proceed: ")
    if ii=='y':
        continue

#2nd code for insertion
   elif n==2:
    entry=input("Enter your to-do (one to at a time): ")
    to_do_list.append(entry)
    print(entry, " - is added in your to-do list")
    print( )
    print("'Do you want to see all entries in to-do list?'")

    nk=input("If yes press 'y' or no press 'n': ")
    if nk=='y':
     for index, item in enumerate(to_do_list, start=1):
      print(index,item)


#code to remove to-do
   elif n==3:
        print(f"Your to-do's: \n")
        for index, todo in enumerate(to_do_list, start=1):
            print(index, todo ,f"\n ")
        v= int(input("Enter the index number yo want to remove: "))
        to_do_list.pop(v-1)

        print(f"Your updated to-do's: \n")
        for index, todo in enumerate(to_do_list, start=1):
            print(index, todo, f"\n ")

        ii=input("Press 'y' to proceed: ")
        if ii=='y':
            continue
