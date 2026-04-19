"""
实验1驱动入口。

这个文件只负责流程调度：
1) 读取数据
2) 设置超参数
3) 调用求解器
4) 导出表格、图像和文字摘要
"""

from pathlib import Path

import numpy as np

from fitlab_solver import solve_line_with_gd
from fitlab_charts import plot_fit_line, plot_loss_curve
from fitlab_exports import save_iteration_csv, write_summary


def main() -> None:
    # 统一使用脚本所在目录作为工作目录，避免从其他路径运行时找不到数据文件。
    base_dir = Path(__file__).resolve().parent
    x_path = base_dir / "data_x.txt"
    y_path = base_dir / "data_y.txt"

    # 提前做输入检查，报错信息明确一些，便于同学复现实验时定位问题。
    if not x_path.exists() or not y_path.exists():
        raise FileNotFoundError("Missing data_x.txt or data_y.txt in script folder.")

    # loadtxt 读取纯数字文本最直接，得到的是 1D 向量。
    x = np.loadtxt(x_path)
    y = np.loadtxt(y_path)

    # 下面三组参数和实验要求保持一致。
    learning_rate = 0.3
    max_iter = 50
    init_w = 0.5
    init_b = 0.5

    # 求解器只做一件事：按给定超参数完成迭代，并返回全量历史。
    final_w, final_b, history = solve_line_with_gd(
        x, y, learning_rate, max_iter, init_w, init_b
    )

    # 输出阶段拆分成独立函数，方便后续替换格式（例如改成 xlsx 或 json）。
    save_iteration_csv(base_dir, history)
    plot_fit_line(base_dir, x, y, final_w, final_b)
    plot_loss_curve(base_dir, history)
    write_summary(
        base_dir,
        len(x),
        learning_rate,
        max_iter,
        init_w,
        init_b,
        final_w,
        final_b,
        float(history[-1, 3]),
    )

    # 终端里打印核心结果，便于快速检查是否收敛到合理范围。
    print(f"Final w = {final_w:.10f}")
    print(f"Final b = {final_b:.10f}")
    print(f"Final loss = {history[-1, 3]:.10f}")


if __name__ == "__main__":
    main()
