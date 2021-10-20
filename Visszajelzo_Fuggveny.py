# Visszajelző függvény Mastermind/Színözön játékhoz, ami a tippek megadasaval kiszámolja a találataidat


# Futtató környezet:

# Színek amiket használhatunk:
lehetosegek = ['sarga', 'zold', 'kek', 'piros', 'feher', 'fekete']

a = lehetosegek[3]  # Piros
b = lehetosegek[0]  # Sárga
c = lehetosegek[4]  # Fehér
d = lehetosegek[5]  # Fekete

talalgatas = [a, b, c, d]
megoldas = (lehetosegek[3], lehetosegek[1], lehetosegek[2], lehetosegek[4])

# Kért függvény:


def visszajelzes(tippek, kod):
    visszajelzo_string = ''
    # A fekete pálcika helyett 'B'-t, a fehér helyett pedig 'W'-t használok visszajelzéskent. Ezek a színek angol neveire utalnak.
    # (Mivel a magyar neveik ugyanazzal a betűvel kezdődnek, ezért használom az angol kezdőbetűt.)

    for i in range(len(tippek)):
        if tippek[i] != kod[i]:
            for j in range(len(tippek)):
                if tippek[i] == kod[j]:
                    visszajelzo_string += 'W'
        else:
            visszajelzo_string += 'B'

    return visszajelzo_string


print(visszajelzes(talalgatas, megoldas))
