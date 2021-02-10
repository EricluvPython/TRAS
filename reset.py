import os


def reset(path_data):
    path = os.getcwd() + '/' + path_data
    for i in os.listdir(path):
        file = path + "/" + i
        if os.path.isfile(file) == True:
            os.remove(file)


reset('record')
reset('results')
