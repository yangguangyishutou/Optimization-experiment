# Assignment Deliverables

Both Python and MATLAB solutions are included.

## Python Version
Path: `python_version`
- `fitlab_entry.py`: 驱动脚本（读数据、调参、调用各模块）
- `fitlab_solver.py`: 梯度下降核心
- `fitlab_exports.py`: 保存 CSV 与 summary
- `fitlab_charts.py`: 保存图像
- `data_x.txt`, `data_y.txt`: input data
- `iteration_first30.csv`: first 30 iterations (`w`, `b`, `Loss`)
- `iteration_all50.csv`: all 50 iterations
- `fit_line_after_50.png`: final fitted-line plot
- `loss_curve_50.png`: loss curve
- `summary.txt`: run summary
- `report.md`: report-ready content
- `requirements.txt`: Python dependencies

Run:
```bash
python python_version/fitlab_entry.py
```

## MATLAB Version
Path: `matlab_version`
- `fitlab_entry.m`: 驱动脚本
- `fitlab_solver.m`: 梯度下降核心
- `fitlab_exports.m` / `fitlab_charts.m` / `fitlab_brief.m`: 导出结果
- `data_x.txt`, `data_y.txt`: input data
- `iteration_first30.csv`: first 30 iterations (`w`, `b`, `Loss`)
- `iteration_all50.csv`: all 50 iterations
- `fit_line_after_50.png`: final fitted-line plot
- `loss_curve_50.png`: loss curve
- `summary.txt`: run summary
- `report.md`: report-ready content

Run in MATLAB:
```matlab
run('matlab_version/fitlab_entry.m')
```
