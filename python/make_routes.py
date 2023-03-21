from .cipher_atok import AtoK
from .cipher_spejd import Spejd
from .cipher_morse import MorseEncode

def make_routes(lead_lines: str):

    leads = lead_lines.strip().splitlines(False)

    # List of all places
    entries = []
    no_of_routes = 4

    # Grouping the entries of each route
    routes = [[] for x in range(no_of_routes)]

    # Grouping [[entry0 of each route], [entry1 of each route], ...]
    groups = [[] for x in range(len(leads)//no_of_routes)]

    for n, lead in enumerate(leads):
        entry = {}
        entries.append(entry)
        group_index = n//no_of_routes
        route_index = n%no_of_routes
        groups[group_index].append(entry)
        routes[route_index].append(entry)
        cipher_spec, clear_text = lead.split(':')
        entry.update(clear_text=clear_text, cipher_spec=cipher_spec, n=n+1)
        # print(f"{cipher_spec}:{clear_text}")
        if cipher_spec == 'morse':
            coded = MorseEncode(clear_text)
            entry.update(coded=coded, alphabets=None)
            # print(f"{coded}\n")
        elif cipher_spec.startswith('a-'):
            coder = AtoK(cipher_spec[-1])
            coded = coder.encode(clear_text)
            alphabets = "\n".join(coder.alphabets())
            entry.update(coded=coded, alphabets=alphabets)
            # print(f"{alphabets}\n{coded}\n")
        else:
            coder = Spejd(cipher_spec)
            coded = coder.encode(clear_text)
            alphabets = "\n".join(coder.alphabets())
            entry.update(coded=coded, alphabets=alphabets)
            # print(f"{alphabets}\n{coded}\n")


    initialLocation = "*** Udleveres ***"
    # Shift starting group
    for ir, rt in enumerate(routes):
        for ii in range(ir):
            head = rt.pop(0)
            rt.append(head)
        location = initialLocation
        for entry in rt:
            entry.update(location=location)
            location = entry['clear_text']
        endmark = dict(n=100, location=location, coded="*** SLUT ***", clear_text="*** SLUT ***", cipher_spec="", alphabets=None)
        rt.append(endmark)

    # Shift starting group
    def helpForMark(entry):
        alphabets = entry['alphabets']
        return f"Kodenøgle:\n{''.join(alphabets)}\n" if alphabets else ""


    for ir, rt in enumerate(routes):
        print()
        print( f"Rute {ir+1}:")
        print( "-" * 30)
        for entry in rt:
            print( """
    Post {n}
    Placering: {location}
    Klartekst: {clear_text}
    {help}Kodetekst:
    {cipher_spec}: {coded}""".format(help=helpForMark(entry), **entry))



    for ir, rt in enumerate(groups):
        print()
        print( f"Gruppe {ir+1}:")
        print( "-" * 30)
        for entry in rt:
            print( """
    Post {n}
    Placering: {location}
    Klartekst: {clear_text}
    {help}Kodetekst:
    {cipher_spec}: {coded}""".format(help=helpForMark(entry), **entry))



