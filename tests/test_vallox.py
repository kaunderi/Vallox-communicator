import unittest
import json
from unittest.mock import Mock, patch, PropertyMock
from Vallox_communicator import Vallox
import Serial_config


class TestVallox(unittest.TestCase):
    @patch("Vallox_communicator.mqtt.Client", autospec=True)
    @patch("Vallox_communicator.serial.Serial", autospec=True)
    def test_init(self, mock_serial, mock_mqtt):
        vallox = Vallox()

        self.assertEqual(vallox.topic, "vallox")
        self.assertEqual(vallox.serial, mock_serial.return_value)
        self.assertEqual(vallox.client, mock_mqtt.return_value)
        mock_mqtt.return_value.username_pw_set.assert_called_once_with(
            "your-mqtt-username", "your-mqtt-password"
        )
        mock_mqtt.return_value.connect.assert_called_once_with(
            "mqtt://your-mqtt-broker-url"
        )
        mock_mqtt.return_value.loop_start.assert_called_once()

    @patch("Vallox_communicator.mqtt.Client", autospec=True)
    @patch("Vallox_communicator.serial.Serial", autospec=True)
    def test_read_byte(self, mock_serial, mock_mqtt):
        mock_serial = Mock()
        mock_serial.read.return_value = b"test_data"
        vallox = Vallox()
        vallox.serial = mock_serial

        result = vallox.read_byte()

        self.assertEqual(result, b"test_data")

    @patch("Vallox_communicator.mqtt.Client", autospec=True)
    @patch("Vallox_communicator.serial.Serial", autospec=True)
    def test_process_measurement_publish(self, mock_serial, mock_mqtt):
        vallox = Vallox()
        vallox.counter = 25  # Set counter to 25 to trigger publishing

        mock_publish = Mock()
        vallox.client.publish = mock_publish

        vallox.process_measurement("test_identifier", "test_value")

        self.assertEqual(vallox.counter, 1)  # Counter should reset
        mock_publish.assert_called_once_with(
            "vallox", str(json.dumps(vallox.vallox_data))
        )

    @patch("Vallox_communicator.mqtt.Client", autospec=True)
    @patch("Vallox_communicator.serial.Serial", autospec=True)
    @patch("Vallox_communicator.Vallox.process_measurement")
    def test_process_sentence(
        self,
        mock_process_measurement,
        mock_serial,
        mock_mqtt,
    ):
        vallox = Vallox()

        sentence_start = Serial_config.SENTENCE_START
        sender = Serial_config.SENTENCE_SYSTEM
        recipient = b"\x21"
        valuetype = Serial_config.TYPE_TEMP_OUTSIDE
        value = b"\x00"[0]
        checksum = bytes(
            hex(sentence_start[0] + sender[0] + recipient[0] + valuetype + value),
            "utf-8",
        )

        test_sentence = [
            sentence_start,
            sender,
            recipient,
            valuetype,
            value,
            checksum,
        ]

        vallox.process_sentence(test_sentence)

        args = mock_process_measurement.call_args.args
        self.assertEqual(
            args,
            (
                Serial_config.TEMP_IDENTIFIERS[valuetype],
                Serial_config.TEMP_LOOKUP[value],
            ),
        )

    @patch("Vallox_communicator.mqtt.Client", autospec=True)
    @patch("Vallox_communicator.serial.Serial", autospec=True)
    @patch("Vallox_communicator.logging.info", autospec=True)
    def test_change_fan_speed(self, mock_logging_info, mock_serial, mock_mqtt):
        vallox = Vallox()

        vallox.change_fan_speed("3")

        expected_message = "Setting fanspeed to 3"
        mock_logging_info.assert_called_once_with(expected_message)

        expected_serial_write_calls = Serial_config.FANSPEED_SET["3"]
        self.assertEqual(
            mock_serial.return_value.write.call_args_list[0][0][0],
            expected_serial_write_calls,
        )

    @patch("Vallox_communicator.mqtt.Client")
    @patch("Vallox_communicator.serial.Serial")
    @patch("Vallox_communicator.Vallox.read_byte")
    @patch("Vallox_communicator.Vallox.process_sentence")
    def test_monitor_values_no_processing(
        self, mock_process_sentence, mock_read_byte, mock_mqtt, mock_serial
    ):
        vallox = Vallox()

        sentinel = PropertyMock(side_effect=[True, False])
        Vallox.RUNNING = sentinel
        mock_read_byte.return_value = bytes(1)
        vallox.monitor_values()

        self.assertFalse(mock_process_sentence.called)

    @patch("Vallox_communicator.mqtt.Client")
    @patch("Vallox_communicator.serial.Serial")
    @patch("Vallox_communicator.Vallox.read_byte")
    @patch("Vallox_communicator.Vallox.process_sentence")
    def test_monitor_values_processed(
        self, mock_process_sentence, mock_read_byte, mock_mqtt, mock_serial
    ):
        vallox = Vallox()

        sentinel = PropertyMock(side_effect=[True, False])
        Vallox.RUNNING = sentinel
        mock_read_byte.return_value = bytes(6)
        vallox.monitor_values()

        self.assertTrue(mock_process_sentence.called)


if __name__ == "__main__":
    unittest.main()
