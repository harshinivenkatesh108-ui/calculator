def calculator():
    print('To start the calculator, enter a number, no decimals.')
    user_input = input()
    final_output = 0
    print('Enter one of the following operations: addition, subtraction, multiplication, division')
    operation = input()
    assert operation == 'addition' or operation == 'subtraction' or operation == 'multiplication' or operation == 'division', 'Please enter valid operation'
    print('Enter another number, no decimals')
    num_b = input()
    if operation == 'addition':
        final_output+= (int(user_input)+int(num_b))
    if operation == 'subtraction':
        final_output+= (int(user_input)-int(num_b))
    if operation == 'multiplication':
        final_output+= (int(user_input)*int(num_b))
    if operation == 'division':
        final_output+= (int(user_input)/int(num_b))
    print(final_output)


    

