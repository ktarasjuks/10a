if __name__ == '__main__':
    my_list = ('is', 'name', 'my')
    out = '{2} {1} {0}'.format(my_list[0], my_list[1], my_list[2])
    out = out.capitalize()
    print('{} {}'.format(out, 'Konstantins'))
