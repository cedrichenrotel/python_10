# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/13 16:58:42 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/13 19:07:38 by cehenrot        ###   ########.fr        #
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


def fire_spell(target: str, power: int) -> str:
    return f"{target} burns with {power} power"


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


def main() -> None:
    # test_powers = [13, 27, 25, 14]
    # spell_names = ['meteor', 'heal', 'freeze', 'earthquake']
    # mage_names = ['Kai', 'Zara', 'Sage', 'River', 'Casey', 'Riley']
    # invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("Testing spell timer...")
    deco = spell_timer(fire_spell)
    deco('dragon', 50)


if __name__ == "__main__":
    main()
