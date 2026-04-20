function fitlab_exports(script_dir, history)
%FITLAB_EXPORTS 将迭代历史写入 iteration_all50 / iteration_first30

% 转成 table，便于后续操作。
T = array2table(history, 'VariableNames', {'Iteration', 'w', 'b', 'Loss'});

% 全量记录：保留每次更新后的参数与损失。
writetable(T, fullfile(script_dir, 'iteration_all50.csv'));

% 前 30 次迭代：只保留前 30 次迭代的结果。
n_head = min(30, height(T));
writetable(T(1:n_head, :), fullfile(script_dir, 'iteration_first30.csv'));

end
