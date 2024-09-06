from typing import Dict

import google.generativeai as genai

from _config import GOOGLE_GEMINI_API_KEY
from application.utils.gemini_config import (
    GEMINI_MODEL,
    GEMINI_PROMPT,
    GEMINI_SYSTEM_INSTRUCTION,
)

# Configure the Gemini GenAI API in order to make requests to it
genai.configure(api_key=GOOGLE_GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name=GEMINI_MODEL, system_instruction=GEMINI_SYSTEM_INSTRUCTION
)


def get_gemini_summary(github_data: Dict[str, any]) -> str:
    """
    Generates a summary of the GitHub repository data using the Gemini model.

    This function takes in a dictionary containing GitHub repository data and
    uses the Gemini model to generate a summary based on that data.

    Args:
        github_data (Dict[str, any]): A dictionary containing GitHub repository information
            as JSON data.

    Returns:
        str: A text/markdown summary generated by the Gemini model, providing insights into the
            GitHub repository based on the provided data.
    """
    response = model.generate_content(f"{github_data} \n {GEMINI_PROMPT}")
    return response.text
