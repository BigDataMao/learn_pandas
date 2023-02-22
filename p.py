# coding=utf8
import inspect


def p(*args, **kwargs):
    # 获取调用堆栈中的信息
    frame = inspect.currentframe().f_back
    filename = frame.f_code.co_filename
    lineno = frame.f_lineno

    # 读取文件内容并找到最近的注释
    with open(filename, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(lineno - 1, -1, -1):
            line = lines[i].strip()
            if line.startswith("#"):
                comment = line[1:].strip()
                print(f"{lineno}: {comment}")
                break

    # 输出原始的 print() 函数内容
    print(*args, **kwargs)
