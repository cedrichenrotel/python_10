# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  scope_mysteries.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/09 17:34:29 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/10 10:44:56 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from _collections_abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter_mage() -> int:
        nonlocal count
        return count + 1
    return counter_mage


def main() -> None:
    # Memory Depths Test Data
    # initial_powers = [77, 72, 29]
    # power_additions = [5, 18, 14, 18, 18]
    # enchantment_types = ['Windy', 'Radiant', 'Earthen']
    # items_to_enchant = ['Shield', 'Sword', 'Wand', 'Armor']

    print("Testing mage counter...")
    counter1 = mage_counter()
    for c in range(2):
        print(f"counter1 call {c}: {counter1}")


if __name__ == "__main()__":
    main()
