1. random
2. math
3. time / datetime / calendar
4. os
5. sys
6. json
7. csv
8. re
9. requests
10. faker


# 1. random
-  RU: Модуль random предоставляет доступ к функциям, которые поддерживают множество операций.
   Возможно, самое важное - это то, что он позволяет генерировать случайные числа.

## random.random() : 
- Return the next random floating point number in the range [0.0, 1.0).
- RU: Возвращает следующее случайное число с плавающей запятой в диапазоне [0.0, 1.0).
## random.randint(a, b) : 
- Return a random integer N such that a <= N <= b.
- RU: Возвращает случайное целое число N такое, что a <= N <= b.
## random.choice(seq) : 
- Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
- RU: Возвращает случайный элемент из непустой последовательности seq. Если seq пуст, возникает IndexError.
## random.shuffle(x[, random]) : 
- Shuffle the sequence x in place.
- RU: Перемешивает последовательность x на месте.
---
# 2. math
- RU: Этот модуль предоставляет доступ к математическим функциям, определенным стандартом C.
(Стандартная библиотека C - это набор заголовочных файлов, которые определяют различные библиотечные функции и макросы.
Большинство функций стандартной библиотеки C также включены в стандартную библиотеку C ++, хотя и в разных заголовочных файлах.)

## math.ceil(x) : 
- Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
- RU: Возвращает потолок x в виде плавающего числа, наименьшее целое значение, большее или равное x.
## math.floor(x) : 
- Return the floor of x as a float, the largest integer value less than or equal to x.
- RU: Возвращает пол x в виде плавающего числа, наибольшее целое значение, меньшее или равное x.
## math.trunc(x) : 
- Return the Real value x truncated to an Integral (usually an integer). 
- RUL Возвращает действительное значение x, усеченное до целого (обычно целое число). 
## math.factorial(x) : 
- Return x factorial as an integer. Raises ValueError if x is not integral or is negative.
- RU: Возвращает факториал x в виде целого числа. Выдает ValueError, если x не является целым или отрицательным.  
## math.gcd(a, b) : 
- Return the greatest common divisor of the specified integer arguments. If any argument is nonzero, 
   then the absolute value of the greatest common divisor is smaller than or equal to the smallest absolute value of the arguments.
- RU: Возвращает наибольший общий делитель указанных целых аргументов. Если любой аргумент отличен от нуля, 
   то абсолютное значение наибольшего общего делителя меньше или равно наименьшему абсолютному значению аргументов.
## math.pow(x, y) : 
- Return x raised to the power y. Exceptional cases follow Annex ‘F’ of the C99 standard as far as possible. 
   In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0, even when x is a zero or a NaN. If both x and y are finite, 
   x is negative, and y is not an integer then pow(x, y) is undefined, and raises ValueError.
- RU: Возвращает x, возведенный в степень y. Исключительные случаи следуют Приложению «F» стандарта C99 насколько это возможно. 
   В частности, pow(1.0, x) и pow(x, 0.0) всегда возвращают 1.0, даже когда x является нулем или NaN. Если x и y конечны, 
   x отрицателен, а y не является целым числом, то pow(x, y) не определен и вызывает ValueError.
## math.sqrt(x) : 
- Return the square root of x.
- RU: Возвращает квадратный корень из x.
## math.pi : 
- The mathematical constant π = 3.141592…, to available precision.
- RU: Математическая константа π = 3.141592…, до доступной точности.
---
# 3. time / datetime / calendar

## time.time() :
- Return the time in seconds since the epoch as a floating point number.
- RU: Возвращает время в секундах с начала эпохи в виде числа с плавающей запятой.
```python
import time
print(time.time())
```
## time.sleep(secs) :
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

## time.localtime([secs]) :
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

## time.strftime(format[, t]) :
- Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument. 
   If t is not provided, the current time as returned by localtime() is used. 
   format must be a string. 
- RU: Преобразует кортеж или struct_time, представляющий время, возвращаемое gmtim() или localtime(), в строку, указанную аргументом format.
   Если t не предоставляется, используется текущее время, возвращаемое localtime().
   Формат должен быть строкой.
```python
print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))
```



## datetime.datetime.now() :
- Return the current local date and time.
- RU: Возвращает текущую локальную дату и время.
```python
import datetime
print(datetime.datetime.now())
```

## datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]) :
- The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. 
   The remaining arguments may be ints, longs, or floats, and may be positive or negative.
- RU: Требуются аргументы год, месяц и день. tzinfo может быть None или экземпляром подкласса tzinfo.
   Оставшиеся аргументы могут быть целыми числами, длинными или плавающими, и могут быть положительными или отрицательными.
```python
print(datetime.datetime(2020, 5, 17, 12, 30, 0, 0))
```


## calendar.month(year, month, w=0, l=0) :
- Returns a month’s calendar in a multi-line string using the formatmonth() of the TextCalendar class.
- RU: Возвращает календарь месяца в нескольких строках, используя formatmonth() класса TextCalendar.
```python
print(calendar.month(2020, 5))
print(calendar.calendar(2020))
print(calendar.isleap(2020))
# isleap is a function that returns True or False based on
# whether the year is a leap year or not
# example: print(calendar.isleap(2020)) will return True because 2020 is a leap year
# example: print(calendar.isleap(2021)) will return False because 2021 is not a leap year
# leap or not leap year is important because it affects the number of days in February (28 or 29)
```

## calendar.weekday(year, month, day) :
- Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).
- RU: Возвращает день недели (0 - понедельник) для года (1970-...), месяца (1-12), дня (1-31).
```python
print(calendar.weekday(2020, 5, 17))
```

## calendar.day_name[0-6]:
- An array that represents the days of the week in the current locale.
- RU: Массив, который представляет дни недели в текущей локали.
```python
print(calendar.day_name[calendar.weekday(2020, 5, 17)])
```


## calendar.month_name[0-12]:
- An array that represents the months of the year in the current locale. 
   This follows normal convention of January being month number 1, so it has a length of 13 and month_name[0] is the empty string.
- RU: Массив, который представляет месяцы года в текущей локали.
   Это следует обычной конвенции, что январь является месяцем номер 1, поэтому он имеет длину 13, а month_name[0] - пустая строка.
```python
print(calendar.month_name[5])
```
# 4. os module
- The OS module in Python provides functions for interacting with the operating system. 
   OS comes under Python’s standard utility modules. 
   This module provides a portable way of using operating system-dependent functionality. 
   The *os* and *os.path* modules include many functions to interact with the file system.
- RU: Модуль OS в Python предоставляет функции для взаимодействия с операционной системой.
   OS входит в стандартные служебные модули Python.
   Этот модуль обеспечивает переносимый способ использования зависимой от операционной системы функциональности.
   Модули *os* и *os.path* включают множество функций для взаимодействия с файловой системой.

## os.getcwd() :
- Return a string representing the current working directory.
- RU: Возвращает строку, представляющую текущий рабочий каталог.
```python
print(os.getcwd())
```
## os.chdir(path) :
- Change the current working directory to path.
- RU: Изменяет текущий рабочий каталог на path.
```python
os.chdir("C:\\Users\\User\\Desktop")
print(os.getcwd())
```
## os.listdir(path='.') :
- Return a list containing the names of the entries in the directory given by path. 
   The list is in arbitrary order, and does not include the special entries '.' and '..' even if they are present in the directory.
- RU: Возвращает список, содержащий имена записей в каталоге, заданном путем.
   Список в произвольном порядке и не включает специальные записи "." и "..", даже если они присутствуют в каталоге.
```python
print(os.listdir())
```
# 5. sys module
- This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. 
- RU: Этот модуль предоставляет доступ к некоторым переменным, используемым или поддерживаемым интерпретатором, и к функциям, которые сильно взаимодействуют с интерпретатором.

## sys.argv :
- The list of command line arguments passed to a Python script. argv[0] is the script name (it is operating system dependent whether this is a full pathname or not). 
   If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'. 
   If no script name was passed to the Python interpreter, argv[0] is the empty string.
- RU: Список аргументов командной строки, переданных сценарию Python. argv[0] - это имя сценария (это зависит от операционной системы, является ли это полным именем пути или нет).
   Если команда была выполнена с использованием параметра командной строки -c для интерпретатора, argv[0] устанавливается в строку "-c".
   Если сценарию Python не было передано имя сценария, argv[0] - пустая строка.
```python
print(sys.argv)
# sys.argv[0] is the name of the script
# output: [daily.py]
```

# 6. json




