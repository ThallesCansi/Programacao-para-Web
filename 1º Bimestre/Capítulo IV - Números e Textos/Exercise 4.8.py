while True:
    string = input('Write a sentence with 5 words: ').split(' ')
    if (len(string) == 4):
        print('Please, write a sentence with only 5 words.')
    else:
        for i in string:
            print(i)
