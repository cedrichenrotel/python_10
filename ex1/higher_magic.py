#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  higher_magic.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/08 18:08:44 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/09 14:44:25 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from collections.abc import Callable


def fire_spell(target: str, power: int) -> str:
    return f"{target} burns with {power} power"


def ice_spell(target: str, power: int) -> str:
    return f"{target} is frozen with {power} power"


def air_spell(target: str, power: int) -> str:
    return f"{target} tornado with a power of {power} power"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def spell(target: str, power: int) -> str:
        rst1 = spell1(target, power)
        rst2 = spell2(target, power)
        return (rst1, rst2)
    return spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier_power(target: str, power: int) -> str:
        rst = base_spell(target, power * multiplier)
        return rst
    return amplifier_power


def is_powerful(target: str, power: int) -> bool:
    return power >= 50


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster_conditional(target: str, power: int) -> str:
        if condition(target, power):
            rst1 = spell(target, power)
            return rst1
        return "Spell fizzled"
    return caster_conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[Callable]:
        return [s(target, power) for s in spells]
    return sequence_spell


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fire_spell, ice_spell)
    rst = combined('Dragon', 20)
    print(f"Combined spell result: {rst[0]}, {rst[1]}")

    print("\nTesting power amplifier...")
    original = fire_spell('Dragon', 20)
    amplified_power = power_amplifier(fire_spell, 2)
    amplified = amplified_power('Dragon', 20)
    print(f"Original: {original}, Amplified: {amplified}")

    print("\nTesting conditional caster...")
    conditional = conditional_caster(is_powerful, fire_spell)
    print(conditional('Dragon', 50))

    print("\nTesting spell sequence...")
    lst_spell = [
        fire_spell,
        ice_spell,
        air_spell
    ]
    sequence = spell_sequence(lst_spell)
    rst = sequence('Dragon', 50)
    print(str(rst).strip("['']").replace("', '", "\n"))


if __name__ == "__main__":
    main()
