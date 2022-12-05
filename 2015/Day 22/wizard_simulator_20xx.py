"""Day 22: Wizard Simulator 20XX"""
from queue import PriorityQueue
from typing import NamedTuple, Optional

with open("2015/Day 22/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


class Effect(NamedTuple):
    lasts: int
    armor: int = 0
    damage: int = 0
    mana: int = 0


class Spell(NamedTuple):
    cost: int
    damage: int = 0
    heal: int = 0
    effect: Optional[str] = None


class Player(NamedTuple):
    hp: int
    mana: int = 0
    damage: int = 0
    # [effect ends turn, effect name]
    effects: tuple[tuple[int, str], ...] = ()

    def active_effects(self, turn: int):
        return tuple(
            (end_turn, effect) for end_turn, effect in self.effects if end_turn >= turn
        )


EFFECTS = {
    "Shield": Effect(lasts=6, armor=7),
    "Poison": Effect(lasts=6, damage=3),
    "Recharge": Effect(lasts=5, mana=101),
}

SPELLS = {
    # Magic Missile costs 53 mana. It instantly does 4 damage.
    "Magic Missile": Spell(cost=53, damage=4),
    # Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
    "Drain": Spell(cost=73, damage=2, heal=2),
    # Shield costs 113 mana. It starts an effect that lasts for 6 turns.
    # While it is active, your armor is increased by 7.
    "Shield": Spell(cost=113, effect="Shield"),
    # Poison costs 173 mana. It starts an effect that lasts for 6 turns.
    # At the start of each turn while it is active, it deals the boss 3 damage.
    "Poison": Spell(cost=173, effect="Poison"),
    # Recharge costs 229 mana. It starts an effect that lasts for 5 turns.
    # At the start of each turn while it is active, it gives you 101 new mana.
    "Recharge": Spell(cost=229, effect="Recharge"),
}


def part1(data: str, hp: int = 50, mana: int = 500, hp_drain=False):
    """Part 1 solution"""
    player = Player(hp=hp, mana=mana)
    boss_hp, boss_damage = parse(data)
    boss = Player(hp=boss_hp, damage=boss_damage)
    todo = PriorityQueue()
    for spell in SPELLS:
        todo.put(((0, 0), (1, player, boss, spell, 0)))
    seen = set()
    while not todo.empty():
        _, (turn, player, boss, spell, total_mana) = todo.get()
        if (player, boss, spell) in seen:
            continue
        seen.add((player, boss, spell))
        if player.hp <= 0:
            continue
        if boss.hp <= 0:
            return total_mana
        if turn % 2:
            try:
                player, boss, spent = player_turn(turn, player, boss, spell, hp_drain)
            except AssertionError:
                continue
            new_total = total_mana + spent
            todo.put(((new_total, boss.hp), (turn + 1, player, boss, "", new_total)))
            continue
        player, boss, spent = boss_turn(turn, player, boss)
        for spell in SPELLS:
            new_total = total_mana + spent
            todo.put(((new_total, boss.hp), (turn + 1, player, boss, spell, new_total)))


def part2(data: str):
    """Part 2 solution"""
    return part1(data, hp_drain=True)


def parse(data: str):
    hp, damage = (int(line.split()[-1]) for line in data.splitlines())
    return hp, damage


def player_turn(turn: int, player: Player, boss: Player, spell_name: str, hp_drain):
    player_hp = player.hp
    if hp_drain:
        player_hp -= 1
    assert player_hp > 0
    mana = player.mana
    poison_damage = 0
    active_effects = player.active_effects(turn)
    forbiddend_spells = set()
    for end_turn, effect_name in active_effects:
        if end_turn > turn:
            forbiddend_spells.add(effect_name)
        effect = EFFECTS[effect_name]
        mana += effect.mana
        poison_damage += effect.damage

    boss_hp = boss.hp - poison_damage
    if boss_hp <= 0:
        return player, Player(hp=0), 0

    spell = SPELLS[spell_name]
    assert spell_name not in forbiddend_spells
    assert mana >= spell.cost
    boss_hp -= spell.damage
    mana -= spell.cost
    player_hp += spell.heal
    if new_effect := spell.effect:
        effect_end_turn = turn + EFFECTS[new_effect].lasts
        active_effects = active_effects + ((effect_end_turn, new_effect),)
        # print(turn, active_effects)
    updated_player = Player(hp=player_hp, mana=mana, effects=active_effects)
    updated_boss = Player(hp=boss_hp, damage=boss.damage)
    return updated_player, updated_boss, spell.cost


def boss_turn(turn: int, player: Player, boss: Player):
    active_effects = player.active_effects(turn)
    mana = player.mana
    armor = 0
    poison_damage = 0
    for _, effect_name in active_effects:
        effect = EFFECTS[effect_name]
        mana += effect.mana
        poison_damage += effect.damage
        armor += effect.armor
    boss_hp = boss.hp - poison_damage
    if boss_hp <= 0:
        return player, Player(hp=0), 0
    damage_to_player = max(1, boss.damage - armor)
    updated_player = Player(
        hp=player.hp - damage_to_player,
        mana=mana,
        effects=active_effects,
    )
    updated_boss = Player(
        hp=boss_hp,
        damage=boss.damage,
    )
    return updated_player, updated_boss, 0


def show_stats(turn: int, player: Player, boss: Player):
    active_effects = player.active_effects(turn)
    armor = sum(EFFECTS[effect].armor for _, effect in active_effects)
    print(f"- Player has {player.hp} hit points, {armor} armor, {player.mana} mana")
    print(f"- Boss has {boss.hp} hit points")


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
