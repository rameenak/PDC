import asyncio
from random import randint

# Palindrome function
def reverse_and_check_palindrome(s):
    reversed_s = s[::-1]
    is_palindrome = s == reversed_s
    return reversed_s, is_palindrome

# New async state for palindrome checking
async def palindrome_state(strings):
    results = [reverse_and_check_palindrome(s) for s in strings]
    await asyncio.sleep(1)  # simulate async processing
    output = "\n".join(f"{s} → {rev} | Palindrome: {is_pal}" for s, (rev, is_pal) in zip(strings, results))
    print("\nPalindrome Check Results:\n" + output)
    return "Palindrome State completed"

# FSM states
async def start_state():
    print('Start State called\n')
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)

    print('Resume of the Transition: \nStart State calling ' + result)

async def state1(transition_value):
    output_value = f'State 1 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)

    return output_value + f'State 1 calling {result}'

async def state2(transition_value):
    output_value = f'State 2 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)

    return output_value + f'State 2 calling {result}'

async def state3(transition_value):
    output_value = f'State 3 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        # Instead of going directly to end_state, let's check palindromes first
        result = await palindrome_state(["madam", "apple", "racecar", "python", "level"])
        result = await end_state(input_value)  # then go to end_state

    return output_value + f'State 3 calling {result}'

async def end_state(transition_value):
    output_value = f'End State with transition value = {transition_value}\n'
    print('...stop computation...')
    return output_value

# Run the FSM
if __name__ == '__main__':
    print('Finite State Machine simulation with Asyncio Coroutine')
    asyncio.run(start_state())
