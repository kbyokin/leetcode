sentence = "eetcode"
sentences = sentence.split(" ")
num_sen = len(sentences)
print(sentences)
if num_sen == 1:
    if sentences[0][0] != sentences[0][-1]:
        print(False)
for i in range(num_sen):
    if i == 0:
        # print(sentences[i], sentences[i-1])
        print(sentences[i][0], sentences[i-1][0])
        if sentences[i][0] != sentences[i-1][-1]:
            print(False)
            break
    elif i + 1 < num_sen:
        print(sentences[i], sentences[i+1])
        print(sentences[i][0], sentences[i+1][0])
        if sentences[i][-1] != sentences[i+1][0]:
            print(False)
            break
    else:
        print(True)
# for i, sentence in enumerate(sentences):
#     print(sentences[i][0], sentence[-1])
    # if sentences[i][0] != sentence[-1]:
    #     print(False)
