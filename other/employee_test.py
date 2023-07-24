# 从具体的场景中抽象出对应的数据结构
# 定义问题：
# 一个员工：员工唯一的ID、重要度、直属下属id
# 举例：第一个员工，id为1，重要度15，有一个下属，下属id是2
# 举例：第二个员工，id为2，重要度10，有一个下属，下属id是3
# 举例：第三个员工，id为3，重要度5，无下属
# 求解：输入一个公司的所有员工信息，以及一个员工id，求这个员工以及其下属的重要度之和

# 思路：将问题抽象为多叉树，通过前序遍历和后序遍历来解决
class Employee:
    def __init__(self, id: int, importance: int):
        self.id = id
        self.importance = importance
        self.subordinate = []


class EmployeeStatistics:
    def __init__(self, all_employee: list[Employee]):
        # 初始化总的重要度以及要处理的所有员工列表
        self.sum_importance = 0
        self.all_employees = all_employee

    def find_employee_by_id(self, id_to_find: int):
        for e in self.all_employees:
            if e.id == id_to_find:
                return e

    def find_all_importance_by_id_pre(self, id_to_find: int):
        employee = self.find_employee_by_id(id_to_find)
        self.find_all_importance_by_employee_pre(employee)

    def find_all_importance_by_id_post(self, id_to_find: int):
        employee = self.find_employee_by_id(id_to_find)
        return self.find_all_importance_by_employee_post(employee)

    # 前序遍历
    def find_all_importance_by_employee_pre(self, employee: Employee):
        if employee is None:
            return
        self.sum_importance += employee.importance
        for e in employee.subordinate:
            self.find_all_importance_by_employee_pre(e)

    # 后序遍历
    def find_all_importance_by_employee_post(self, employee: Employee):
        if employee is None:
            return 0
        total = 0
        for e in employee.subordinate:
            total += self.find_all_importance_by_employee_post(e)
        return total + employee.importance


if __name__ == '__main__':
    empolyee_1 = Employee(1, 5)
    empolyee_2 = Employee(2, 3)
    empolyee_3 = Employee(3, 3)
    empolyee_4 = Employee(4, 2)
    empolyee_5 = Employee(5, 1)
    empolyee_6 = Employee(6, 1)
    empolyee_1.subordinate = [empolyee_2, empolyee_3, empolyee_4]
    empolyee_2.subordinate = [empolyee_5, empolyee_6]

    all_employee = [empolyee_1, empolyee_2, empolyee_3, empolyee_4, empolyee_5, empolyee_6]

    es = EmployeeStatistics(all_employee)
    es.find_all_importance_by_id_pre(1)
    print(es.sum_importance)

    result = es.find_all_importance_by_id_post(1)
    print(result)
