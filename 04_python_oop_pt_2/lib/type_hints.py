def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


headline
# <function headline at 0x105b81268>

print(headline(7, align="left"))

print(headline("python type checking", align="center"))