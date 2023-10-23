apartmani = [
    {'gym': False, 'school': True, 'store': False},
    {'gym': True, 'school': False, 'store': False},
    {'gym': True, 'school': True, 'store': False},
    {'gym': False, 'school': True, 'store': False},
    {'gym': False, 'school': True, 'store': True}
]

trenutni_apartman = None
najbolji_apartman = None
najmanji_broj_koraka = float('inf')

for indeks, apartman in enumerate(apartmani):
    koraci = 0
    if apartman['gym']:
        koraci += 1
    if apartman['school']:
        koraci += 1
    if apartman['store']:
        koraci += 1

    if koraci < najmanji_broj_koraka:
        trenutni_apartman = apartman
        najbolji_apartman = apartman
        najmanji_broj_koraka = koraci
        redni_broj = indeks + 1

print(f"Najbolji apartman: {najbolji_apartman}, Minimalan broj koraka (koliko je najmanje koraka potrebno obaviti za doći do bilo čega): {najmanji_broj_koraka}. Apartman na rednom broju {indeks}.")
