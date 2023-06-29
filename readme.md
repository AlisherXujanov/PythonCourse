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
