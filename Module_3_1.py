def count_calls():
    global calls
    calls += 1


def string_info(str_):
    count_calls()
    str_info = (len(str_), str_.upper(),str_.lower())
    return str_info

def is_contains(str_, list_):
    count_calls()
    is_cont = True
    if str_.lower() in list(map(str.lower,list_)):
        return True
    else:
        return False

calls = 0
print(string_info('hello, world'))
print(string_info('hohoho'))
print(is_contains('ho',['hO','hA','hE']))

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print('------')
print(calls)
