def num_box(numbers):
    # Determine the maximum length of the numbers (converted to strings)
    max_length = max(len(str(num)) for num in numbers)
    box_width = max_length + 4

    # Top line of the box
    print('+' + '-' * (box_width - 2) + '+')

    # Numbers inside the box
    for num in numbers:
        print('| ' + str(num).center(box_width - 4) + ' |')

    # Bottom line of the box
    print('+' + '-' * (box_width - 2) + '+')

# whats in the box? what ever you want it to be :)
num_box(['Whats in the box?',134, 7, 45678, 69])