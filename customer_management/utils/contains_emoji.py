"""
Module to check if name contains emoji
"""

import re

def contains_emoji(text):
    """
    Checks if the given text contains any emoji.
    
    Args: 
        text(str): Text to validate.
    
    Returns: 
        bool: True if the text contains emojis, False otherwise.
    """
    emoji_pattern = re.compile(
        "[" 
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "\U00002700-\U000027BF"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    return bool(emoji_pattern.search(text))
