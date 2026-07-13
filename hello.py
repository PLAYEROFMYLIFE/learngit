# calculator.py - 解决冲突后的版本
def add(a, b):
    """计算两个数的和（含10%税费+四舍五入）"""
    result = round((a + b) * 1.1, 2)  # 融合两个分支的逻辑
    return result

# 测试代码
if __name__ == "__main__":
    print("计算结果（含税费+四舍五入）：", add(10, 20))  # 预期输出：33.0