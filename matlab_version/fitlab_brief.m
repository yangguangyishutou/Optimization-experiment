function fitlab_brief(script_dir, n, learning_rate, max_iter, init_w, init_b, w, b, final_loss)
%FITLAB_BRIEF 写入 summary.txt

% 文本摘要给快速检查用：参数配置 + 最终结果。
fid = fopen(fullfile(script_dir, 'summary.txt'), 'w');
fprintf(fid, 'Linear fitting by gradient descent\n');
fprintf(fid, 'Data points: %d\n', n);
fprintf(fid, 'Learning rate: %.1f\n', learning_rate);
fprintf(fid, 'Max iterations: %d\n', max_iter);
fprintf(fid, 'Initial w: %.1f\n', init_w);
fprintf(fid, 'Initial b: %.1f\n', init_b);
fprintf(fid, 'Final w: %.10f\n', w);
fprintf(fid, 'Final b: %.10f\n', b);
fprintf(fid, 'Final loss: %.10f\n', final_loss);
fclose(fid);

end
