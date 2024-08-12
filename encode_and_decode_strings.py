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
    position = 1
    input = list(s)

    while position < len(input):
    
        if input[position]  == "#":
            char_count = int(input[position-1])
            str_to_add = "".join(input[position+1:position+char_count+1])
            output.append(str_to_add)

            # print(f"""
            #         Position {position}
            #         Char Count {char_count}
            #         Str to Add {str_to_add}                    
            #         """)

            position = position + char_count + 2
            
            # print(f"Ending position {position}")

    # print(f"\nInput {s}")
    # print(f"Final output: {output}\n")
    return output


decode_test_inputs = {
   "4#lint4#code4#love3#you": ["lint","code","love","you"],
   "2#we3#say1#:3#yes":["we", "say", ":", "yes"],
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




