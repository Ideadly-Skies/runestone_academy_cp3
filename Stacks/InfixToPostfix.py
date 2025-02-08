from Stack import Stack

def infix_to_postfix(infix_expr: str):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()
    
    for token in token_list:
        token = token.lower()

        if token in "abcdefghijklmnopqrstuvwxyz" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()

            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty() and prec[op_stack.peek()] >= prec[token]):
                # postfix_list append the operands w/ high priority from op_stack
                postfix_list.append(op_stack.pop())
            op_stack.push(token) # push the token operator to op_stack

    # while the op_stack is not empty push postfix_list
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    # return the string rep of postfix_list
    return " ".join(postfix_list) 

if __name__ == "__main__":
    """
    algorithm:
        1. push operands to the postfix_list
        2. push operator to the op_list:
            1. if the operator is (, push it directly to the op_list
            2. if the operator is ), while the current op that is popped from the stack is not (, keep popping and appending to postfix_list
            3. else, while the top of the op_stack still has operator with higher than or equal to precedence with incoming operator, pop it from the stack
               and then push the incoming operator to the op_stack
        3. while the op_stack is not empty, push the remaining ops to the postfix list
    
    """
    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(infix_to_postfix("( A + B ) * ( C + D )"))

    # final exercise
    print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))