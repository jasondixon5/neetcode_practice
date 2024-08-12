"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Because the string may contain any of the 256 legal ASCII characters, your algorithm must be able to handle any character that may appear

Do not rely on any libraries, the purpose of this problem is to implement the "encode" and "decode" algorithms on your own

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

Input: ["we", "saysaysaysay", ":", "yes"]
Output: ["we", "saysaysaysaysay", ":", "yes"]
"""

# TODO: Fix bug where length value above 9 would not be captured accurately
#       when decoding string

def encode_string(str_list):
    """
    Encode a list of strings into a single string
    """
    DELIM = "#"
    encoded_string = ""

    for elem in str_list:
        elem_len = str(len(elem))
        new_elem = f"{elem_len}{DELIM}{elem}"
        encoded_string += new_elem
    
    return encoded_string

encode_test_inputs = {
   tuple(["lint","code","love","you"]): "4#lint4#code4#love3#you",
   tuple(["we", "say", ":", "yes"]): "2#we3#say1#:3#yes"
}

def test_encode_string():
    
    for input, expected in encode_test_inputs.items():

        sol = encode_string(input)

        try:
            assert sol == expected
        except AssertionError:
            print(f"Test failed on input {input}\nExpected: {expected}\nReceived: {sol}")
            raise AssertionError


def decode_string(s):
    """
    Decode a single string into a list of strings
    """

    output = []
    position = 0
    input = list(s)
    

    while position < len(input):

        delim_pos = position

        # Increment j counter until find the '#' delimiter
        while input[delim_pos] != "#":
            delim_pos += 1

        # Count indicator is from position counter up to but not incl delim
        count_arr = input[position:delim_pos]
        count_int = int("".join(count_arr))
        # char_count = int(input[position:delim_pos])
        str_to_add = input[delim_pos+1:delim_pos+1+count_int]
        output.append(str_to_add)
        position = delim_pos + count_int

        print(f"""
                Position {position}
                Char Count {count_arr}
                Count Int {count_int}
                Str to Add {str_to_add}                    
                """)

            
            # print(f"Ending position {position}")

    # print(f"\nInput {s}")
    # print(f"Final output: {output}\n")
    return output


decode_test_inputs = {
   "4#lint4#code4#love3#you": ["lint","code","love","you"],
   "2#we3#say1#:3#yes":["we", "say", ":", "yes"],
   "2#we12#saysaysaysay1#:3#yes": ["we", "saysaysaysay", ":", "yes"],
}

def test_decode_string():

    for input, expected in decode_test_inputs.items():

        sol = decode_string(input)

        try:
            assert sol == expected
        except AssertionError:
            print(f"Test failed on input {input}\nExpected: {expected}\nReceived: {sol}")
            raise AssertionError



# def introspect_decode():
    
#     for input, expected in decode_test_inputs.items():
#         decode_string(input)

# if __name__ == "__main__":
#     introspect_decode()




