import time

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

def generate_utf8_range(start, end):
    utf8_range = {}
    for code_point in range(start, end + 1):
        utf8_bytes = decimal_to_utf8(code_point)
        if utf8_bytes is not None:
            utf8_range[code_point] = utf8_bytes
            # time.sleep(0.2)  # Sleep for 0.2 seconds between iterations
    return utf8_range

# Input from the user
start_decimal = int(input("Enter the starting decimal code point: "))
end_decimal = int(input("Enter the ending decimal code point: "))

# Generate and display UTF-8 representations for the specified range
utf8_range = generate_utf8_range(start_decimal, end_decimal)

if utf8_range:
    print("UTF-8 Representations for the specified range:")
    for code_point, utf8_bytes in utf8_range.items():
        time.sleep(0.9)
        print(f"Code Point {code_point} (UTF-8): {utf8_bytes}")
else:
    print("Invalid input or code point range out of bounds.")
