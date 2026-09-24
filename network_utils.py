import socket


def list_network_interfaces():
    print("\n=== Interfaces réseau disponibles ===")

    interfaces = socket.if_nameindex()

    if not interfaces:
        print("Aucune interface réseau trouvée.")
        return []

    names = []

    for index, name in interfaces:
        print(f"{index} : {name}")
        names.append(name)

    return names