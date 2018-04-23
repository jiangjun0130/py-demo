__author__ = 'jiangjun'
__date__ = '2018/4/11 下午11:31'


product_list = [
    ('iPhone', 5800),
    ('Mac Pro', 9800),
    ('Watch', 3800)
]

shopping_list = []

salalry = input('Input your salary:')

if salalry.isdigit():
    salalry = int(salalry)
    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input('请选择商品：')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice <= len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salalry:
                    shopping_list.append(p_item)
                    salalry -= p_item[1]
                    print('Added %s into shopping cart, your cuttent balance is \033[31;1m%s\033[0m' % (p_item, salalry))
                else:
                    print('你的余额只剩\033[41;1m%s\033[0m啦，还买个毛线啊' % salalry)
            else:
                print('商品不存在')
        elif user_choice == 'q':
            for p in shopping_list:
                print(p)
            print('Your current balance is ', salalry)
            exit()
        else:
            print('invalid option')