import paho.mqtt.client as mqtt


# Funktion för att kryptera meddelanden med rot-n
def encrypt(message, n):
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    encrypted_message = ''
    
    for char in message:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            char_idx = alphabet.index(char.lower())
            encrypted_char_idx = (char_idx + shift) % len(alphabet)
            encrypted_char = alphabet[encrypted_char_idx]
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

# Anslut till MQTT-brokern
client = mqtt.Client()
client.connect("broker.hivemq.com", port=1883, keepalive=60)

# Starta MQTT-loopen
client.loop_start()

# Läs in användarnamn från användaren
username = input("Ange användarnamn: ")
# Läs in förskjutning från användaren
shift = int(input("Ange en krypterings-förskjutning mellan 0 - 28: "))

try:
    while True:
        # Läs in text från användaren
        message = input("Ange meddelande (eller tryck Enter för att avsluta): ")
        
        # Avsluta om användaren inte skriver något
        if not message:
            break
        
        # Skicka meddelandet till MQTT-brokern på angiven topic

        encrypted_message = encrypt(message, shift)
        client.publish(f"ela/superchat/{username}", payload=encrypted_message, qos=1)
except KeyboardInterrupt:
    pass

# Stoppa MQTT-loopen och koppla från
client.loop_stop()
client.disconnect()

#client.publish("ela/superchat", payload=message_with_username, qos=1)