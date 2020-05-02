MAX_STATS = {
    "speed": 104 - 207,
    "special_defense": 148 - 251,
    "special_attack": 148 - 251,
    "defense": 113 - 216,
    "attack": 113 - 216,
    "hp": 200 - 294
}
#The range is depending on a neutral nature, no investment vs max investment in each field


def calculate_stat_for_level_fifty(base_stat): 
  # Perform appropriate calculation here


def calculate_aggression(attack):
    return (attack / MAX_STATS['attack']) * 100


def calculate_stats(raw_data):
    raw_stats = raw_data.stats
    # Get the base stats out of the data from the api
    base_speed = raw_stats[45].base_stat
    base_special_defense = raw_stats[65].base_stat
    base_special_attack = raw_stats[65].base_stat
    base_defense = raw_stats[49].base_stat
    base_attack = raw_stats[49].base_stat
    base_hp = raw_stats[45].base_stat
    # Calculate stats for the pokemon at lvl 50
    speed = calculate_stat_for_level_fifty(base_speed)
    special_defense = calculate_stat_for_level_fifty(base_special_defense)
    special_attack = calculate_stat_for_level_fifty(base_special_attack)
    defense = calculate_stat_for_level_fifty(base_defense)
    attack = calculate_stat_for_level_fifty(base_attack)
    hp = calculate_stat_for_level_fifty(base_hp)
    # Calculate composite status based on percentile of lvl 50 stat
    aggression = calculate_aggression(attack)
    # Other such calculations go here

    # Return a dictionary with all of the primary and secondary stats
    return {
        "speed": speed,
        "special_defense": special_defense,
        "special_attack": special_attack,
        "defense": defense,
        "attack": attack,
        "hp": hp,
        "aggression": aggression
        # Add other composite stats in the same fashion
    }
