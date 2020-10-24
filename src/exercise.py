def main():
    #write your code below this line

    # create the word list
    word_list = []

    input_string = "a"
    while input_string != "":
      input_string = input()
      word_list.append(input_string)

    print(word_list[2]) # third element

if __name__ == '__main__':
    main()
