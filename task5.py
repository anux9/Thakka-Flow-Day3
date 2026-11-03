message = input("Enter message: ").strip()

if not message.startswith("ZT:"):
    print("Not a message from planet Zeta")

else:
    # Remove ZT: prefix
    decoded = message[3:].strip()

    # Decode message
    decoded = decoded.replace("4", "a")
    decoded = decoded.replace("3", "e")
    decoded = decoded.replace("0", "o")
    decoded = decoded.replace("1", "i")

    # Classify message
    lower_message = decoded.lower()

    if "help" in lower_message:
        message_type = "DISTRESS"
    elif "hello" in lower_message:
        message_type = "GREETING"
    elif "?" in decoded:
        message_type = "QUESTION"
    else:
        message_type = "UNKNOWN"

    # Determine urgency
    exclamations = decoded.count("!")

    if exclamations >= 3:
        urgency = "HIGH"
    elif exclamations >= 1:
        urgency = "MEDIUM"
    else:
        urgency = "LOW"

    # Count characters without spaces
    letters = len(decoded.replace(" ", ""))

    # Encode reply
    reply = "we come in peace"
    reply = reply.replace("a", "4")
    reply = reply.replace("e", "3")
    reply = reply.replace("o", "0")
    reply = reply.replace("i", "1")

    # Display results
    print("Message:", message)
    print("Message:", decoded.upper())
    print("Letters (no spaces):", letters)
    print("Type:", message_type)
    print("Urgency:", urgency)
    print("Encoded reply: EA:", reply)

    # Thinking question:
# We check "help" before "hello" because the message may contain both.
# If "hello" is checked first, a distress message may be classified as GREETING.
# This is important because emergency messages must receive priority.