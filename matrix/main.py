# Import NetworkTables to communicate with the RIO
from networktables import NetworkTables

from Matrix import Matrix

# Connect to the RIO as a client
NetworkTables.initialize(server='10.71.27.197')

# Get an instance of the table
ledTable = NetworkTables.getTable('PiLED/matrix')

matrix = Matrix()

def LED_value_changed(source, key, value, isNew):
    global matrix
    print("==================")
    filename = ledTable.getString("file", "")
    print("New file: " + filename)

    # Get media type
    effectType = ledTable.getString("type", "off")
    print("Of type: " + effectType)

    result = matrix.display(effectType, filename)
    ledTable.putBoolean("result", result)

    print("Result:")
    print(result)

ledTable.addEntryListener(LED_value_changed, True, "trigger")

print("Press Ctrl+C to exit")
while True:
    input()
