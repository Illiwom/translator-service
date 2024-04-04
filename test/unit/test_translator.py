import vertexai
from mock import patch
from src.translator import query_llm_robust

@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_unexpected_language(mocker_from_pretrained, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker_send_message.return_value.text = "I don't understand your request"
    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_no_comma(mocker_from_pretrained, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker.return_value.text = "0Testing"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_nothing(mocker_from_pretrained, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker.return_value.text = ""

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_no_translation(mocker_from_pretrained, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker.return_value.text = "0,"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_no_english_boolean(mocker_from_pretrained, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker.return_value.text = ",Testing"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_comma_out_of_place(mocker_from_pretrained, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker.return_value.text = "1Tes,ting"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_smaller_integer(mocker_from_pretrained, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker.return_value.text = "-1,Testting"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_larger_integer(mocker_from_pretrained, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker.return_value.text = "5,Testing"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
def test_crazy_input(mocker_from_pretrained, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker.return_value.text = "2149*&(*&*^*&^)"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")