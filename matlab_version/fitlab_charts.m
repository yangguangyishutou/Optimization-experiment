function fitlab_charts(script_dir, x, y, w, b, history)
%FITLAB_CHARTS 保存拟合直线图与 Loss 曲线图

% 图1：样本散点 + 最终拟合直线。
fig1 = figure('Color', 'w');
scatter(x, y, 25, 'filled');
hold on;
% 在样本区间生成更密集的 x，用来画平滑直线。
x_line = linspace(min(x), max(x), 200)';
y_line = w * x_line + b;
plot(x_line, y_line, 'r-', 'LineWidth', 2);
xlabel('x');
ylabel('y');
title('Linear Fit After 50 Iterations');
legend('Observed data', sprintf('Fit line: y = %.4fx + %.4f', w, b), 'Location', 'northwest');
grid on;
saveas(fig1, fullfile(script_dir, 'fit_line_after_50.png'));
close(fig1);

% 图2：loss 收敛曲线，观察优化过程是否稳定下降。
fig2 = figure('Color', 'w');
plot(history(:, 1), history(:, 4), '-o', 'LineWidth', 1.5, 'MarkerSize', 4);
xlabel('Iteration');
ylabel('Loss (MSE)');
title('Loss Curve Over 50 Iterations');
grid on;
saveas(fig2, fullfile(script_dir, 'loss_curve_50.png'));
close(fig2);

end
