print("SECONDS IN A YEAR")
year=int(input("Enter the year: "))
if year%4==0:
  print("it is a leap year")
  print("there are",60*60*24*366,"seconds  in this year")
else:
  print("it is not a leap year")
  print("there are",60*60*24*365,"seconds in this year")