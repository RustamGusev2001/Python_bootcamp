def my_decorator(func: any) -> any:
    def wrapper(purse: dict):
        print('SQUEAK')
        return func(purse)

    return wrapper

@my_decorator
def add_ingot(purse: dict[str, int]):
    copy: dict[str, int] = purse.copy()
    if "gold_ingots" in copy:
        copy["gold_ingots"] += 1
    else:
        copy["gold_ingots"] = 1
    return copy

@my_decorator
def get_ingot(purse: dict[str, int]):
    copy: dict[str, int] = purse.copy()
    if "gold_ingots" in copy and copy["gold_ingots"] > 0:
        copy["gold_ingots"] -= 1
    return copy

@my_decorator
def empty(purse: dict[str, int]):
    copy: dict[str, int] = {}
    return copy


if __name__ == "__main__":
    d: dict[str, int] = {'gold_ingots': 10, 'silver_ingots': 13, 'copper_ingots': 10}

    print(add_ingot(d))
    print(get_ingot(d))
    print(empty(d))
