import openai

class translator:
    language, sentence = None, None

    # here is the API key for OpenAI.
    openai.api_key = ''

    def __init__(self, language, sentence):
        self.language, self.sentence = language, sentence

    def translate(self):
        prompt = f"Translate the following English text to '{self.language}': '{self.sentence}'"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature = 0.1,
            max_tokens= 250
        )

        translated_text = response.choices[0].text.strip()
        return translated_text





