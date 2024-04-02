from src.translator import translate_content, query_llm
from mock import patch


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_llm_normal_response():
    is_english, translated_content = translate_content("Ceci est un message en français")
    assert is_english == False
    assert translated_content == "This is a French message"

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("idosajfawio;efaio;we")
    assert is_english == False
    assert translated_content == ""


@patch('src.translator.query_llm')
def test_unexpected_language(mocker):
    # we mock the model's response to return a random message
    mocker.return_value = "I don't understand your request"

    # TODO assert the expected behavior
    assert translate_content("Aquí está su primer ejemplo.") == (False, "")

@patch('src.translator.query_llm')
def test_no_comma(mocker):
    # we mock the model's response to return a random message
    mocker.return_value = "0Testing"

    # TODO assert the expected behavior
    assert translate_content("Aquí está su primer ejemplo.") == (False, "")

@patch('src.translator.query_llm')
def test_nothing(mocker):
    # we mock the model's response to return a random message
    mocker.return_value = ""

    # TODO assert the expected behavior
    assert translate_content("Aquí está su primer ejemplo.") == (False, "")

@patch('src.translator.query_llm')
def test_no_translation(mocker):
    # we mock the model's response to return a random message
    mocker.return_value = "0,"

    # TODO assert the expected behavior
    assert translate_content("Aquí está su primer ejemplo.") == (False, "")

@patch('src.translator.query_llm')
def test_no_english_boolean(mocker):
    # we mock the model's response to return a random message
    mocker.return_value = ",Testing"

    # TODO assert the expected behavior
    assert translate_content("Aquí está su primer ejemplo.") == (False, "")

@patch('src.translator.query_llm')
def test_comma_out_of_place(mocker):
    # we mock the model's response to return a random message
    mocker.return_value = "1Tes,ting"

    # TODO assert the expected behavior
    assert translate_content("Aquí está su primer ejemplo.") == (False, "")

@patch('src.translator.query_llm')
def test_smaller_integer(mocker):
    # we mock the model's response to return a random message
    mocker.return_value = "-1,Testting"

    # TODO assert the expected behavior
    assert translate_content("Aquí está su primer ejemplo.") == (False, "")

@patch('src.translator.query_llm')
def test_larger_integer(mocker):
    # we mock the model's response to return a random message
    mocker.return_value = "5,Testing"

    # TODO assert the expected behavior
    assert translate_content("Aquí está su primer ejemplo.") == (False, "")

@patch('src.translator.query_llm')
def test_crazy_input(mocker):
    # we mock the model's response to return a random message
    mocker.return_value = "2149*&(*&*^*&^)"

    # TODO assert the expected behavior
    assert translate_content("Aquí está su primer ejemplo.") == (False, "")