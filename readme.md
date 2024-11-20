This is a repository that contains all the resources that I have used to learn Python.
Down below, you will find a table of contents that will help you navigate through the resources.

<h1>TABLE OF CONTENTS</h1>

- Lessons 
   - [1. Introduction and Variables](MD/1.Intro_and_vars.md)
   - [2. Integers and Operators](MD/2.Integers_and_operators.md)
   - [3. Bool and If/Else](MD/3.bool_and_if_else.md)
   - [4. String methods](MD/4.String-methods.md)
   - [5. Functions](MD/5.Functions.md)
   - [6. Exceptions and error handling](MD/6.Exceptions_and_error_handling.md)
   - [7. Sequence-1](MD/7.Sequence_1.md)
   - [8. Sequence-2](MD/8.Sequence_2.md)
   - [9. Loops](MD/9.Loops.md)
- [Exercises](#exercises)
- [✅ Semantic versioning:](#-semantic-versioning)
- [✅ Install pipenv](#-install-pipenv)
- [✅ To create requirements.txt file](#-to-create-requirementstxt-file)
- [✅ Modules](#-modules)
  - [random](#random)
  - [math](#math)
  - [time / datetime / timedelta](#time--datetime--timedelta)
  - [json](#json)
  - [logging](#logging)
  - [requests](#requests)
  - [faker](#faker)
  - [translators](#translators)
  - [re](#re)
  - [collections](#collections)


# Exercises
🎯 Here are some resources to help you get started with Python and exercise 💪👇️
1. Practice Python (https://www.practicepython.org/)
2. HackerRank (https://www.hackerrank.com/domains/python)
3. Project Euler (https://projecteuler.net/archives)
4. Codewars (https://www.codewars.com/kata/search/python)


# ✅ Semantic versioning: 
https://semver.org/

> - ex: 3.11.0
> - 1. "3"  - Major version
> - 2. "11" - Minor version
> - 3. "0"  - Patch version
## ✅ Install pipenv

To install `pipenv`, run the following commands:

```bash
pip install pipenv
pipenv --version  
```

If it did not work, try the following steps:

1. Uninstall `virtualenv` and `pipenv`:
   ```bash
   python -m pip uninstall virtualenv pipenv -y
   py -m pip uninstall virtualenv pipenv -y
   python3 -m pip uninstall virtualenv pipenv -y
   ```
2. Upgrade `setuptools` and `wheel`:
   ```bash
   python -m pip install --upgrade setuptools wheel
   ```
3. Reinstall `pipenv`:
   ```bash
   python -m pip install --user pipenv
   ```

If you encounter the error:
```
'pipenv' is not recognized as an internal or external command, operable program or batch file
```

Follow these steps to resolve it:

1. Get the path to the base directory for the user site-packages by running:
   ```bash
   python -m site --user-site
   ```
   Example output: `C:\Users\YourUsername\AppData\Roaming\Python\Python37\site-packages`
2. Replace `site-packages` in the path with `Scripts` and add it to your system PATH:
   - On Windows: Edit environment variables for your account > in the User variables select `Path` > Edit > New > `C:\Users\YourUsername\AppData\Roaming\Python\Python37\Scripts`

## ✅ To create requirements.txt file

1. The outdated command:
   ```bash
   pipenv lock -r > requirements.txt
   ```
2. The new version:
   ```bash
   pipenv run pip freeze > requirements.txt
   ```

___

# ✅ Modules

- [**Codete**](https://codete.com/blog/10-built-in-modules-in-python-you-should-know#overview) - 10 Built-in Modules in Python You Should Know
- [**Levelup**](https://levelup.gitconnected.com/11-most-useful-built-in-python-modules-you-might-not-know-yet-eff3e0e6f586) - 11 Most Useful Built-in Python Modules You Might Not Know Yet

## random

- [Documentation](https://docs.python.org/3/library/random.html)

1. `random.random()`: 
   - Return the next random floating point number in the range [0.0, 1.0).
   ```python
   import random
   print(random.random())
   ```

2. `random.randint(a, b)`: 
   - Return a random integer N such that a <= N <= b.
   ```python
   import random
   print(random.randint(0, 10))
   ```

3. `random.choice(seq)`: 
   - Return a random element from the non-empty sequence `seq`. If `seq` is empty, raises `IndexError`.
   ```python
   import random
   x = [i for i in range(10)]
   print(random.choice(x))
   ```

4. `random.shuffle(x[, random])`: 
   - Shuffle the sequence `x` in place.
   ```python
   import random
   x = [[i] for i in range(10)]
   random.shuffle(x)
   print(x)
   ```

## math

- [Documentation](https://docs.python.org/3/library/math.html)

1. `math.ceil(x)`: 
   - Return the ceiling of `x` as a float, the smallest integer value greater than or equal to `x`.
   ```python
   import math
   print(math.ceil(4.2))
   ```

2. `math.floor(x)`: 
   - Return the floor of `x` as a float, the largest integer value less than or equal to `x`.
   ```python
   import math
   print(math.floor(4.8))
   ```

3. `math.trunc(x)`: 
   - Return the Real value `x` truncated to an Integral (usually an integer).
   ```python
   import math
   print(math.trunc(4.8))
   ```

4. `math.factorial(x)`: 
   - Return `x` factorial as an integer. Raises `ValueError` if `x` is not integral or is negative.
   ```python
   import math
   print(math.factorial(5))
   ```

5. `math.gcd(a, b)`: 
   - Return the greatest common divisor of the specified integer arguments.
   ```python
   import math
   print(math.gcd(10, 20))
   ```

6. `math.pow(x, y)`: 
   - Return `x` raised to the power `y`.
   ```python
   import math
   print(math.pow(2, 3))
   ```

7. `math.sqrt(x)`: 
   - Return the square root of `x`.
   ```python
   import math
   print(math.sqrt(16))
   ```

8. `math.pi`: 
   - The mathematical constant π = 3.141592…, to available precision.
   ```python
   import math
   print(math.pi)
   ```

## time / datetime / timedelta

1. `time.time()`: 
   - Return the time in seconds since the epoch as a floating point number.
   ```python
   import time
   print(time.time())


   print("tm_wday  =>", time_z.tm_wday)
   print("tm_min  =>", time_z.tm_min)
   print("tm_isdst  =>", time_z.tm_isdst)
   print("tm_mday  =>", time_z.tm_mday)
   print("tm_year  =>", time_z.tm_year)
   print("tm_zone  =>", time_z.tm_zone)
   ```

2. `time.sleep(secs)`: 
   - Suspend execution of the calling thread for the given number of seconds.
   ```python
   import time
   time.sleep(1)
   ```

3. `time.localtime([secs])`: 
   - Convert a time expressed in seconds since the epoch to a `struct_time` in local time.
   ```python
   import time
   print(time.localtime())
   ```

4. `time.strftime(format[, t])`: 
   - Convert a tuple or `struct_time` representing a time to a string as specified by the format argument.
   ```python
   import time
   print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

   # 1. %y  => is year in short version  =>  Годы в краткой версии
   # 2. %Y  => is year in full version  =>  Годы в полной версии
   # 3. %m  => is month in number =>  Месяцы в числовом формате
   # 4. %M  => is minute in number =>  Минуты в числовом формате
   # 5. %d  => is day in number =>  Дни в числовом формате
   # 6. %D  => is Date (full date) =>  Дата (полная дата)
   # 7. %h  => is month in short version =>  Месяцы в краткой версии
   # 8. %H  => is hour in number =>  Часы в числовом формате
   # 9. %s  => DOES NOT EXIST =>  НЕ СУЩЕСТВУЕТ
   # 10. %S => is second in number =>  Секунды в числовом формате
   ```

5. `datetime.datetime.now()`: 
   - Return the current local date and time.
   ```python
   import datetime
   print(datetime.datetime.now())
   ```

6. `datetime.datetime(year, month, day, ...)`: 
   - The year, month, and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass.
   ```python
   import datetime
   print(datetime.datetime(2020, 5, 17, 12, 30, 0, 0))
   ```

7. `timedelta`: 
- EN: The timedelta class is used to represent the difference between two dates or times.
```python
import datetime
print(datetime.timedelta(days=365, hours=5, minutes=1))
```
- timedelta can add days, seconds and microseconds to a datetime object
```python
import datetime
now = datetime.now()
print(now)
>>> datetime.datetime(2023, 7, 31, 12, 30, 10, 999999)

print(now + datetime.timedelta(days=365))
>>> datetime.datetime(*2024*, 7, 30, 12, 30, 10, 999999)
```

## json

- [Documentation](https://docs.python.org/3/library/json.html)

1. `json.dumps(obj)`: 
   - Serialize `obj` to a JSON formatted `str`.
   ```python
   import json
   print(json.dumps({}))
   ```

2. `json.loads(s)`: 
   - Deserialize `s` (a `str`, `bytes` or `bytearray` instance containing a JSON document) to a Python object.
   ```python
   import json
   print(json.loads("{}"))
   ```

## logging

- [Documentation](https://docs.python.org/3/library/logging.html)

Logging is a means of tracking events that happen when some software runs. It has an ordered list of levels that indicate the severity of events:

1. `DEBUG`: Detailed information, typically of interest only when diagnosing problems.
2. `INFO`: Confirmation that things are working as expected.
3. `WARNING`: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’).
4. `ERROR`: Due to a more serious problem, the software has not been able to perform some function.
5. `CRITICAL`: A serious error, indicating that the program itself may be unable to continue running.

To configure the logging module, you must use the `basicConfig()` function:

```python
import logging

logging.basicConfig(
   level=logging.DEBUG,
   filename='app.log',
   filemode='a+',
   format='%(levelname)s - %(message)s - %(asctime)s'
)

logging.debug('This is a debug message')
```

## requests

- [Documentation](https://docs.python-requests.org/en/master/)

This library is similar to `axios` in JavaScript.

```python
import requests

# HTTP METHODs
# axios.get()       # get data from server      =>  Получить данные с сервера
# axios.post()      # send data to server       =>  Отправить данные на сервер
# axios.put()       # update data on server     =>  Обновить данные на сервере
# axios.delete()    # delete data from server   =>  Удалить данные с сервера
# axios.patch()     # partially update data on server  =>  Частично обновить данные на сервере

URL = "https://reqres.in/api/users?page=2"
response = requests.get(URL)

print("Status:", response)
users = response.json().get("data", "No data found")

for user in users:
   str = f"""
   Name: {user["first_name"]} {user["last_name"]}
   Email: {user["email"]}
   ------------------------------------------------
   """
   print(str)


# {}[key]       # raise error if key not found
# {}.get(key)   # return None if key not found

# ===================================================================
# In js we would do:
# axios.get('https://...')

# In python we do:
# response = requests.get('https://...')

# # To get the status code:
# print(response.status_code)

# # To get the content:
# print(response.content)

# # To get the json:
# print(response.json())
```

## faker

- [Documentation](https://faker.readthedocs.io/en/master/)

This library generates fake data.

```python
from faker import Faker

fake = Faker()
print(fake.name())
print(fake.address())
print(fake.text())
print(fake.email())
print(fake.phone_number())
print(fake.country())
print(fake.url())
```

## translators

- [Documentation](https://pypi.org/project/translators/)

```python
import translators as ts

original_text = "Hello, what a beautiful weather it is today!"

arabic_translation = ts.translate_text(original_text, to_language='ar')
print("ARABIC translation:", arabic_translation)

uzbek_translation = ts.translate_text(original_text, to_language='uz')
print("UZBEK translation:", uzbek_translation)

russian_translation = ts.translate_text(original_text, to_language='ru')
print("RUSSIAN translation:", russian_translation)

japanese_translation = ts.translate_text(original_text, to_language='ja')
print("JAPANESE translation:", japanese_translation)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# OUTPUT:
# ARABIC translation:  مرحبا ، يا له من طقس جميل اليوم!
# UZBEK translation:  Assalomu alaykum bugungi kun qanday go'zal ob-havo!
# RUSSIAN translation:  Здравствуйте, какая сегодня прекрасная погода!
# JAPANESE translation:  こんにちは、今日はなんと美しい天気でしょう!
```

## re

- [Documentation](https://docs.python.org/3/library/re.html)

```python
# Source: https://regexr.com/
import re

# string = "The rain in Spain"
# pattern = "ai"
# r_pattern = r'[A-Z]'
# --------------------------------------
# re.findall(pattern, string)  # => It returns a list of all matching patterns.

# result = re.findall(pattern, string)
# print(result)
# --------------------------------------
# re.search(pattern, string)   # => It returns first match's position
# result = re.search(r_pattern, string)
# print(result)
# --------------------------------------
# re.split(pattern, string)
# => Works like split() method of strings but can take RE as separator.
# r_pattern = r'[A-Z]'
# string = "The rain in Spain"
# result = re.split(r_pattern, string)
# print(result)
# --------------------------------------
# re.sub(pattern, repl, string, count=0, flags=re...)
# # => It returns a new string with all matches of the pattern replaced by repl.
# ________________
# r_pattern = r'[A-Z]'
# string = "The rain in Spain"
# result = re.sub(r_pattern, '*', string)
# print(result)
# ________________
# 1. pattern =>  The regular expression pattern string.
# 2. repl    =>  The replacement string.
# 3. string  =>  The source string.
# 4. count   =>  Maximum number of occurrences that will be replaced.
#                If not specified or is 0, all occurrences will be replaced.
# 5. flags   =>  A combination of re flags.
# --------------------------------------
# re.compile(pattern, flags=0)
# => It returns a regular expression object.
# r_pattern = r'[A-Z]'
# string = "The rain in Spain"
# pattern = re.compile(r_pattern)
# result = pattern.findall(string)
# print(result)

# f''
# ''.format()
# ======= Username pattern =======
# re.compile(r'@([A-Za-z0-9_]+)')
# @  ->   indicates the start of the username
# () ->   indicates the start and end of the username
# [] ->   indicates the range of characters that can be used in the username
# +  ->   indicates that the username must contain at least one character
# A-Za-z0-9_ -> indicates the range of characters that can be used in the username
# Ex: @username
# Ex: @user_name
# To test if it works, use the following code:
# username = '@user_name'
# print(re.search(r'@([A-Za-z0-9_]+)', username) != None)
# ============================================================
# ^ (Caret)    =>  It matches the start of the string.
# string = "Hello World!"
# x = re.findall("^Hello", string)
# print(x)
# ============================================================
# # $ (Dollar)   =>  It matches the end of the string.
# string = "Hello World!"
# x = re.findall("World!$", string)
# print(x)
# # ============================================================
# . (Dot)   =>  It matches any character except a newline.
# string = "Hello World!"
# x = re.findall("H.ll.", string)
# print(x)
```

## collections

- [Documentation](https://docs.python.org/3/library/collections.html)

1. `collections.deque`
   ```python
   from collections import deque

   queue = deque()
   queue.append(5)
   queue.append("Mine")
   queue.append(True)
   queue.appendleft(10)
   print(queue)
   queue.rotate(2)
   print(queue)
   ```

2. `collections.Counter`
   ```python
   from collections import Counter

   arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
   word = "Hello World"
   lc = Counter(arr)
   wc = Counter(word)
   print(lc)
   print(wc)
   print(lc.most_common(2))
   print(wc.total())
   ```

3. `collections.defaultdict`
   ```python
   from collections import defaultdict

   d = defaultdict(int)
   d['a'] = 1
   d['b'] = 2
   print(d['c'])
   ```
