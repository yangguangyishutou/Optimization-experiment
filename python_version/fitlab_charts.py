"""拟合直线与 Loss 曲线作图并保存为 PNG。"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot_fit_line(base_dir: Path, x: np.ndarray, y: np.ndarray, w: float, b: float) -> None:
    # 在样本区间内均匀取点，得到平滑拟合直线。
    x_line = np.linspace(float(x.min()), float(x.max()), 200)
    y_line = w * x_line + b

    # 图1：散点 + 拟合线，直观看拟合效果。
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, s=25, label="Observed data")
    plt.plot(
        x_line,
        y_line,
        color="crimson",
        linewidth=2,
        label=f"Fit line: y = {w:.4f}x + {b:.4f}",
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Fit After 50 Iterations")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(base_dir / "fit_line_after_50.png", dpi=200)
    plt.close()


def plot_loss_curve(base_dir: Path, history: np.ndarray) -> None:
    # 图2：loss 随迭代变化，判断是否单调下降、是否已趋于平稳。
    plt.figure(figsize=(8, 5))
    plt.plot(history[:, 0], history[:, 3], marker="o", markersize=3, linewidth=1.5)
    plt.xlabel("Iteration")
    plt.ylabel("Loss (MSE)")
    plt.title("Loss Curve Over 50 Iterations")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(base_dir / "loss_curve_50.png", dpi=200)
    plt.close()
