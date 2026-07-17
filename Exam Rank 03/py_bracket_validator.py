def bracket_validator(s: str) -> bool:
    parenthesis = {
        "(" : ")",
        "{": "}",
        "[": "]"
    }
    close = []

    for c in s:
        if c in parenthesis:
            close.append(parenthesis[c])
        elif c in ")}]":
            if not close or close[-1] != c:
                return False
            close.pop()
    
    #return len(close) == 0
    return not close



print(bracket_validator("()"))
print(bracket_validator("()[]{}"))
print(bracket_validator("(]"))
print(bracket_validator("([)]"))
print(bracket_validator("{[]}"))
print(bracket_validator("hello(world)"))
print(bracket_validator("((())"))
print(bracket_validator(""))
## true true false false true true false true