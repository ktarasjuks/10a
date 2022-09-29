def forward():
    print('You go forward')


def left():
    pass


def right():
    pass


def fight(somenumber):
    hp = 100
    return hp - somenumber
    # hp = hp - somenumber
    # print('Your current hp is {} '.format(hp))
    # return hp


def game_over(your_name):
    print('Game over {}'.format(your_name))


if __name__ == '__main__':
    forward()
    left()
    right()
    current_hp = fight(50)
    print('Your current hp is {}'.format(current_hp))
    game_over('name')
