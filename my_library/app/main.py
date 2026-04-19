from fastapi import FastAPI
from my_library.my_library.math_utils import calculate_mean, factorial
from my_library.my_library.string_utils import reverse_string, count_vowels

app = FastAPI()


@app.get("/")
def read_root():
    """Return a welcome message for the API root endpoint."""
    return {"message": "Добро пожаловать в API библиотеки"}


@app.get("/mean")
def get_mean(numbers: str):
    """Parse comma-separated numbers and return their arithmetic mean."""
    try:
        numbers_list = [float(n) for n in numbers.split(",")]
        return {"result": calculate_mean(numbers_list)}
    except ValueError:
        return {"error": "Неверный формат чисел"}


@app.get("/factorial/{n}")
def get_factorial(n: int):
    """Return the factorial for a non-negative integer value."""
    try:
        return {"result": factorial(n)}
    except ValueError as e:
        return {"error": str(e)}


@app.get("/reverse")
def get_reverse(text: str):
    """Return reversed text string."""
    return {"result": reverse_string(text)}


@app.get("/count_vowels")
def get_count_vowels(text: str):
    """Return the number of English vowels in the input text."""
    return {"result": count_vowels(text)}
