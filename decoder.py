def decode_message(message):
    if not message or len(message) == 1:
        return 1
    count = 0
    if message[0] != '0':
     count += decode_message(message[1:])
    if message[0:2] <= '26':
      count += decode_message(message[2:])
    return count

print(decode_message('128'))


