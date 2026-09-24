from network_utils import list_network_interfaces


interfaces = list_network_interfaces()

print("\nNombre d'interfaces trouvées :", len(interfaces))