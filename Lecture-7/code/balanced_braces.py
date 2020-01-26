from typing import List, Optional

# s = "{(({})[])}"
s = "((()))"


def check(s: str) -> None:
    """
    Checks if the given input string of brackets are balanced or not
    
    Args:
        s (str): The input string
    """

    stack: List[str] = []

    def get_opening(char: str) -> Optional[str]:
        """
        Gets the corresponding opening braces of the given input character.
        
        Args:
            char (str): The closing braces
        
        Returns:
            str: The corresponding open braces.
        """

        if char == ")":
            return "("
        
        if char == "]":
            return "["
        
        if char == "}":
            return "{"

        return None

    # for every character in the given input string
    for char in s:

        # if the string is an opening brace, push to stack
        if char in ("(", "{", "["):
            stack.append(char)
        
        else:
            try:
                # if the top element of the stack is the same as
                # the corresponding opening bracket of the current
                # character, pop the element
                if get_opening(char) == stack[-1]:
                    stack.pop()
                
                # else, the input string is unbalanced, break out of the
                # loop
                else:
                    break
            except IndexError:
                break
    else:
        # if the loop terminated normally, and stack is empty, print success message
        if len(stack) == 0:
            print("Balanced.")
        
        # else print unsuccessful message
        else:
            print("Not balanced.")
        return
    
    # since at this point the loop terminated abnormally, 
    # print unsuccessful message
    print("Not balanced.")

check(s)
