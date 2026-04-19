% Linear fitting assignment solved with gradient descent.
clear;
clc;
close all;

script_dir = fileparts(mfilename('fullpath'));
if isempty(script_dir)
    script_dir = pwd;
end

x = load(fullfile(script_dir, 'data_x.txt'));
y = load(fullfile(script_dir, 'data_y.txt'));

learning_rate = 0.3;
max_iter = 50;
w = 0.5;
b = 0.5;
n = length(x);

% history columns: [iteration, w, b, loss]
history = zeros(max_iter, 4);

for iter = 1:max_iter
    y_pred = w * x + b;
    err = y_pred - y;

    grad_w = (2 / n) * sum(err .* x);
    grad_b = (2 / n) * sum(err);

    w = w - learning_rate * grad_w;
    b = b - learning_rate * grad_b;

    loss = mean((w * x + b - y).^2);
    history(iter, :) = [iter, w, b, loss];
end

T = array2table(history, 'VariableNames', {'Iteration', 'w', 'b', 'Loss'});
writetable(T, fullfile(script_dir, 'iteration_all50.csv'));
writetable(T(1:30, :), fullfile(script_dir, 'iteration_first30.csv'));

fig1 = figure('Color', 'w');
scatter(x, y, 25, 'filled');
hold on;
x_line = linspace(min(x), max(x), 200)';
y_line = w * x_line + b;
plot(x_line, y_line, 'r-', 'LineWidth', 2);
xlabel('x');
ylabel('y');
title('Linear Fit After 50 Iterations');
legend('Observed data', sprintf('Fit line: y = %.4fx + %.4f', w, b), 'Location', 'northwest');
grid on;
saveas(fig1, fullfile(script_dir, 'fit_line_after_50.png'));

fig2 = figure('Color', 'w');
plot(history(:, 1), history(:, 4), '-o', 'LineWidth', 1.5, 'MarkerSize', 4);
xlabel('Iteration');
ylabel('Loss (MSE)');
title('Loss Curve Over 50 Iterations');
grid on;
saveas(fig2, fullfile(script_dir, 'loss_curve_50.png'));

fid = fopen(fullfile(script_dir, 'summary.txt'), 'w');
fprintf(fid, 'Linear fitting by gradient descent\n');
fprintf(fid, 'Data points: %d\n', n);
fprintf(fid, 'Learning rate: %.1f\n', learning_rate);
fprintf(fid, 'Max iterations: %d\n', max_iter);
fprintf(fid, 'Initial w: %.1f\n', 0.5);
fprintf(fid, 'Initial b: %.1f\n', 0.5);
fprintf(fid, 'Final w: %.10f\n', w);
fprintf(fid, 'Final b: %.10f\n', b);
fprintf(fid, 'Final loss: %.10f\n', history(end, 4));
fclose(fid);

disp('Final parameters and loss:');
disp(T(end, :));
disp('Saved files:');
disp('- iteration_first30.csv');
disp('- iteration_all50.csv');
disp('- fit_line_after_50.png');
disp('- loss_curve_50.png');
