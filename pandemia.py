people = input()


def infected(s):
    population = 0
    people_infected = 0
    continents = s.split('X')
    print(continents)
    for continent in continents:
        population += len(continent)
        print(f"{continent}={continent.find('1')}"
        )
        if continent.find('1') >= 0:
            people_infected += len(continent)
    if people_infected == 0:
        return 0
    else:
        return 100*people_infected/len(s)


print(infected(people))
