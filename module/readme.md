# 🎯 Here are some resources to help you get started with Python and exercise 💪👇️

### Practice Python (https://www.practicepython.org/)
### HackerRank (https://www.hackerrank.com/domains/python)
### Project Euler (https://projecteuler.net/archives)
### Codewars (https://www.codewars.com/kata/search/python)


# 👇️ Install pipenv
1. python -m pip uninstall virtualenv pipenv -y
2. py -m pip uninstall virtualenv pipenv -y
3. python3 -m pip uninstall virtualenv pipenv -y
4. python -m pip install --upgrade setuptools wheel
5. python -m pip install --user pipenv

## or 
#### python -m pip install pipenv 

###### If you however get 
```
    'pipenv' is not recognized as an internal or external command, operable program or batch file 
```
###### get the Python>- path to the base directory for the user site-packages by running:
###### Mine is C:\Users\drgabrielharris\AppData\Roaming\Python\Python37\site-packages
###### Replace site-packages in the path with Scripts then add to your system PATH 
###### (on Windows: Edit environment variables for your account > in the User variables select 
###### Path > Edit > New > C:\Users\drgabrielharris\AppData\Roaming\Python\Python37\Scripts )


# 🎯 To create requirements.txt file
1. ```pipenv lock -r > requirements.txt```  - is outdated
2. New version is: ```pipenv run pip freeze  > requirements.txt```


___
# Modules

<!--* https://codete.com/blog/10-built-in-modules-in-python-you-should-know#overview -->
<!--* https://levelup.gitconnected.com/11-most-useful-built-in-python-modules-you-might-not-know-yet-eff3e0e6f586 -->

