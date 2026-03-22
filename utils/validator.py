class ResponseValidator:

    @staticmethod
    def is_not_empty(response):
        return response is not None and len(response.strip()) > 0

    @staticmethod
    def contains_keyword(response, keyword):
        return keyword.lower() in response.lower()

    @staticmethod
    def is_meaningful(response):
        # simple logic to check response quality
        return len(response.split()) > 3

    @staticmethod
    def no_error_message(response):
        return "error" not in response.lower()