#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/08 10:58:51 by cehenrot        #+#    #+#               #
#  Updated: 2026/04/15 09:52:54 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda x: x['power'])['power'],
        'min_power': min(mages, key=lambda x: x['power'])['power'],
        'avg_power': (round(sum(map(lambda x: x['power'],
                                    mages)) / len(mages), 2))
    }


def main() -> None:
    artifacts = [
        {'name': 'Light Prism', 'power': 96, 'type': 'accessory'},
        {'name': 'Shadow Blade', 'power': 79, 'type': 'relic'},
        {'name': 'Ice Wand', 'power': 101, 'type': 'accessory'},
        {'name': 'Storm Crown', 'power': 107, 'type': 'accessory'}
        ]

    mages = [
        {'name': 'Alex', 'power': 79, 'element': 'shadow'},
        {'name': 'Jordan', 'power': 80, 'element': 'lightning'},
        {'name': 'Kai', 'power': 83, 'element': 'earth'},
        {'name': 'Ember', 'power': 55, 'element': 'fire'},
        {'name': 'Zara', 'power': 88, 'element': 'lightning'}
        ]

    spells = ['meteor', 'shield', 'lightning', 'tsunami']

    artifact_trier = artifact_sorter(artifacts)
    filter_mage = power_filter(mages, 86)
    spell_trans = spell_transformer(spells)
    mages_stat = mage_stats(mages)

    print("Testing artifact sorter...")
    for a in artifact_trier:
        print(str(a).strip("{}").replace("'", ""))
    print("\ntesting mage filter...")
    print(str(filter_mage).replace("'", '').strip("{['']}"))
    print("\ntesting mage statistics...")
    print(str(mages_stat).replace("''{'", '').strip("{[]}"))
    print("\nTesting spell transformer...")
    print(str(spell_trans).replace("', '", ' ').strip("['']"))


if __name__ == "__main__":
    main()
