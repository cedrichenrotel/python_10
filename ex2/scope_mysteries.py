# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  scope_mysteries.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/09 17:34:29 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/13 14:03:49 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from _collections_abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter_mage() -> int:
        nonlocal count
        count += 1
        return count
    return counter_mage


def spell_accumulator(initial_power: int) -> Callable:
    initial = initial_power

    def accumulator_spell(add: int) -> int:
        nonlocal initial
        initial += add
        return initial
    return accumulator_spell


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda item: enchantment_type + " " + item


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> dict:
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {'Store': store, 'Recall': recall}


def main() -> None:
    counter1 = mage_counter()
    counter2 = mage_counter()
    print("Testing mage counter...")
    for c in range(3):
        print(f"counter1 call {c + 1}:{counter1()}")
        if c < 1:
            print(f"counter2 call {c + 1}:{counter2()}")

    print("\nTesting spell accumulator..")
    initial_power = 100
    new_power = spell_accumulator(initial_power)
    print(f"Base {initial_power}, add 20: {new_power(20)}")
    print(f"Base {initial_power}, add 30: {new_power(30)}")

    print("\nTesting enchantment factory...")
    factory = [
        enchantment_factory('Flaming'),
        enchantment_factory('Frozen')
    ]
    enchantment = [
        factory[0]('Sword'),
        factory[1]('Shield')
    ]
    list(map(print, enchantment))

    print("Testing memory vault...")
    vault = memory_vault()
    vault['Store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['Recall']('secret')}")
    print(f"Recall 'unknown': {vault['Recall']('unknown')}")


if __name__ == "__main__":
    main()
