def main(k):
    output = ""
    left = k  # )
    right = k # (
    solve(output,right,left)

def solve(output,right,left):
    if right == 0 and left == 0:
        print(output)
        return
    else:
        if right != 0:
            output_1 = output + "("
            solve(output_1,right - 1 ,left)
        if left - 1 >= right:
            output_2 = output + ")"
            solve(output_2, right , left - 1)
        return

main(5)

