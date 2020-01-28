import random


def main():
    COUNTRIES = "countries.txt"
    VERBS = "verbs.txt"
    GAMES = "games.txt"
    CONFLICTS = "conflicts.txt"

    with open(COUNTRIES) as f:
        countries_list = f.readlines()
    with open(VERBS) as f:
        verbs_list = f.readlines()
    with open(GAMES) as f:
        games_list = f.readlines()
    with open(CONFLICTS) as f:
        conflicts_list = f.readlines()

    countries_list = [x.strip() for x in countries_list]
    verbs_list = [x.strip() for x in verbs_list]
    games_list = [x.strip() for x in games_list]
    conflicts_list = [x.strip() for x in conflicts_list]

    c1 = random.choice(countries_list)
    countries_list.remove(c1)
    c2 = random.choice(countries_list)
    v = random.choice(verbs_list)
    g = random.choice(games_list)

    if random.random() > 0.5:
        cl = random.choice(conflicts_list)
        print("What if %s %s %s during the %s? %s" % (c1, v, c2, cl, g))
    else:
        print("What if %s %s %s? %s" % (c1, v, c2, g))


if __name__ == "__main__":
    main()
