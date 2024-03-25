
# What is file handling and types of files? 
`Что такое обработка файлов и какие типы файлов существуют?`

- File handling is an important part of any web application. 
  ex: Uploading a profile picture, uploading a file, etc.
  - RU: Процесс работы с файлами в программе называется обработкой файлов.
  Например, загрузка изображения профиля, загрузка файла и т. д.
<br><br><br>

- Python has several functions for (CRUD) creating, reading, updating, and deleting files.
    - RU: Python имеет несколько функций для создания, чтения, обновления и удаления файлов.
<br><br><br>

- There are two types of files in Python:
    - RU: В Python существуют два типа файлов:
1. Text files
    - Text files are normal files that contain alphabets, numbers, and special characters. 
       - RU: Текстовые файлы - это обычные файлы, содержащие буквы, цифры и специальные символы.
2. Binary files
    - Binary files are used to store data in the form of bytes. Ex: images, videos, etc.
       - RU: Бинарные файлы используются для хранения данных в виде байтов. Например, изображения, видео и т. д.
<br><br><br>

# File handling Operations and Process
`Операции с файлами и процесс работы с файлами`

In python, a file operation takes place in the following order:
- RU: В Python операции с файлами выполняются в следующем порядке:

1. Open a file - [open()](https://www.w3schools.com/python/ref_func_open.asp)
2. Read or write (perform operation) - [read()](https://www.w3schools.com/python/ref_file_read.asp), [write()](https://www.w3schools.com/python/ref_file_write.asp)
3. Close the file - [close()](https://www.w3schools.com/python/ref_file_close.asp)


```python
# Open a file
file = open('file.txt', 'r')

# Read or write
print(file.read())

# Close the file
file.close()
```

<br><br><br>


# Opening a file
`Открытие файла`

In Python, we can work with files by using the built-in open() function.
- RU: В Python мы можем работать с файлами, используя встроенную функцию open().

```python
# It takes two parameters: file-name and mode.
# RU: Он принимает два параметра: имя файла и режим.
file = open('file.txt', 'r')
```

# Various modes
**`Различные режимы`**


- `'r' - Read` - Default value. Opens a file for reading. **Error if the file does not exist.** [See more...](https://www.w3schools.com/python/ref_file_read.asp)
    - RU: Открывает файл для чтения. Ошибка, если файл не существует.
- `'a' - Append` - Opens a file for appending, **creates the file if it does not exist.** 
    - RU: Открывает файл для добавления, создает файл, если он не существует.
- `'w' - Write` - Opens a file for writing, **creates the file if it does not exist.** [See more...](https://www.w3schools.com/python/ref_file_write.asp)
    - RU: Открывает файл для записи, создает файл, если он не существует.
- `'b' - Binary` - Binary mode (e.g., images). [See more...](https://www.geeksforgeeks.org/reading-binary-files-in-python/)
    - RU: Бинарный режим (например, изображения).


```python
# for creating a new file  -  RU: для создания нового файла

# file1 = open("myfile.txt", "x") 
file1 = open("myfile.txt", "w")
L = ["This is Samarkand \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()

# Append-adds at last
# append mode
file1 = open("myfile.txt", "a")

# writing newline character
file1.write("\n")
file1.write("Today")

# without newline character
file1.write("Tomorrow")


file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()
```

### Functions in modes
1. `read(size)` - Reads whole file [See more...](https://www.w3schools.com/python/ref_file_read.asp)
   - size parameter is optional and it is the number of bytes to be read from the file. If not provided, it reads the whole file.
2. `readline(size)` - Reads one line of the file [See more...](https://www.w3schools.com/python/ref_file_readline.asp)
3. `readlines()` - Reads all the lines of the file [See more...](https://www.w3schools.com/python/ref_file_readlines.asp)
4. `write()` - Writes the string to the file [See more...](https://www.w3schools.com/python/ref_file_write.asp)
5. `writelines(list[str])` - Writes a list of strings to the file [See more...](https://www.w3schools.com/python/ref_file_writelines.asp)

<br><br><br>
