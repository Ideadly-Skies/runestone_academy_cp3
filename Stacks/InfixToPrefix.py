from Stack import Stack
from InfixToPostfix import infix_to_postfix

def infix_to_prefix(infix_expr: str):
    """algoritm to convert infix to prefix expression"""
    infix_expr_rev = "" 
    for char in infix_expr[::-1]:
        if char == "(":
            infix_expr_rev += ") "
        elif char == ")":
            infix_expr_rev += "( "
        else:
            infix_expr_rev += char + " "
    # strip infix_expr_rev from whitespace
    infix_expr_rev = infix_expr_rev.rstrip()

    # convert infix_expr_rev to postfix
    infix_expr_rev_postfix = infix_to_postfix(infix_expr_rev)

    # reverse infix_expr_rev_postfix
    return infix_expr_rev_postfix[::-1]

# test run
if __name__ == "__main__":
    print(infix_to_prefix("( A + B ^ C ) * D + E ^ 5"))