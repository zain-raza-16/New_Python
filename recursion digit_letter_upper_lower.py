def main(string):
    input_str = string
    output_str = ""
    sub_arr(input_str,output_str)

def sub_arr(inp,out):
    if inp == "":
        print(out)
        return
    else:
        value = inp[0]

        inp = inp[1:]
        out_1 = out + value
        sub_arr(inp,out_1)
        if value.isnumeric():
           return
        elif value.isupper():
            value = value.lower()
            out_2 = out + value
            sub_arr(inp,out_2)
        else:
            value = value.upper()
            out_2 = out + value
            sub_arr(inp, out_2)
        return

print("______")
main("aB3Cd")