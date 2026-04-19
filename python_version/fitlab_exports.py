"""保存 CSV 与 summary 文本（与算法、作图分离）。"""

from pathlib import Path

import numpy as np


def save_iteration_csv(base_dir: Path, history: np.ndarray) -> None:
    # 统一小数位，避免不同平台/区域设置导致导出格式不一致。
    fmt = ["%.0f", "%.10f", "%.10f", "%.10f"]
    header = "Iteration,w,b,Loss"

    # 保存全量 50 次迭代，便于完整复盘参数变化过程。
    np.savetxt(
        base_dir / "iteration_all50.csv",
        history,
        delimiter=",",
        header=header,
        comments="",
        fmt=fmt,
    )

    # 另外单独保存前 30 次，和课程报告中的“前30步分析”对应。
    np.savetxt(
        base_dir / "iteration_first30.csv",
        history[:30],
        delimiter=",",
        header=header,
        comments="",
        fmt=fmt,
    )


def write_summary(
    base_dir: Path,
    n_points: int,
    learning_rate: float,
    max_iter: int,
    init_w: float,
    init_b: float,
    final_w: float,
    final_b: float,
    final_loss: float,
) -> None:
    # 文本摘要用于快速查看核心配置和最终收敛结果。
    lines = [
        "Linear fitting by gradient descent",
        f"Data points: {n_points}",
        f"Learning rate: {learning_rate}",
        f"Max iterations: {max_iter}",
        f"Initial w: {init_w}",
        f"Initial b: {init_b}",
        f"Final w: {final_w:.10f}",
        f"Final b: {final_b:.10f}",
        f"Final loss: {final_loss:.10f}",
        "",
        "Generated files:",
        "- iteration_first30.csv",
        "- iteration_all50.csv",
        "- fit_line_after_50.png",
        "- loss_curve_50.png",
    ]
    # 使用 utf-8，保证中文环境下打开不会乱码。
    (base_dir / "summary.txt").write_text("\n".join(lines), encoding="utf-8")
