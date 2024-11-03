def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.
    """
    
    if (a > b and a < c) or (a < b and a > c):
        return a
# elif是else if的意思
    elif (b > a and b < c) or (b < a and b > c):
        return b
    else:
        return c



def sum_digits(y: int) -> int:
    """
    Sum all the digits of y.
    """ 
    str_y = str(y)  # 将整数转换为字符串
    total = 0  # 初始化总和为0
    
    for digit in str_y:  # 遍历字符串中的每一个字符
        total += int(digit)  # 将字符转换为整数并累加到总和中
    
    return total  # 返回总和



def double_eights(n: int) -> bool:
    """
    Return True if n has two eights in a row.
    """
    passstr_n = str(n)  # 将整数转换为字符串
    
    for i in range(len(str_n) - 1):  # 遍历字符串中的每一个字符，除了最后一个字符
        if str_n[i] == '8' and str_n[i + 1] == '8':  # 如果当前字符和下一个字符都是8
            return True  # 返回True
    
    return False  # 如果没有找到连续的两个8，返回False