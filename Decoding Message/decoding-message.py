def create_staircase(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets

def decode(message_file):
    # Read the content of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Create a dictionary of numbers and words
    num_word_dict = {}
    for line in lines:
        num, word = line.split()
        num_word_dict[int(num)] = word

    # Create a list of numbers in ascending order
    nums = sorted(list(num_word_dict.keys()))

    # Create the staircase
    staircase = create_staircase(nums)

    if not staircase:
        return "Invalid input file format"

    # Extract the words corresponding to the staircase numbers
    # decoded_words = [words_and_numbers[line[-1] - 1][1] for line in staircase]
    decoded_words = [num_word_dict[line[-1]] for line in staircase]

    # Join the words to form the decoded message
    decoded_message = ' '.join(decoded_words)

    return decoded_message

# verifying if python is running or is running as a module
if (__name__ == "__main__"):
    # Replace with the actual file name
    message_file = "example.txt"
    decoded_message = decode(message_file)
    print(decoded_message)
