from time import sleep

def utf8_range_display(start, end):
    # Check if the start and end values are valid code points
    if start < 0 or end < 0 or start > 0x10FFFF or end > 0x10FFFF:
        print("Invalid code point values. Code points must be in the range 0x0000 to 0x10FFFF.")
        return

    print(f"UTF-8 characters in the range {hex(start)} to {hex(end)}:")
    for code_point in range(start, end + 1):
        try:
            character = chr(code_point)
            print(f"Code Point: {hex(code_point)}, Character: {character.encode('utf-8').decode('utf-8', 'ignore')}")
            
            
            
        except UnicodeEncodeError:
            # Skip characters that can't be encoded in UTF-8
            pass

if __name__ == "__main__":
    
    
    
    
    start_point = int(input("Enter the starting code point value in hexadecimal (e.g., 0x0041): "), 16)
    end_point = int(input("Enter the ending code point value in hexadecimal (e.g., 0x005A): "), 16)
    
    utf8_range_display(start_point, end_point)
