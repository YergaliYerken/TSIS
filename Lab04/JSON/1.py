import json

# Load data from the JSON file
with open('sample-data.json') as f:
    data = json.load(f)

# Print the header
print("Interface Status")
print("=" * 80)
print("{:<50}{:<20}{:<8}{:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Iterate through the data and print the required fields
for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')

    print("{:<50}{:<20}{:<8}{:<6}".format(dn, description, speed, mtu))
