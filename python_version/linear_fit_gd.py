#!/usr/bin/env python3
"""Linear fitting assignment solved with gradient descent."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def gradient_descent(
    x: np.ndarray,
    y: np.ndarray,
    learning_rate: float,
    max_iter: int,
    init_w: float,
    init_b: float,
):
    """Run gradient descent and return final params plus iteration history."""
    w = float(init_w)
    b = float(init_b)
    n = x.size
    history = []

    for iteration in range(1, max_iter + 1):
        y_pred = w * x + b
        error = y_pred - y

        grad_w = (2.0 / n) * np.sum(error * x)
        grad_b = (2.0 / n) * np.sum(error)

        w -= learning_rate * grad_w
        b -= learning_rate * grad_b

        loss = np.mean((w * x + b - y) ** 2)
        history.append((iteration, w, b, loss))

    return w, b, np.array(history, dtype=float)


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    x_path = base_dir / "data_x.txt"
    y_path = base_dir / "data_y.txt"

    if not x_path.exists() or not y_path.exists():
        raise FileNotFoundError("Missing data_x.txt or data_y.txt in script folder.")

    x = np.loadtxt(x_path)
    y = np.loadtxt(y_path)

    learning_rate = 0.3
    max_iter = 50
    init_w = 0.5
    init_b = 0.5

    final_w, final_b, history = gradient_descent(
        x, y, learning_rate, max_iter, init_w, init_b
    )

    np.savetxt(
        base_dir / "iteration_all50.csv",
        history,
        delimiter=",",
        header="Iteration,w,b,Loss",
        comments="",
        fmt=["%.0f", "%.10f", "%.10f", "%.10f"],
    )
    np.savetxt(
        base_dir / "iteration_first30.csv",
        history[:30],
        delimiter=",",
        header="Iteration,w,b,Loss",
        comments="",
        fmt=["%.0f", "%.10f", "%.10f", "%.10f"],
    )

    x_line = np.linspace(x.min(), x.max(), 200)
    y_line = final_w * x_line + final_b

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, s=25, label="Observed data")
    plt.plot(
        x_line,
        y_line,
        color="crimson",
        linewidth=2,
        label=f"Fit line: y = {final_w:.4f}x + {final_b:.4f}",
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Fit After 50 Iterations")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(base_dir / "fit_line_after_50.png", dpi=200)
    plt.close()

    plt.figure(figsize=(8, 5))
    plt.plot(history[:, 0], history[:, 3], marker="o", markersize=3, linewidth=1.5)
    plt.xlabel("Iteration")
    plt.ylabel("Loss (MSE)")
    plt.title("Loss Curve Over 50 Iterations")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(base_dir / "loss_curve_50.png", dpi=200)
    plt.close()

    summary_lines = [
        "Linear fitting by gradient descent",
        f"Data points: {len(x)}",
        f"Learning rate: {learning_rate}",
        f"Max iterations: {max_iter}",
        f"Initial w: {init_w}",
        f"Initial b: {init_b}",
        f"Final w: {final_w:.10f}",
        f"Final b: {final_b:.10f}",
        f"Final loss: {history[-1, 3]:.10f}",
        "",
        "Generated files:",
        "- iteration_first30.csv",
        "- iteration_all50.csv",
        "- fit_line_after_50.png",
        "- loss_curve_50.png",
    ]
    (base_dir / "summary.txt").write_text("\n".join(summary_lines), encoding="utf-8")

    print(f"Final w = {final_w:.10f}")
    print(f"Final b = {final_b:.10f}")
    print(f"Final loss = {history[-1, 3]:.10f}")


if __name__ == "__main__":
    main()
