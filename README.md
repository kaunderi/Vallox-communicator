# Vallox-communicator

Vallox-communicator is a library to monitor and control Vallox ventilation unit with RS485 serial connection. MQTT is used to publish/receive information to/from Home Assistant with MQTT integration.

Built on top of https://github.com/au-ee/read_vallox

## Supported features
- Monitor default sensor values (No humidity/CO2)
    - Inside-, outside-, exhaust- and intake temperature
    - Fanspeed
- Control the fanspeed
### TODO
- Monitor all possible values
- Control all possible things

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install needed packages

```bash
pip install -r requirements.txt
```

## Usage

Change correct serial device to Serial_config.py
```python
SERIAL_PORT = "/dev/ttyS0"
```

Input correct MQTT broker setting to MQTT_config.py
```python
ip_address = "IP_ADDRESS_OF_BROKER"
topic = "homeassistant/sensor/vallox"
username = "MQTT_USERNAME"
password = "MQTT_PASSWORD"
```
## Home Assistant control
Example on how to send command to the communicator from Home Assistant
```yaml
input_select:
  valloxfanspeed:
    name: Ventilation Fan Speed
    options:
      - "1"
      - "2"
      - "3"
      - "4"
      - "5"
      - "6"
      - "7"
      - "8"
    initial: "2"
    icon: mdi:tune

automation:
  - alias: "Change Ventilation Fan Speed"
    trigger:
      platform: state
      entity_id: input_select.valloxfanspeed
    action:
      - call-service
      - service: mqtt.publish
      - data:
          payload_template: "{{ states.input_select.valloxfanspeed }}"
          topic: homeassistant/sensor/vallox/control
```

Simple card for Lovelace UI
```yaml
type: entities
entities:
  - input_select.valloxfanspeed
```