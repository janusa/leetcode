def generate_fizz_buzz_list_v3(n):
    fizz_buzz_list = []
    for i in range(1, n + 1):
        fizz_buzz_list.append(fizz_buzz(i))
    return fizz_buzz_list


def fizz_buzz(i):
    if i % 15 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return str(i)


print(generate_fizz_buzz_list_v3(15))
