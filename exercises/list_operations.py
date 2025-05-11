"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    if operation == "add":
        for student in args:
            students.append(student)
        return students
    elif operation == "remove":
        for student in args:
            students.remove(student)
        return students
    elif operation == "update":
        old, new = args[0], args[1]
        for i, student in enumerate(students):
            if student == old:
                students[i] = new
        return students