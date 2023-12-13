# Vallox Configuration

# MQTT Configuration
MQTT_BROKER = "mqtt://your-mqtt-broker-url"  # Replace with your MQTT broker URL
MQTT_TOPIC = "homeassistant/sensor/vallox"  # Replace with your MQTT topic
MQTT_USERNAME = "your-mqtt-username"  # Replace with your MQTT username
MQTT_PASSWORD = "your-mqtt-password"  # Replace with your MQTT password

# Serial Port Configuration
SERIAL_PORT = (
    "/dev/ttyS0"  # Replace with the serial port your Vallox device is connected to
)
BAUD_RATE = 9600