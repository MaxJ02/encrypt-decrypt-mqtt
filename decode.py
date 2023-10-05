import paho.mqtt.client as mqtt

def decode_message(coded_message, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    decoded_message = ""
    for char in coded_message:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            char_idx = alphabet.index(char.lower())
            decoded_char_idx = (char_idx - shift) % len(alphabet)
            decoded_char = alphabet[decoded_char_idx]
            if is_upper:
                decoded_char = decoded_char.upper()
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message


def on_connect(client, userdata, flags, rc):
    client.subscribe(f"ela/superchat/#", qos=1)

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode("utf-8")
        topic = msg.topic

        for shift in range(29):
            decoded_payload = decode_message(payload, shift)
            print(f"{topic} (shift={shift}): {decoded_payload}")

    except UnicodeDecodeError:
        print("Failed to decode message as UTF-8")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", port=1883, keepalive=60)

client.loop_forever()
