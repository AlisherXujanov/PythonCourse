// # 1. Create a function that can take many params as args and sums them all up
// # If any of the params is not a number, skip it
// # ------------------------------------------------
// # RU: Создайте функцию, которая может принимать множество параметров и 
// # суммирует все эти параметры. Если какой-то из параметров не является числом,
// # то пропустите его
// def sum_all(*args) -> int:
//     total = 0
//     for item in args:
//         if type(item) == int:
//             total += item
//     return total

// # print(sum_all(["Mirsaid", 2, 2, 6, 10, 'Ozodjon', 5]))

// # ================================================
// # 2. Create a function that takes string and counts vowels and consonants in it
// # ------------------------------------------------
// # RU: Создайте функцию, которая принимает строку и считает в ней гласные 
// # и согласные буквы
// все_гласные = "aouie"
// test_text = "This is for you"
// def считать_гласные_согласные(текст:str="") -> str:
//     гласные = ''
//     согласные = ''
//     for буква in текст:
//         if буква.isspace() == False:
//             if буква in все_гласные:
//                 гласные += буква
//             else:
//                 согласные += буква
//     return f"Гласные => {len(гласные)}...  Сoгласные => {len(согласные)}"
            
// # print(считать_гласные_согласные(test_text))

// # ================================================
// # 3. Create a function that finds last letter of the sentence and finds 
// # how many times it occured in the sentence
// # RU: Создайте функцию, которая находит последнюю букву предложения и
// # считает сколько раз она встречается в предложении

// def последная_буква(текст:str='') -> str:
//     последная = текст[-1]
//     return f"Буква {последная} встречается {текст.count(последная)} раз"

// print(последная_буква("Hello world"))
    
// # ================================================
// # 4. Create a function that counts uppercase and lowercase letters
// # RU: Создайте функцию чтобы он считал большие и маленькие буквы

// def считать_большие_маленькие(текст:str='') -> str:
//     uppers = ''
//     lowers = ''
//     for letter in текст:
//         if not letter.isspace():
//             if letter.isupper():
//                 uppers += letter
//             else:
//                 lowers += letter
//     return f"Большие => {len(uppers)}...  Маленькие => {len(lowers)}"
        
// print(считать_большие_маленькие("Hello World"))

console.log("Hello world")