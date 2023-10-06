from a2 import *

print(get_length('ATCGAT'))


def convert_to_celsius(fahrenheit):

 ''' (number) -> number

 Return the number of Celsius degrees equivalent to fahrenheit degrees.

convert_to_ccelsius(32)
0
convert_to_celsius(212)
 100 '''
 return (fahrenheit - 32) * 5 / 9

 def colder_temperature(temp1, temp2):
  '''(number, number) -> number
  Return the colder of the two temperatures, temp1 (degrees Celsius)
  and temp2 (degrees Fahrenheit), in degrees Celsius.
  '''
# print(convert_to_celsius(35))
# help(convert_to_celsius)
#
# print('''yesterday
# today
# \ntomorrow''')
#
# def country(name) -> str:
#  print(name)
#  return name
#
# h = country('hello')
# print(h)
#
#
# def count_letters():
#  """ (str) -> int
#
#  Return the number of letters in word.
# count_letters('hello')
#  5
# count_letters('bonjour')
#  7
#  """
#  def count_vowels():
#   return 5
#
#  def consonents():
#   return 4
#  return count_vowels(), consonents()
# # Write the one-line function body that belongs here.
# count_letters()