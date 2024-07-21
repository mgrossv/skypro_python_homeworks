import pytest
from string_utils import StringUtils

utils = StringUtils()

# capitilize Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст

def test_capitilize():
    """pozitive"""
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("maria") == "Maria"
    assert utils.capitilize("1993") == "1993"
    """negative"""
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("987654тестирую") == "987654тестирую"

# trim Принимает на вход текст и удаляет пробелы в начале, если они есть

def test_trim():
    # pozitive
    assert utils.trim(" skypro") == "skypro"
    assert utils.trim(" hello") == "hello"
    assert utils.trim(" QA ") == "QA "
    # negative
    assert utils.trim("") == ""

# to_list Принимает на вход текст с разделителем и возвращает список строк
     # Параметры: 
     # `string` - строка для обработки \n
     # `delimeter` - разделитель строк. По умолчанию запятая (",")

@pytest.mark.parametrize('string, delimeter, result',[
    ("стол,ручка,стул", ",", ["стол", "ручка", "стул"]),
    ("9,8,7,6,5", ",",["9", "8", "7", "6", "5"]),
    # negative
    ("", None,[]),
    ("1,2,3,4,5", None,["1", "2", "3", "4", "5"])
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

# contains Возвращает `True`, если строка содержит искомый символ и `False` - если нет

@pytest.mark.parametrize('string, symbol, result',[
    ("собака", "с", True),
    (" кошка", "к", True),
    ("888", "8", True),
    ("", "", True),
    
    ("креветка", "б", False),
    (" лимон", "е", False),
    ("чай ", "ф", False),
    ("увлажнитель воздуха", "&", False),
    ("9999", "1", False),
    # ("криминал", "", False) # дефект 
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result
    
# delete_symbol Удаляет все подстроки из переданной строки

@pytest.mark.parametrize('string, symbol, result',[
    ("собака", "с", "обака"),
    ("кошка", "ш", "кока"),
    ("Маруся", "М", "аруся"),
    ("878", "7", "88"),
    
    ("сон", "л", "сон"),
    ("", "", ""),
    ("отпуск", "", "отпуск"),
    ("", "д", "")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

 # starts_with Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n 

@pytest.mark.parametrize('string, symbol, result',[
    ("собака", "с", True),
    ("", "", True),
    ("Gross", "G", True),
    ("988", "9", True),
    
    ("Новосибирск", "н", False),
    ("просекко", "П", False),
    ("", "ф", False),
    ("", "&", False),
    ("брют", "1", False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

# end_with Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n

@pytest.mark.parametrize('string, symbol, result',[
    ("марк", "к", True),
    ("", "", True),
    ("ИЮЛЬ", "Ь", True),
    ("889", "9", True),
    
    ("лето", "л", False),
    ("жара", "б", False),
    ("", "ф", False),
    ("брют", "Т", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

# is_empty Возвращает `True`, если строка пустая и `False` - если нет \n

@pytest.mark.parametrize('string, result',[
    ("", True),
    (" ", True),
    ("  ", True),
    
    ("ттттт", False),
    (" ттт", False),
    ("010101", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

# list_to_string Преобразует список элементов в строку с указанным разделителем \n

@pytest.mark.parametrize('lst, joiner, result',[
    (["бело","чёрный"], "-", "бело-чёрный"),
    (["1","2"], ",", "1,2"),
    (["раз","два"], " ", "раз два"),

    ([], None, ""),
    ([], ",", ""),
    ([], "8888", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result

