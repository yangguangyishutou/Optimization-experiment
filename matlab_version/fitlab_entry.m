% 实验1驱动入口：负责串联完整流程，不在这里写具体算法细节。
% 流程顺序：
% 1) 读入数据
% 2) 配置超参数
% 3) 调用求解器拿到历史
% 4) 导出 csv / 图像 / 摘要

clear;
clc;
close all;

script_dir = fileparts(mfilename('fullpath'));
if isempty(script_dir)
    % 在命令行直接分段执行时，mfilename 可能为空，此时回退到当前路径。
    script_dir = pwd;
end

% 读入数据。
x = load(fullfile(script_dir, 'data_x.txt'));
y = load(fullfile(script_dir, 'data_y.txt'));

% 设置超参数。
learning_rate = 0.3;
max_iter = 50;
init_w = 0.5;
init_b = 0.5;

% 调用求解器。
[w, b, history] = fitlab_solver(x, y, learning_rate, max_iter, init_w, init_b);

% 导出结果。
fitlab_exports(script_dir, history);
fitlab_charts(script_dir, x, y, w, b, history);
fitlab_brief(script_dir, length(x), learning_rate, max_iter, init_w, init_b, w, b, history(end, 4));

% 命令行输出最终结果。
T = array2table(history, 'VariableNames', {'Iteration', 'w', 'b', 'Loss'});
disp('Final parameters and loss:');
disp(T(end, :));
disp('Saved files:');
disp('- iteration_first30.csv');
disp('- iteration_all50.csv');
disp('- fit_line_after_50.png');
disp('- loss_curve_50.png');
