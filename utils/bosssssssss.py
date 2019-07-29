class Boss:
    def __init__(self, finance, product):
        self.finance = finance
        self.product = product
        self.emp_list = []

    def hire(self, people):
        self.emp_list.append(people)

    def sell_product(self):
        self.finance += self.product * 10
        self.product = 0


class Employee:
    def __init__(self, exp):
        self.exp = exp
        self.salary = 0

    def work_per_year(self, boss):
        boss.product += self.exp * 12
        self.salary += 2000 * 12
        boss.finance -= 2000 * 12
        if self.exp < 500:
            self.exp += 50


if __name__ == '__main__':
    GuoHong = Boss(10000, 0)
    for _ in range(1, 11):
        print(f"第{_}年".center(18, "*"))
        Julei1 = Employee(300)
        GuoHong.hire(Julei1)
        for people in GuoHong.emp_list:
            people.work_per_year(GuoHong)
            # print(f"员工工资为：{people.salary}")
        GuoHong.sell_product()
        print(f"第{_}年结余：{GuoHong.finance}")

    print(GuoHong.finance)
