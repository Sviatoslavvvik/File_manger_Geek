from random import randint
def game():
    answer = randint(0,100)
    count = 0
    check = None
    levels = {1: 10, 2: 5, 3:3}
    print ('Игра угадай число'
           ' Ваша задача угадать число в диапазоне от 1 до 100 за ограниченное количество попыток')
    max_count = levels [int ( input ('введите уровень сложности: 1 ( 10 попыток), 2 (5 попыток) или 3 (3 попытки) '))]
    user_count = int (input ('введите количество пользователей '))
    users = []
    for i in range (user_count):
        user_name = input(f'введите имя пользователя {i+1}')
        users.append(user_name)
    print(users)

    is_winner = False
    winner_name = None
    while not is_winner:
        count += 1
        if count > max_count:
            print ('you are looser')
            break
        print (f'Попытка №  {count} ')
        for user in users:
            print (f'Ход пользователя {user}')
            check = int (input ('введите число '))
            if check == answer:
                winner_name = user;
                is_winner = True
                break

            elif check < answer:
                    print('введите число больше ')
            else:
                print ('введите число меньше ')
    else:
        print (f'{winner_name} поздравляю вы угадали')