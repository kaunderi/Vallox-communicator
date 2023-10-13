# Vallox Configuration

# MQTT Configuration
MQTT_BROKER = "mqtt://your-mqtt-broker-url"  # Replace with your MQTT broker URL
MQTT_TOPIC = "vallox"  # Replace with your MQTT topic
MQTT_USERNAME = "your-mqtt-username"  # Replace with your MQTT username
MQTT_PASSWORD = "your-mqtt-password"  # Replace with your MQTT password

# Serial Port Configuration
SERIAL_PORT = (
    "/dev/ttyUSB0"  # Replace with the serial port your Vallox device is connected to
)
BAUD_RATE = 9600

# Define temperature identifiers and lookup values
TEMP_IDENTIFIERS = {
    0: "TEMP_0",
    1: "TEMP_1",
    # Add more temperature identifiers as needed
}

TEMP_LOOKUP = {
    0: 20.0,
    1: 22.5,
    # Add more temperature lookup values as needed
}

# Define fan speed lookup values
FANSPEED_LOOKUP = {
    0: "LOW",
    1: "MEDIUM",
    2: "HIGH",
}

# Define fan speed settings
FANSPEED_SET = {
    "LOW": b"\x01",
    "MEDIUM": b"\x02",
    "HIGH": b"\x03",
}
