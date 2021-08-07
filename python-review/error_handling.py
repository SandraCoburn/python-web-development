#Error handling with Try, except
def age():
  while True:
    try:
      age = int(input("what's your age?"))
      print(age)
    except ValueError as err:
      print(f'try again, this time a number {err}' )
    except ZeroDivisionError:
      print("No zeroes!!")
    else:
      print("thank you!")
      break
    finally:
      print("I'm finally done")

# age()

#You can add two exceptions together
def sum(a,b):
  try:
    return a+b
  except (ValueError, ZeroDivisionError) as err:
    print(err) 
print(sum(1,'1'))

#or raise an error ex. raise ValueError('Customized error')
# or raise an exception ex. raise Exception('Customized message')