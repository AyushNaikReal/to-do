to_do_list = ['hi','hi'] # This list will store to-do of user
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

