# MQTT Chat Client with Rot-n Encryption

This is a simple chat client project designed to communicate over a public MQTT topic while also encrypting messages using a variant of the ROT-n (Caesar cipher) encryption method. The purpose of this project is to demonstrate a basic chat application that ensures message privacy by shifting characters by a specified number of positions before sending.

## Getting Started

To use this chat client, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies if necessary.

## Usage

1. Start the chat client.
2. Specify the number of character positions to shift messages (0-28). This will be the encryption key.
3. Choose a username when prompted.
4. Start sending and receiving encrypted messages.

## ROT-n Encryption

In this project, we use a variant of the ROT-n encryption method where 'n' is the number of character positions to shift. This variant also includes support for Swedish characters. Below is the ROT-3 encryption mapping:

abcdefghijklmnopqrstuvwxyzåäö

åäöabcdefghijklmnopqrstuvwxyz

For example, the word "hej" is encoded as "ebg". All other characters, including special characters, numbers, and letters from other alphabets, remain unchanged.

## MQTT Configuration

Messages are published using MQTT as plain text to the topic `ela/superchat/<fromuser>`, where `<fromuser>` is the chosen username. You should use the public MQTT broker at [https://broker.hivemq.com](https://broker.hivemq.com) for communication. Keep in mind that all groups will be using the same broker.

## Decrypting Messages

Messages received by the client are automatically decrypted using the specified ROT-n key. Messages sent with a different ROT-n key will appear as garbage text. You can achieve this by creating separate send and receive programs or by integrating both functionalities into a single program.

## Testing

Make sure to test the program by chatting with others in your group to ensure that the decryption process works as expected. Try using the program simultaneously with another group to see if their messages appear as garbage text.

## Extra Task

If you have extra time, consider creating a decoder for ROT-n. This would involve creating a program that takes an encoded text string and tries all 28 ROT-n variations to decode messages sent by others without knowing the specific ROT-n key used.

Enjoy your secure and private chat experience with ROT-n encryption!

