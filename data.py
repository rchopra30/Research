
data = open("coreference_pro.txt", "r")
new_data = open("pronouns_rmv_data.txt", "w")


#bias = data.readline()
# print(bias)
# print(bias.find("["))
# print(bias.find("[", 3))
# print(bias[2:51])
# print(bias.replace("[", ''))
# print(bias.replace("]", ''))
for bias in data:
    first = bias.find("[")
    stop = bias.find("[", first + 1)
    bias = bias[:stop]
    remove = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']']
    for r in remove:
        bias = bias.replace(r, '')
    new_data.write(bias[1:] + '\n')

data.close()
