Customers = {110: {'name': 'Babak Rezae', 'Add': 'IndEngFUM'}, 111: {'name': 'Bahram Rostami', 'Add': 'SciFUM'}}
Goods = {11: {'name': 'Pen', 'cost': 1000}, 12: {'name': 'Paper', 'cost': 15000}, 13: {'name': 'cake', 'cost': 5000}}

L1 = [110, [11, 10], [12, 5], [11, 1], [13, 5], [12, 14]]

dash = '-'
blank = ' '


def print_factor(L1):
    goods_list = []
    goods_codes_list = []
    buying_goods_code = []
    buying_goods_quantity = []
    total_price = [0]

    n = len(L1) - 1  # int(input("Enter number of elements you want to order : "))
    for j in range(0, n):
        ele_code = L1[j + 1][0]
        ele_quan = L1[j + 1][1]
        buying_goods_code.append(ele_code)
        buying_goods_quantity.append(ele_quan)  # adding the element
        total_price[0] = total_price[0] + buying_goods_quantity[j] * Goods[buying_goods_code[j]]['cost']

    # print (buying_goods_code,buying_goods_quantity)
    print('customer name: ', Customers[L1[0]]['name'], ' ' * 9, 'customer address: ', Customers[L1[0]]['Add'])
    print(dash * 60)
    print('No. |', 'code   |', 'name     |', 'price  |', 'quantity |', 'cost')
    print(dash * 60)

    for i in range(0, len(buying_goods_code)):
        print(str(i + 1).ljust(6, ' '), str(buying_goods_code[i]).ljust(7, ' '),
              Goods[buying_goods_code[i]]['name'].ljust(10, ' '),
              str(Goods[buying_goods_code[i]]['cost']).ljust(10, ' '), str(buying_goods_quantity[i]).ljust(8, ' '),
              str(buying_goods_quantity[i] * Goods[buying_goods_code[i]]['cost']).ljust(8, ' '))
        print(dash * 60)
    print('total:', blank * 29, str(sum(buying_goods_quantity)).ljust(8, ' '), total_price[0])


print_factor(L1)

xla = input('press I to continue or Q to quit')
while xla == 'i':
    L2 = []
    L2 = input("enter new items: ")
    L2 = L2.split(',')
    b = 0

    while b < len(L2):
        L1.append([int(L2[b]), int(L2[b + 1])])
        b += 2
    print_factor(L1)
    xla = 0
    xla = input('press I to continue or Q to quit')
if xla == 'q':
    exit(print('see you soon!'))
else:
    print('wrong command key!')
