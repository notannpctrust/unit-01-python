
room_number = (input("What is the room number?" ))

#Using an if statement for t
if "B" in room_number or "C" in room_number:
  print("That is an upper room,moving on.B204")
  
else:
  print("That is not an upper room")

  

number_of_students = int(input("How many students are present?" ))

if number_of_students <= 30:
    teacher = input("Ok,now is there a teacher present? ")
    if teacher == "yes":
     print("Excellent.Moving on")
    else:
     print("CODE RED! CODE RED! TRY AGAIN.")
else:
 print("NOT ENOUGH STUDENTS!")

 

exit_door = input("Is the nearest exit door clear?"  )

if exit_door == "yes":
   print("Okay,check.")
else:
 print("Error:Clear it immediately!!!!!!")
 




