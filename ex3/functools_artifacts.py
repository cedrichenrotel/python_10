# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  functools_artifacts.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/13 07:43:25 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/14 15:38:48 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
try:
    from functools import reduce, partial, lru_cache, singledispatch
    from operator import add, mul
    from collections.abc import Callable
    from typing import Any
except ImportError as e:
    print(f"[Error] {e}")
    sys.exit(1)


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    elif operation == 'add':
        return reduce(add, spells)
    elif operation == 'multiply':
        return reduce(mul, spells)
    elif operation == 'max':
        return reduce(max, spells)
    elif operation == 'min':
        return reduce(min, spells)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def base_enchantment(power: int, element: str, target: str) -> str:
    return (f"{element} enchantment of power {power} on {target}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "Fire": partial(base_enchantment, 50, "Fire"),
        "Water": partial(base_enchantment, 50, "Water"),
        "Air": partial(base_enchantment, 50, "Air")
    }


@lru_cache(None)
def memoized_fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError(f"fib({n}) is not int")
    if n == 0 or n == 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(data):
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(data):
        return (f"{data} damage")

    @dispatcher.register(str)
    def _(data):
        return (f"{data}")

    @dispatcher.register(list)
    def _(data):
        return (f"{len(data)} spells")

    return dispatcher


def main() -> None:
    print("Testing spell reducer...")
    try:
        spell_powers = [45, 41, 10, 21, 16, 22]
        operations = ['add', 'multiply', 'max', 'min']
        for i in operations:
            rst = spell_reducer(spell_powers, i)
            print(f"{i.capitalize()}: {rst}")
    except (TypeError, ValueError) as e:
        print(f"[ERROR] {e}")

    print("\nTesting partial enchanter...")
    try:
        targets = ['dragon', 'goblin', 'ork']
        elements = ["Fire", "Water", "Air"]
        enchantment = (partial_enchanter(base_enchantment))
        for target, element in zip(targets, elements):
            print(enchantment[element](target))
    except KeyError as e:
        print(f"[ERROR] Unknown key: {e}")

    print("\nTesting memoized fibonacci...")
    try:
        fibonacci_tests = [13, 16, 15]
        for test in fibonacci_tests:
            print(f"fib({test}): {memoized_fibonacci(test)}")
    except TypeError as e:
        print(f"[ERROR] {e}")

    print("\nTesting spell dispatcher...")
    test = spell_dispatcher()
    print(f"Damage spell: {test(42)}")
    print(f"Enchantment: {test('fireball')}")
    print(f"Multi-cast: {test(['Fire', 'Water', 'Air'])}")
    print(test(None))


if __name__ == "__main__":
    main()
