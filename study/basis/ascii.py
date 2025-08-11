# ascii conversion
def ascii_to_char(ascii_value):
    """
    Convert an ASCII value to its corresponding character.
    
    :param ascii_value: An integer representing the ASCII value.
    :return: The corresponding character as a string.
    """
    if 0 <= ascii_value <= 127:
        return chr(ascii_value)
    else:
        raise ValueError("ASCII value must be in the range 0-127")

def char_to_ascii(character):
    """
    Convert a character to its corresponding ASCII value.
    
    :param character: A single character string.
    :return: The ASCII value of the character as an integer.
    """
    if len(character) == 1:
        return ord(character)
    else:
        raise ValueError("Input must be a single character string")

if __name__ == "__main__":
    # Example usage
    try:
        ascii_value = 65
        character = ascii_to_char(ascii_value)
        print(f"ASCII {ascii_value} corresponds to character '{character}'")

        character = 'A'
        ascii_value = char_to_ascii(character)
        print(f"Character '{character}' corresponds to ASCII {ascii_value}")
    except ValueError as e:
        print(e)