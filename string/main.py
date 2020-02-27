# Import NetworkTables to communicate with the RIO
from networktables import NetworkTables

from String import String

# Connect to the RIO as a client
NetworkTables.initialize(server='DESKTOP-T5DSCVI.local')

# Get an instance of the table
ledTable = NetworkTables.getTable('PiLED/strip')

string = String()

def LED_value_changed(source, key, value, isNew):
    global string
    print("==================")
    print("New file: " + value)

    # Get media type
    effectType = ledTable.getString("type", "off")
    print("Of type: " + effectType)

    result = string.display(effectType, value)
    ledTable.putBoolean("result", result)

    print("Result:")
    print(result)

ledTable.addEntryListener(LED_value_changed, True, "file")

print("Press Ctrl+C to exit")
while True:
    input()
