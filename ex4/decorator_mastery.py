# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/13 16:58:42 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/14 13:07:25 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
try:
    from collections.abc import Callable
    from functools import wraps
    from time import time
except ImportError as e:
    print(f"[ERROR] : {e}")
    sys.exit(1)


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:

        print(f"Casting {func.__name__}...")
        start_time = time()
        rst = func(*args, **kwargs)
        end_time = time()
        estimated_time = end_time - start_time
        print(f"Spell completed in {estimated_time:.3f} seconds")
        print(f"Result: {rst}")

        return rst

    return wrapper


def power_validator(min_power: int) -> Callable:

    def validator_power(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> Callable:

            if kwargs.get('power') >= min_power:
                return func(*args, **kwargs)
            else:
                return ("Insufficient power for this spell")

        return wrapper

    return validator_power


def retry_spell(max_attempts: int) -> Callable:

    def spell_retry(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> str:

            for attempt in range(max_attempts):
                try:
                    rst = func(*args, **kwargs)
                    return rst
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"({attempt + 1}/{max_attempts})")

            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return spell_retry


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(n.isalpha() or n == ' ' for n in name):
            return True
        else:
            return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fire_spell(target: str, power: int) -> str:
        return f"{target} burns with {power} power"
    fire_spell('Dragon', power=5)

    print("\nTesting power_validator...")

    @power_validator(min_power=10)
    def fire_spell(target: str, power: int) -> None:
        return f"{target} burns with {power} power"
    print(fire_spell('goblin', power=5))

    print("\nTesting retrying spell...")

    count = [0]

    @retry_spell(3)
    def test_spell() -> str:

        count[0] += 1
        if count[0] < 3:
            raise Exception("failure")
        return "Waaaaaaagh spelled !"
    print(test_spell())

    print("\nTesting MageGuild...")
    test = MageGuild()
    print(test.validate_mage_name('alex'))
    print(test.validate_mage_name('Alex123'))

    print(test.cast_spell('Lightning', power=15))
    print(test.cast_spell('Lightning', power=5))


if __name__ == "__main__":
    main()
