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

% 数据文件与脚本放在同一目录，路径写法更稳，不依赖 MATLAB 当前工作目录。
x = load(fullfile(script_dir, 'data_x.txt'));
y = load(fullfile(script_dir, 'data_y.txt'));

% 实验参数。
learning_rate = 0.3;
max_iter = 50;
init_w = 0.5;
init_b = 0.5;

% 核心迭代放在独立函数里，入口脚本只负责调用。
[w, b, history] = fitlab_solver(x, y, learning_rate, max_iter, init_w, init_b);

% 导出环节拆开，后续要改输出格式时改动更局部。
fitlab_exports(script_dir, history);
fitlab_charts(script_dir, x, y, w, b, history);
fitlab_brief(script_dir, length(x), learning_rate, max_iter, init_w, init_b, w, b, history(end, 4));

% 命令行输出最终一行，便于快速检查收敛结果。
T = array2table(history, 'VariableNames', {'Iteration', 'w', 'b', 'Loss'});
disp('Final parameters and loss:');
disp(T(end, :));
disp('Saved files:');
disp('- iteration_first30.csv');
disp('- iteration_all50.csv');
disp('- fit_line_after_50.png');
disp('- loss_curve_50.png');
