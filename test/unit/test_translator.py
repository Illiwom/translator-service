import vertexai
from mock import patch
from src.translator import query_llm_robust

class Response:
    def __init__(self, text):
        self.text = text


@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_chinese(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text = "0,This is a Chinese message"

    assert query_llm_robust("这是一条中文消息") == (False, "This is a Chinese message")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_llm_normal_response(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text = "1,hello"

    assert query_llm_robust("hello") == (True, "hello")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_llm_gibberish_response(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text = "awejfioasdf"

    assert query_llm_robust("awejfioasdf") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_no_comma(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text = "0Testing"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_nothing(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text = ""

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_no_translation(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text = "0,"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_no_english_boolean(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text = ",Testing"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_comma_out_of_place(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text = "1Tes,ting"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_smaller_integer(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text = "-1,Testting"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_larger_integer(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text = "5,Testing"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_crazy_input(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    # we mock the model's response to return a random message
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text ="2149*&(*&*^*&^)"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")

@patch('vertexai.preview.language_models._PreviewChatSession.send_message')
@patch('vertexai.preview.language_models.ChatModel.start_chat')
@patch('vertexai.preview.language_models._PreviewChatSession')
@patch('vertexai.preview.language_models.ChatModel')
@patch('vertexai.preview.language_models.ChatModel.from_pretrained')
def test_unexpected_language(mocker_from_pretrained, mocker_chat_model, mocker_preview_chat_session, mocker_start_chat, mocker_send_message):
    mocker_from_pretrained.return_value = mocker_chat_model
    mocker_start_chat.return_value = mocker_preview_chat_session
    mocker_send_message.return_value.text = "I don't understand your request"

    # TODO assert the expected behavior
    assert query_llm_robust("Aquí está su primer ejemplo.") == (False, "")