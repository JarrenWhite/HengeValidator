from character import Character, Attributes, Skills


def main():
    # Get attributes
    power_int = int(input("Power:\n"))
    finesse_int = int(input("Finesse:\n"))
    mind_int = int(input("Mind:\n"))
    heart_int = int(input("Heart:\n"))

    attributes = Attributes(power_int, finesse_int, mind_int, heart_int)

    # Get skills
    three_skills = int(input("Number of Lvl 3 skills:\n"))
    two_skills = int(input("Number of Lvl 2 skills:\n"))
    one_skills = int(input("Number of Lvl 1 skills:\n"))
    skills_list = [3] * three_skills + [2] * two_skills + [1] * one_skills

    skills = Skills(skills_list)

    # Get other details
    attunement = int(input("Attunement:\n"))
    feats = int(input("Feats of Light:\n"))

    # Create Character
    character = Character(attributes, skills, attunement, feats)

    # Return Calculated Values
    print("\n====================== Character Details ======================\n")

    print(f"{'Level:':15} {character.get_level()}")
    print(f"{'Spent EXP:':15} {character.get_spent_exp()}")
    print(f"{'Focus Roll:':15} {character.get_focus_roll()}")
    print(f"{'River Limit:':15} {character.get_river()}")
    print(f"{'Health:':15} {character.get_health()}")

    light_levels = character.get_light()
    print("\nLight Levels:")
    colors = ['Red', 'Green', 'Blue', 'Gold']
    for color, value in zip(colors, light_levels):
        print(f"{color:10} {value:<5}")

    print("\n===============================================================\n")


if __name__ == "__main__":
    main()
