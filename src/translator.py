from vertexai.preview.language_models import ChatModel, InputOutputTextPair

def query_llm_robust(post: str) -> tuple[bool, str]:
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    print(chat_model)
    parameters = {
        "temperature": 0.7,
        "max_output_tokens": 256
    }
    context = '''
    Return the following outputs:
    1 if the text is in English and 0 otherwise
    The original exact text (case-sensitive) if it is unreadable/invalid, and an English translation of the entire text given otherwise
    Make these two outputs comma-separated csv-format in one line and no space between the comma and the translation in the form boolean,english_translation
    Text:'''
    try:
        chat = chat_model.start_chat(context=context)
        response = chat.send_message(post, **parameters)
    except: 
        return (False, "")
    comma_index = response.text.find(',')
    if comma_index == -1:
        return (False, "")
    try:
        number_provided = int(response.text[:comma_index])
    except:
        return (False, "")
    if number_provided != 0 and number_provided != 1:
        return (False, "")
    boolean = number_provided == 1
    translation = response.text[comma_index + 1:]
    if translation == "":
        return (False, "")
    return (boolean, translation)


def translate_content(content: str) -> tuple[bool, str]:
    return query_llm_robust(content)