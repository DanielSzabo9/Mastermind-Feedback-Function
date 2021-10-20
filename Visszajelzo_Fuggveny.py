# Visszajelző függvény Mastermind/Színözön játékhoz, ami a tippek megadásával kiszámolja a találataidat

# Színek amiket használhatunk:
lehetosegek = ['sarga', 'zold', 'kek', 'piros', 'feher', 'fekete']

a = lehetosegek[3]  # Piros
b = lehetosegek[0]  # Sárga
c = lehetosegek[4]  # Fehér
d = lehetosegek[5]  # Fekete

talalgatas = [a, b, c, d]


def visszajelzes(tippek):
    megoldas = (lehetosegek[3], lehetosegek[1], lehetosegek[2], lehetosegek[4])
    visszajelzo_string = ''
    # A fekete pálcika helyett 'B'-t, a fehér helyett pedig 'W'-t használok visszajelzéskent. Ezek a színek angol neveire utalnak.

    for i in range(len(tippek)):
        if tippek[i] != megoldas[i]:
            for j in range(len(tippek)):
                if tippek[i] == megoldas[j]:
                    visszajelzo_string += 'W'
        else:
            visszajelzo_string += 'B'

    return visszajelzo_string


print(visszajelzes(talalgatas))
