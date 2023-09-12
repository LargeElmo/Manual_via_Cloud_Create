def decimal_to_utf8(decimal_code_point):
    # Convert decimal code point to UTF-8 bytes
    try:
        # Ensure the code point is within the valid range
        if 0 <= decimal_code_point <= 0x10FFFF:
            if decimal_code_point <= 0x7F:
                # Single-byte UTF-8
                utf8_bytes = bytes([decimal_code_point])
            elif decimal_code_point <= 0x7FF:
                # Two-byte UTF-8
                utf8_bytes = bytes([
                    0xC0 | ((decimal_code_point >> 6) & 0x1F),
                    0x80 | (decimal_code_point & 0x3F)
                ])
            elif decimal_code_point <= 0xFFFF:
                # Three-byte UTF-8
                utf8_bytes = bytes([
                    0xE0 | ((decimal_code_point >> 12) & 0x0F),
                    0x80 | ((decimal_code_point >> 6) & 0x3F),
                    0x80 | (decimal_code_point & 0x3F)
                ])
            else:
                # Four-byte UTF-8
                utf8_bytes = bytes([
                    0xF0 | ((decimal_code_point >> 18) & 0x07),
                    0x80 | ((decimal_code_point >> 12) & 0x3F),
                    0x80 | ((decimal_code_point >> 6) & 0x3F),
                    0x80 | (decimal_code_point & 0x3F)
                ])

            return utf8_bytes
        else:
            return None  # Invalid code point
    except ValueError:
        return None  # Invalid input

# Input from the user
decimal_input = int(input("Enter a decimal code point: "))

# Convert decimal code point to UTF-8 bytes
utf8_result = decimal_to_utf8(decimal_input)

if utf8_result is not None:
    print("UTF-8 Representation:", utf8_result)
else:
    print("Invalid input or code point out of range.")
