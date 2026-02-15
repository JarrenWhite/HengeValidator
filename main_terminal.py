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

    print(skills_list)

    skills = Skills(skills_list)

    # Get other details
    attunement = int(input("Attunement:\n"))
    feats = int(input("Feats of Light:\n"))

    # Create Character
    character = Character(attributes, skills, attunement, feats)


if __name__ == "__main__":
    main()
