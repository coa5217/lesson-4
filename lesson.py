while True:
    piglatin = ""
    for word in input().split():
        for i in range(len(word)):
            if word[i] in "aeiouy":
                break
        if i == 0:
            piglatin += word + "yay" + " "
        else:
            piglatin += word[i:] + word[:i] + "ay" + " "
    print(piglatin[:-1])
            piglatin += word[i:] + word[:i] + "ay" + " "
