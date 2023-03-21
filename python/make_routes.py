from .cipher_atok import AtoK
from .cipher_spejd import Spejd
from .cipher_morse import MorseEncode


def make_routes(lead_lines: str, no_of_routes: int, show_sequential=True, show_grouped=False, rotate_routes=False):

    leads = lead_lines.strip().splitlines(False)

    if len(leads) % no_of_routes != 0:
        raise Exception(
            f"The number of leads ({len(leads)}) should be a multiple of no_of_routes ({no_of_routes}).")

    # List of all places
    entries = []

    # Grouping the entries of each route
    routes = [[] for x in range(no_of_routes)]

    # Grouping [[entry0 of each route], [entry1 of each route], ...]
    groups = [[] for x in range(len(leads)//no_of_routes)]

    for n, lead in enumerate(leads):
        entry = {}
        entries.append(entry)
        group_index = n//no_of_routes
        route_index = n % no_of_routes
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
    for index, route in enumerate(routes):
        if rotate_routes:
            # Rotate the routes, making it so that they start in different groups
            for ii in range(index):
                head = route.pop(0)
                route.append(head)
        # Add location information to each entry
        # - It should be the clear text of the previous entry
        location = initialLocation
        for entry in route:
            entry.update(location=location)
            location = entry['clear_text']
        # Append the final entry
        endmark = dict(n=100, location=location, coded="*** SLUT ***",
                       clear_text="*** SLUT ***", cipher_spec="", alphabets=None)
        route.append(endmark)

    # Shift starting group
    def helpForMark(entry):
        alphabets = entry['alphabets']
        return f"Kodenøgle:\n{''.join(alphabets)}\n" if alphabets else ""

    if show_sequential:
        for index, route in enumerate(routes):
            print()
            print(f"Rute {index+1}:")
            print("-" * 30)
            for entry in route:
                print()
                param = dict(help=helpForMark(entry), **entry)
                print("Post {n}".format(**param))
                print("Placering: {location}".format(**param))
                print("Klartekst: {clear_text}".format(**param))
                print("{help}Kodetekst:".format(**param))
                print("{cipher_spec}: {coded}".format(**param))

    if show_grouped:
        for index, route in enumerate(groups):
            print()
            print(f"Gruppe {index+1}:")
            print("-" * 30)
            for entry in route:
                print()
                param = dict(help=helpForMark(entry), **entry)
                print("Post {n}".format(**param))
                print("Placering: {location}".format(**param))
                print("Klartekst: {clear_text}".format(**param))
                print("{help}Kodetekst:".format(**param))
                print("{cipher_spec}: {coded}".format(**param))
