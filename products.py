products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)

print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('price.csv', 'w', encoding='utf-8') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

