"""一元线性模型 y = w*x + b 的梯度下降核心迭代。"""

import numpy as np


def solve_line_with_gd(
    x: np.ndarray,
    y: np.ndarray,
    learning_rate: float,
    max_iter: int,
    init_w: float,
    init_b: float,
):
    """
    对 MSE 损失做梯度下降，返回最终参数与迭代历史。

    history 每行: [iteration, w, b, loss]
    """
    # 参数转成 float，避免后续因为输入类型混杂触发隐式类型问题。
    w = float(init_w)
    b = float(init_b)
    n = int(x.size)
    # 预分配历史数组比循环里 append 更稳定，后处理也更方便。
    history = np.zeros((max_iter, 4), dtype=float)

    for iteration in range(1, max_iter + 1):
        # 当前参数下的预测值与残差。
        y_pred = w * x + b
        error = y_pred - y

        # MSE 对 w、b 的梯度：
        # dL/dw = (2/n) * sum((wx+b-y)*x)
        # dL/db = (2/n) * sum(wx+b-y)
        grad_w = (2.0 / n) * float(np.sum(error * x))
        grad_b = (2.0 / n) * float(np.sum(error))

        # 沿负梯度方向更新参数。
        w -= learning_rate * grad_w
        b -= learning_rate * grad_b

        # 用更新后的参数重新计算一次损失，和常见训练日志对齐。
        loss = float(np.mean((w * x + b - y) ** 2))
        history[iteration - 1, :] = [iteration, w, b, loss]

    return w, b, history
