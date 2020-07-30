"""Python Coding Examples by Robert Nochez (Last update: 7/29/2020)"""

    """ The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
    We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

    Base Cases:
    >>>sleep_in(False, False)
    True
    >>>sleep_in(True, False)
    False
    >>>sleep_in(False, True)
    True
    """

def sleep_in(weekday, vacation):
  if weekday is False or vacation is True: # Can also be written as not weekday or vacation
    return True
  return False
# Single line answer: return(not weekday or vacation)

################################################################################

    """ We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
    We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

    Base Cases:
    >>>monkey_trouble(True, True)
    True
    >>>monkey_trouble(False, False)
    True
    >>>monkey_trouble(True, False)
    False
    """

def monkey_trouble(a_smile, b_smile):
  if a_smile is b_smile:
    return True
  return False
# Single line answer: return (a_smile == b_smile)

################################################################################

    """Given two int values, return their sum. Unless the two values are the same, then return double their sum.

    Base Cases:
    >>>sum_double(1, 2)
    3
    >>>sum_double(3, 2)
    5
    >>>sum_double(2, 2)
    8
    """
def sum_double(a, b):
  if a == b:
    return (a+b)*2
  return a+b

################################################################################

    """Given an int n, return the absolute difference between n and 21,
    except return double the absolute difference if n is over 21.

    Base Cases:
    >>>diff21(19)
    2
    >>>diff21(10)
    11
    >>>diff21(21)
    0
    """
def diff21(n):
  if n > 21:
    return (abs(21-n))*2
  return abs(21-n)

################################################################################

    """We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
    We are in trouble if the parrot is talking and the hour is before 7 or after 20.
    Return True if we are in trouble.

    Base Cases:
    >>>parrot_trouble(True, 6)
    True
    >>>parrot_trouble(True, 7)
    False
    >>>parrot_trouble(False, 6)
    False
    """

def parrot_trouble(talking, hour):
  if talking and (hour<7 or hour>20):
    return True
  return False
# Single line answer: return (talking and (hour < 7 or hour > 20))

################################################################################

    """Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

    Base Cases:
    >>>makes10(9, 10)
    True
    >>>makes10(9, 9)
    False
    >>>makes10(1, 9)
    True
    """

def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)

################################################################################

    """Given an int n, return True if it is within 10 of 100 or 200.
    Note: abs(num) computes the absolute value of a number.

    Base Cases:
    >>>near_hundred(93)
    True
    >>>near_hundred(90)
    True
    >>>near_hundred(89)
    False
    """

def near_hundred(n):
  return (abs(100-n) <= 10 or abs(200-n) <= 10)

################################################################################

    """Given 2 int values, return True if one is negative and one is positive.
    Except if the parameter "negative" is True, then return True only if both are negative.

    Base Cases:
    >>>pos_neg(1, -1, False)
    True
    >>>pos_neg(-1, 1, False)
    True
    >>>pos_neg(-4, -5, True)
    True
    """

def pos_neg(a, b, negative):
  if negative is True: # is True can be removed as condition cannot be passed if negative is False
    return (a<0 and b<0)
  return ((a<0 and b>0) or (a>0 and b<0))

################################################################################

    """Given a string, return a new string where "not " has been added to the front.
    However, if the string already begins with "not", return the string unchanged.

    Base Cases:
    >>>not_string('candy')
    'not candy'
    >>>not_string('x')
    'not x'
    >>>not_string('not bad')
    'not bad'
    """

def not_string(str):
  if str[:3] == 'not': # len(str) >= 3 can be added to verify operand
    return str
  return 'not ' + str

################################################################################

    """Given a non-empty string and an int n, return a new string where the char at index n has been removed.
    The value of n will be a valid index of a char in the original string
    (i.e. n will be in the range 0..len(str)-1 inclusive).

    Base Cases:
    >>>missing_char('kitten', 1)
    'ktten'
    >>>missing_char('kitten', 0)
    'itten'
    >>>missing_char('kitten', 4)
    'kittn'
    """

def missing_char(str, n):
  str1 = str[:n] # strings are immutable so splicing is the only option to iterate strings
  str2 = str[n+1:]
  return str1 + str2

################################################################################

    """Given a string, return a new string where the first and last chars have been exchanged.

    Base Cases:
    >>>front_back('code')
    'eodc'
    >>>front_back('a')
    'a'
    >>>front_back('ab')
    'ba'
    """

def front_back_v1(str):
    count = len(str)-1
    list = [char for char in str]
    list[0], list[count] = list[count], list[0] #reassigns last and first chars
    return ''.join(list)

def front_back_v2(str):
  if len(str) <= 1:
    return str

  mid = str[1:len(str)-1]  # can be written as str[1:-1]

  # last + mid + first
  return str[len(str)-1] + mid + str[0]

################################################################################

    """Given a string, return a new string in reverse order.

    Base Cases:
    >>>backward_string('code')
    'edoc'
    >>>backward_string('keyboard')
    'draobyek'
    >>>backward_string('berkeley')
    'yelekreb'
    """

def backward_string(str):
    list = [char for char in str]
    list.reverse()
    return ''.join(list)

################################################################################

    """Given a string, we'll say that the front is the first 3 chars of the string.
    If the string length is less than 3, the front is whatever is there.
    Return a new string which is 3 copies of the front.

    Base Cases:
    >>>front3('Java')
    'JavJavJav'
    >>>front3('Chocolate')
    'ChoChoCho'
    >>>front3('abc')
    'abcabcabc'
    """

def front3_v1(str):
  front = str[:3]
  return front + front + front

def front3_v2(str):
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front

################################################################################

    """Given a starting value and a maximum value, print all even numbers from starting value to a maximum value.
    (Uses recursion).

    Base Cases:
    >>>even_nums(2, 10)
    2
    4
    6
    8
    10
    """

def even_nums(StartValue, MaxValue):
    if StartValue > MaxValue:
        return
    if StartValue%2 != 0:
        return even_nums(StartValue + 1, MaxValue)
    print(StartValue)
    return even_nums(StartValue + 2, MaxValue)

################################################################################

    """Given a string and a non-negative int n, return a larger string that is n copies of the original string.

    Base Cases:
    >>>string_times('Hi', 2)
    'HiHi'
    >>>string_times('Hi', 3)
    'HiHiHi'
    >>>string_times('Hi', 1)
    'Hi'
    """

def string_times(str, n):
  return str*n # String data type can be used with +,-,*

def string_times(str, n):
  result = ""
  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
    result = result + str  # could use += here
  return result
################################################################################
