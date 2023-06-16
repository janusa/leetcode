def generate_fizz_buzz_list_v2(n):
    fizz_buzz_list = []
    fizz = 1
    buzz = 1
    for i in range(1, n + 1):
        if fizz * buzz == 15:
            fizz_buzz_list.append("FizzBuzz")
            fizz = 0
            buzz = 0
        elif fizz == 3:
            fizz_buzz_list.append("Fizz")
            fizz = 0
        elif buzz == 5:
            fizz_buzz_list.append("Buzz")
            buzz = 0
        else:
            fizz_buzz_list.append(str(i))
        fizz += 1
        buzz += 1
    return fizz_buzz_list


print(generate_fizz_buzz_list_v2(15))
