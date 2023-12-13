#!/usr/bin/python3

import serial
import Serial_config
import paho.mqtt.client as mqtt
import json
import threading
import logging

# Configuration Module (vallox_config.py)
from vallox_config import MQTT_USERNAME, MQTT_PASSWORD, MQTT_BROKER, MQTT_TOPIC, SERIAL_PORT, BAUD_RATE


class Vallox:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        self.client.connect(MQTT_BROKER)
        self.client.loop_start()
        self.topic = MQTT_TOPIC

        self.serial = serial.Serial(port=SERIAL_PORT, baudrate=BAUD_RATE)

        self.vallox_data = {}
        self.counter = 0

    RUNNING = True

    def read_byte(self):
        return self.serial.read()

    def process_measurement(self, identifier, value):
        self.vallox_data.update({identifier: value})
        # Publish for only every 25th measurement
        # TODO publish when every value is updated
        if self.counter == 25:
            logging.info(f"Publishing {self.vallox_data} to {self.topic}")
            self.client.publish(self.topic, str(json.dumps(self.vallox_data)))
            self.counter = 0
        self.counter += 1

    def process_sentence(self, sentence):
        sender = sentence[1]
        recipient = sentence[2]
        valuetype = sentence[3]
        value = sentence[4]
        checksum = sentence[5]

        if sender in Serial_config.SENTENCE_SYSTEM:
            # Only process sentences originating from controller
            if valuetype in Serial_config.TEMP_IDENTIFIERS:
                self.process_measurement(
                    Serial_config.TEMP_IDENTIFIERS[valuetype],
                    Serial_config.TEMP_LOOKUP[value],
                )
            elif valuetype == Serial_config.TYPE_FANSPEED:
                self.process_measurement(
                    "FANSPEED", Serial_config.FANSPEED_LOOKUP[value]
                )

    def monitor_values(self):
        logging.info("Starting monitoring Vallox readings!!")
        sentence = bytearray()
        while self.RUNNING:
            sentence += self.read_byte()
            length = len(sentence)
            if (length == 1 and (sentence[-1] not in Serial_config.SENTENCE_START)) or (
                (length == 2 or length == 3)
                and sentence[-1] not in Serial_config.SENTENCE_VALID_PEERS
            ):
                # TODO: Handle bytes. Eventually valid values are there with an offset, do not just throw them away
                sentence = bytearray()
            elif length >= 6:
                # sentence valid: correct start byte, syntactically correct sender and recipient
                self.process_sentence(sentence)
                sentence = bytearray()

    def on_message(self, client, userdata, message):
        self.change_fan_speed(str(message.payload.decode("utf-8")))

    def subscribe(self):
        logging.info(f"Started subscribing topic {self.topic}/control")
        self.client.on_message = self.on_message
        self.client.subscribe(f"{self.topic}/control")

    def change_fan_speed(self, value):
        logging.info(f"Setting fanspeed to {value}")
        self.serial.write(Serial_config.FANSPEED_SET[value])


if __name__ == "__main__":
    vallox = Vallox()
    vallox.subscribe()
    monitor = threading.Thread(target=vallox.monitor_values)
    monitor.start()
