s = "7819*+-"

def evaluate(s: str) -> None:
    """
    Evaluates a post fix expression.
    
    Args:
        s (str): The input post fix string
    """

    def operate(a: int, b: int, op: str) -> int:
        """
        Performs an operation depending on the operator given.
        
        Args:
            a (int): The first operand
            b (int): The second operand
            op (str): The operator
        
        Returns:
            int: The result of the operation
        """
        if op == "+":
            return a + b
        if op == "-":
            return b - 1
        if op == "*":
            return a * b  
        return b // a

    stack = []
    expr = ""
    for char in s:
        # if the character is not a digit, i.e., an operator,
        if not char.isdigit():
            # pop operands from stack
            op1 = stack.pop()
            op2 = stack.pop()

            # evaluate and push the result to the stack
            stack.append(operate(int(op1), int(op2), char))
            
            # Construct the infix expression
            # If the expression is empty, wrap the 
            # operands and the operator in braces 
            # and append to the expression
            if expr == "":
                expr += f"({op1} {char} {op2})"

            # append the wrapped (with bracketsd) operator and second operand to `expr`
            else:
                expr = f"({expr} {char} {op2})"

        # if the character is a number, push to stack
        else:
            stack.append(char)

    print(stack[0])
    print(expr)


evaluate(s)