1. random (https://docs.python.org/3/library/random.html)
2. math 
3. - time (https://docs.python.org/3/library/time.html)
   - datetime (https://www.pythoncheatsheet.org/modules/datetime-module)
   - timedelta (https://www.pythoncheatsheet.org/modules/datetime-module)
4. json (https://medium.com/analytics-vidhya/json-in-python-163857b00415)
5. logging  (https://medium.com/pythoneers/master-logging-in-python-73cd2ff4a7cb)
6. re (https://medium.com/analytics-vidhya/regular-expression-in-python-5ab2e8b707f1)
7. requests
8.  faker
9.  googletranslate
10. collections


## 1. random
-  RU: Модуль random предоставляет доступ к функциям, которые поддерживают множество операций.
   Возможно, самое важное - это то, что он позволяет генерировать случайные числа.

#### random.random() : 
- Return the next random floating point number in the range [0.0, 1.0).
- RU: Возвращает следующее случайное число с плавающей запятой в диапазоне [0.0, 1.0).
#### random.randint(a, b) : 
- Return a random integer N such that a <= N <= b.
- RU: Возвращает случайное целое число N такое, что a <= N <= b.
- ex:
  ```python
   import random
   print(random.randint(0, 10))
  ```
#### random.choice(seq) : 
- Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
- RU: Возвращает случайный элемент из непустой последовательности seq. Если seq пуст, возникает IndexError.
- ex:
  ```python
   import random
   x = [i for i in range(10)]
   print(x)
   print(random.choice(x))
  ```
#### random.shuffle(x[, random]) : 
- Shuffle the sequence x in place.
- RU: Перемешивает последовательность x на месте.
- ex:
  ```python
   import random
   x = [[i] for i in range(10)]
   print(x)
   random.shuffle(x)
   print(x)
  ```
---
## 2. math
- RU: Этот модуль предоставляет доступ к математическим функциям, определенным стандартом C.
(Стандартная библиотека C - это набор заголовочных файлов, которые определяют различные библиотечные функции и макросы.
Большинство функций стандартной библиотеки C также включены в стандартную библиотеку C ++, хотя и в разных заголовочных файлах.)

#### math.ceil(x) : 
- Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
- RU: Возвращает потолок x в виде плавающего числа, наименьшее целое значение, большее или равное x.
#### math.floor(x) : 
- Return the floor of x as a float, the largest integer value less than or equal to x.
- RU: Возвращает пол x в виде плавающего числа, наибольшее целое значение, меньшее или равное x.
#### math.trunc(x) : 
- Return the Real value x truncated to an Integral (usually an integer). 
- RUL Возвращает действительное значение x, усеченное до целого (обычно целое число). 
#### math.factorial(x) : 
- Return x factorial as an integer. Raises ValueError if x is not integral or is negative.
- RU: Возвращает факториал x в виде целого числа. Выдает ValueError, если x не является целым или отрицательным.  
#### math.gcd(a, b) : 
- Return the greatest common divisor of the specified integer arguments. If any argument is nonzero, 
   then the absolute value of the greatest common divisor is smaller than or equal to the smallest absolute value of the arguments.
- RU: Возвращает наибольший общий делитель указанных целых аргументов. Если любой аргумент отличен от нуля, 
   то абсолютное значение наибольшего общего делителя меньше или равно наименьшему абсолютному значению аргументов.
ex:
```python
import math
print(math.gcd(10, 20))
```

#### math.pow(x, y) : 
- Return x raised to the power y. Exceptional cases follow Annex ‘F’ of the C99 standard as far as possible. 
   In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0, even when x is a zero or a NaN. If both x and y are finite, 
   x is negative, and y is not an integer then pow(x, y) is undefined, and raises ValueError.
- RU: Возвращает x, возведенный в степень y. Исключительные случаи следуют Приложению «F» стандарта C99 насколько это возможно. 
   В частности, pow(1.0, x) и pow(x, 0.0) всегда возвращают 1.0, даже когда x является нулем или NaN. Если x и y конечны, 
   x отрицателен, а y не является целым числом, то pow(x, y) не определен и вызывает ValueError.
#### math.sqrt(x) : 
- Return the square root of x.
- RU: Возвращает квадратный корень из x.
#### math.pi : 
- The mathematical constant π = 3.141592…, to available precision.
- RU: Математическая константа π = 3.141592…, до доступной точности.
---
## 3. time / datetime / timedelta

#### time.time() :
- Return the time in seconds since the epoch as a floating point number.
- RU: Возвращает время в секундах с начала эпохи в виде числа с плавающей запятой.
```python
import time
print(time.time())
```
#### time.sleep(secs) :
- Suspend execution of the calling thread for the given number of seconds. 
   The argument may be a floating point number to indicate a more precise sleep time. 
   The actual suspension time may be less than that requested because any caught signal will terminate the sleep() following execution of that signal’s catching routine. 
   Also, the suspension time may be longer than requested by an arbitrary amount because of the scheduling of other activity in the system.
- RU: Приостанавливает выполнение вызывающего потока на заданное количество секунд.
   Аргументом может быть число с плавающей запятой, чтобы указать более точное время сна.
   Фактическое время приостановки может быть меньше запрошенного, потому что любой перехваченный сигнал прерывает sleep() после выполнения процедуры перехвата этого сигнала.
   Кроме того, время приостановки может быть дольше запрошенного на произвольную величину из-за планирования другой активности в системе.
```python
time.sleep(1) # sleep for 1 second
```

#### time.localtime([secs]) :
- Convert a time expressed in seconds since the epoch to a struct_time in time. 
   If secs is not provided or None, the current time as returned by time() is used. 
   Fractions of a second are ignored. 
   Note that since not all time functions handle leap seconds, this is not necessarily a precise inverse function to time().
- RU: Преобразует время, выраженное в секундах с начала эпохи, в struct_time в time.
   Если secs не предоставляется или None, используется текущее время, возвращаемое time().
   Доли секунды игнорируются.
   Обратите внимание, что поскольку не все функции времени обрабатывают високосные секунды, это не обязательно точная обратная функция к time().

```python
print(time.localtime(UNIX-time))
```

#### time.strftime(format[, t]) :
- Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument. 
   If t is not provided, the current time as returned by localtime() is used. 
   format must be a string. 
- RU: Преобразует кортеж или struct_time, представляющий время, возвращаемое gmtime() или localtime(), в строку, указанную аргументом format.
   Если t не предоставляется, используется текущее время, возвращаемое localtime().
   Формат должен быть строкой.
```python
print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))

1. %y  => is year in short version  =>  Годы в краткой версии
2. %Y  => is year in full version  =>  Годы в полной версии
3. %m  => is month in number =>  Месяцы в числовом формате
4. %M  => is minute in number =>  Минуты в числовом формате
5. %d  => is day in number =>  Дни в числовом формате
6. %D  => is Date (full date) =>  Дата (полная дата)
7. %h  => is month in short version =>  Месяцы в краткой версии
8. %H  => is hour in number =>  Часы в числовом формате
9. %s  => DOES NOT EXIST =>  НЕ СУЩЕСТВУЕТ
10. %S => is second in number =>  Секунды в числовом формате
```



#### datetime.datetime.now() :
- Return the current local date and time.
- RU: Возвращает текущую локальную дату и время.
```python
import datetime
print(datetime.datetime.now())
```

#### datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]) :
- The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. 
   The remaining arguments may be ints, longs, or floats, and may be positive or negative.
- RU: Требуются аргументы год, месяц и день. tzinfo может быть None или экземпляром подкласса tzinfo.
   Оставшиеся аргументы могут быть целыми числами, длинными или плавающими, и могут быть положительными или отрицательными.
```python
print(datetime.datetime(2020, 5, 17, 12, 30, 0, 0))
```

### Timedelta
- EN: The timedelta class is used to represent the `difference` between two dates or times.
- RU: Класс timedelta используется для представления `разницы` между двумя датами или временем.
```python
import datetime
print(datetime.timedelta(days=365, hours=5, minutes=1))
```

- timedelta can add `days`, `seconds` and `microseconds` to a datetime object
- RU: timedelta может добавлять `дни`, `секунды` и `микросекунды` к объекту datetime
```python
import datetime
now = datetime.now()
print(now)
>>> datetime.datetime(2023, 7, 31, 12, 30, 10, 999999)

print(now + datetime.timedelta(days=365))
>>> datetime.datetime(*2024*, 7, 30, 12, 30, 10, 999999)
```

# 4. json




