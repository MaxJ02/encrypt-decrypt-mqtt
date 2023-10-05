import paho.mqtt.client as mqtt

# Funktion för att dekryptera meddelanden med rot-n
def decrypt_message(encrypted_message, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    decrypted_message = ""
    for char in encrypted_message:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            char_idx = alphabet.index(char.lower())
            decrypted_char_idx = (char_idx - shift) % len(alphabet)
            decrypted_char = alphabet[decrypted_char_idx]
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message


def on_connect(client, userdata, flags, rc):
    client.subscribe(f"ela/superchat/#", qos=1)

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode("utf-8")
        topic = msg.topic
        shift = 13  # Antal tecken för förskjutning (samma som användes vid kryptering)

        # Dekryptera meddelandet
        decrypted_payload = decrypt_message(payload, shift)

        print(topic)
        print(f"Message: {decrypted_payload}")

    except UnicodeDecodeError:
        print("Failed to decode message as UTF-8")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", port=1883, keepalive=60)

client.loop_forever()
