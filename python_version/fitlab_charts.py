"""拟合直线与 Loss 曲线作图并保存为 PNG。"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot_fit_line(base_dir: Path, x: np.ndarray, y: np.ndarray, w: float, b: float) -> None:
    # 在样本区间内均匀取点，得到平滑拟合直线。
    x_line = np.linspace(float(x.min()), float(x.max()), 200)
    y_line = w * x_line + b
    obs_color = "#526F8A"
    fit_color = "#244969"
    grid_color = "#E3E7ED"

    # 图1：散点 + 拟合线，直观看拟合效果。
    fig, ax = plt.subplots(figsize=(8.8, 5.2), dpi=160)
    plt.scatter(
        x,
        y,
        s=26,
        color=obs_color,
        edgecolors="none",
        alpha=0.78,
        label="Observed data",
    )
    plt.plot(
        x_line,
        y_line,
        color=fit_color,
        linewidth=3.0,
        label=f"fitted line: y = {w:.4f}x + {b:.4f}",
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Linear Fit After 50 Iterations", fontweight="normal")
    ax.legend(frameon=False, loc="upper left")
    ax.grid(True, color=grid_color, linewidth=0.8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(direction="out", length=4)
    fig.tight_layout()
    fig.savefig(base_dir / "fit_line_after_50.png")
    plt.close(fig)


def plot_loss_curve(base_dir: Path, history: np.ndarray) -> None:
    # 图2：loss 随迭代变化，判断是否单调下降、是否已趋于平稳。
    loss_color = "#2A5C86"
    grid_color = "#E3E7ED"
    fig, ax = plt.subplots(figsize=(8.8, 5.2), dpi=160)
    x_axis = history[:, 0]
    loss = history[:, 3]
    ax.plot(
        x_axis,
        loss,
        linewidth=2.8,
        color=loss_color,
    )
    # 每隔 5 个点打一次标记，既能看步进感，又不会显得拥挤。
    ax.plot(
        x_axis[::5],
        loss[::5],
        "o",
        markersize=4.8,
        markerfacecolor="white",
        markeredgecolor=loss_color,
        markeredgewidth=1.0,
        linewidth=0,
    )
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Loss (MSE)")
    ax.set_title("Loss Curve Over 50 Iterations", fontweight="normal")
    ax.grid(True, color=grid_color, linewidth=0.8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(direction="out", length=4)
    fig.tight_layout()
    fig.savefig(base_dir / "loss_curve_50.png")
    plt.close(fig)
