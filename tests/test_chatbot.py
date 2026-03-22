import os
from dotenv import load_dotenv
from utils.api_client import GeminiClient
from utils.validator import ResponseValidator
from utils.logger import log   
import pytest

load_dotenv()

def test_login_response():
    log("Starting test: test_login_response")

    client = GeminiClient(os.getenv("API_KEY"))

    response = client.generate_response("Write test cases for login page")

    log(f"Response: {response}")

    assert ResponseValidator.is_not_empty(response)
    assert ResponseValidator.contains_keyword(response, "login")
    assert ResponseValidator.is_meaningful(response)
    assert ResponseValidator.no_error_message(response)

    log("Test passed: test_login_response")


def test_empty_prompt():
    log("Starting test: test_empty_prompt")

    client = GeminiClient(os.getenv("API_KEY"))
    response = client.generate_response("")

    log(f"Response: {response}")

    assert ResponseValidator.is_not_empty(response)

    log("Test passed: test_empty_prompt")


def test_random_prompt():
    log("Starting test: test_random_prompt")

    client = GeminiClient(os.getenv("API_KEY"))
    response = client.generate_response("asdjkhaskjdh123")

    log(f"Response: {response}")

    assert ResponseValidator.is_not_empty(response)

    log("Test passed: test_random_prompt")


def test_hallucination_check():
    log("Starting test: test_hallucination_check")

    client = GeminiClient(os.getenv("API_KEY"))
    response = client.generate_response("Give API for non-existing website")

    log(f"Response: {response}")

    assert "not sure" in response.lower() or "cannot" in response.lower()

    log("Test passed: test_hallucination_check")


@pytest.mark.parametrize("prompt, keyword", [
    ("login test cases", "login"),
    ("password validation", "password"),
    ("hello", "hello"),
])
def test_multiple_inputs(prompt, keyword):
    log(f"Starting test: test_multiple_inputs | Prompt: {prompt}")

    client = GeminiClient(os.getenv("API_KEY"))
    response = client.generate_response(prompt)

    log(f"Response: {response}")

    assert keyword in response.lower()

    log(f"Test passed for prompt: {prompt}")
