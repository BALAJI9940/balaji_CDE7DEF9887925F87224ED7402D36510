 




def is_leap_year(year):
  """
  This function determines whether a year is a leap year or not.

  Args:
    year: The year to be checked.

  Returns:
    True if the year is a leap year, False otherwise.
  """
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  else:
    return year % 4 == 0


def main():
  """
  This function gets the year from the user and prints whether it is a leap year or not.
  """
  year = int(input("Enter a year: "))
  if is_leap_year(year):
    print(f"{year} is a leap year.")
  else:
    print(f"{year} is not a leap year.")


if __name__ == "__main__":
  main()


    
    

    



  

