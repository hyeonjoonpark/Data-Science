import csv
import matplotlib.pyplot as plt
f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')

header = next(data)

print(data)

# 최고기온 구하기
max_temp = -999
max_date = ''

result = []
high =[]
low = []
month = [[], [], [], [], [], [], [], [], [], [], [], []]
