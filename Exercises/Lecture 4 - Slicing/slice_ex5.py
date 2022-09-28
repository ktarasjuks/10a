if __name__ == '__main__':
    my_string = 't1234h1234i1234saaaaiaaaasbbbbm1234yaaaapbbbbabbbbsaaaas1234'
    corrected_string = my_string.replace('1234', '')
    corrected_string = corrected_string.replace('aaaa', '')
    corrected_string = corrected_string.replace('bbbb', '')
    print(corrected_string)
