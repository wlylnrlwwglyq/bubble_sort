import random


def bubble_sort(datas,reverse=False):
	for i in range(len(datas)-1):
		for j in range(len(datas)-i-1):
			if (reverse and datas[j] < datas[j+1]) or (not reverse and datas[j] > datas[j+1]):
					tmp = datas[j]
					datas[j] = datas[j+1]
					datas[j+1] = tmp


if __name__ == "__main__":
	data_length = int(input("データ数を入力> "))
	reverse = int(input("昇順:0 降順:1 >")) == 1
	datas = [ random.random() for i in range(data_length) ]
	bubble_sort(datas,reverse)
	for i in datas:
		print(i)

