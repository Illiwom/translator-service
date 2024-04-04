import vertexai
from mock import patch

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_unexpected_language(mocker):
    # we mock the model's response to return a random message
    mocker.return_value.text = "I don't understand your request"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_no_comma(mocker):
    # we mock the model's response to return a random message
    mocker.return_value.text = "0Testing"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_nothing(mocker):
    # we mock the model's response to return a random message
    mocker.return_value.text = ""

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_no_translation(mocker):
    # we mock the model's response to return a random message
    mocker.return_value.text = "0,"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_no_english_boolean(mocker):
    # we mock the model's response to return a random message
    mocker.return_value.text = ",Testing"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_comma_out_of_place(mocker):
    # we mock the model's response to return a random message
    mocker.return_value.text = "1Tes,ting"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_smaller_integer(mocker):
    # we mock the model's response to return a random message
    mocker.return_value.text = "-1,Testting"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_larger_integer(mocker):
    # we mock the model's response to return a random message
    mocker.return_value.text = "5,Testing"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_crazy_input(mocker):
    # we mock the model's response to return a random message
    mocker.return_value.text = "2149*&(*&*^*&^)"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")