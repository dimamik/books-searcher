import logging

from main import *

recom = Recommender(documents_n=25000, persons_n=4000)

with open('out.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        temp = line
        line = line.split(',')
        if (len(line) != 3):
            line = [line[0], ''.join(line[1:len(line) - 1]), line[len(line) - 1]]
        try:
            line[2] = line[2].split('=')[1]
            line[2] = "".join(filter(str.isdigit, line[2]))
            # print(line[2],line[0])
            recom.record(line[1], line[0])
        except:
            logging.error("Exception!! " + temp)
