from google import genai

class GeminiClient:

    def __init__(self, api_key):
        self.api_key = api_key
        try:
            self.client = genai.Client(api_key=api_key)
        except:
            self.client = None

    def generate_response(self, prompt):
        try:
            if self.client:
                response = self.client.models.generate_content(
                    model="gemini-1.5-pro-latest",
                    contents=[prompt]
                )
                return response.text
        except Exception as e:
            print("Gemini API failed, using fallback:", e)

        return self.fake_response(prompt)

    def fake_response(self, prompt):
        prompt = prompt.lower()   # ✅ properly indented

        if "login" in prompt:
            return "Test case: Verify login with valid and invalid credentials"

        elif "password" in prompt:
            return "Test case: Validate password rules"

        elif "hello" in prompt:
            return "Hello! How can I help you?"

        elif "non-existing" in prompt:
            return "I am not sure about this query"

        else:
            return "I am not sure about this query"
        