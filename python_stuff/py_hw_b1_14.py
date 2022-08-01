flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
         "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
         "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}

# выше были данные, а после этой строчки
# вам надо дописать код.
def get_general_mean_values(flowers:dict):
    mean = {}
    for flower_item in flowers.items():
        for parametr, keys in flower_item[1].items():
            # print(flower_item[0], parametr, sum(keys)/len(keys))
            mean[flower_item[0]+ ' ' + parametr] = (sum(keys)/len(keys))
            # print('*'*100)
    return(mean)

def get_mean_values(mean:dict):
    sepal_length = []
    sepal_width = []
    petal_length = []
    for item, key in mean.items():
        if 'sepal_length' in item:
            sepal_length.append(round(key, 1))
        elif 'sepal_width' in item:
            sepal_width.append(round(key, 1))
        elif 'petal_length' in item:
            petal_length.append(round(key, 1))
        # print(item, key)
        # print(sepal_length, sepal_width, petal_length)
    return (sepal_length, sepal_width, petal_length)


sepal_length = (get_mean_values(get_general_mean_values(flowers))[0])
sepal_width = (get_mean_values(get_general_mean_values(flowers))[1])
petal_length = (get_mean_values(get_general_mean_values(flowers))[2])


print('sepal_length = ',sepal_length)
print('sepal_width = ',sepal_width)
print('petal_length = ',petal_length)


print(sum(petal_length)/len(petal_length))

# общее среднее значение для sepal_length:
# print('mean_sepal_length = %s' % (get_mean_values(get_general_mean_values(flowers))[0]))
# общее среднее значение для sepal_width:
# print('mean_sepal_width = %s' % (mean_sepal_width))
# общее среднее значение для petal_length:
# print('mean_petal_length = %s' % (mean_petal_length))
