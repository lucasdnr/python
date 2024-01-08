def decode(message_file):
    # Read the content of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extract numbers and words from each line
    pyramid = [line.strip().split()[1] for line in lines]

    # Create a dictionary to store the words with their corresponding numbers
    words_dict = {}
    current_number = 1

    for word in pyramid:
        words_dict[current_number] = word
        current_number += 1

    # Get the decoded message by joining the words in the correct order
    decoded_message = ' '.join(words_dict.values())

    return decoded_message


# verifying if python is running or is running as a module
if (__name__ == "__main__"):
    message_file = "example.txt"  # Replace with the actual file name
    decoded_message = decode(message_file)
    print(decoded_message)
