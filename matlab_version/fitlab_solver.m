function [w, b, history] = fitlab_solver(x, y, learning_rate, max_iter, init_w, init_b)
%FITLAB_SOLVER 一元线性模型 y = w*x + b 的梯度下降（MSE）
%
%   history 每行: [iteration, w, b, loss]

% 从给定初值开始迭代。
w = init_w;
b = init_b;
n = length(x);
% 预分配历史矩阵，避免循环中动态扩容。
history = zeros(max_iter, 4);

for iter = 1:max_iter
    % 当前参数下的预测和残差。
    y_pred = w * x + b;
    err = y_pred - y;

    % 均方误差对参数的梯度：
    % dL/dw = (2/n) * sum((wx+b-y).*x)
    % dL/db = (2/n) * sum(wx+b-y)
    grad_w = (2 / n) * sum(err .* x);
    grad_b = (2 / n) * sum(err);

    % 梯度下降更新。
    w = w - learning_rate * grad_w;
    b = b - learning_rate * grad_b;

    % 用更新后的参数记录 loss，和常见训练日志一致。
    loss = mean((w * x + b - y).^2);
    history(iter, :) = [iter, w, b, loss];
end

end
