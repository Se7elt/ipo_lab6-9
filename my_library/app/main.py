from fastapi import FastAPI 
from my_library.my_library.math_utils import calculate_mean, factorial
from my_library.my_library.string_utils import reverse_string, count_vowels
app = FastAPI() 
 
@app.get("/") 
def read_root(): 
    return {"message": "Добро пожаловать в API библиотеки"} 
 
@app.get("/mean") 
def get_mean(numbers: str): 
    try: 
        numbers_list = [float(n) for n in numbers.split(",")] 
        return {"result": calculate_mean(numbers_list)} 
    except ValueError: 
        return {"error": "Неверный формат чисел"} 
 
@app.get("/factorial/{n}") 
def get_factorial(n: int): 
    try: 
        return {"result": factorial(n)} 
    except ValueError as e: 
        return {"error": str(e)} 
 
@app.get("/reverse") 
def get_reverse(text: str): 
    return {"result": reverse_string(text)} 
 
@app.get("/count_vowels") 
def get_count_vowels(text: str): 
    return {"result": count_vowels(text)} 
