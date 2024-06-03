import torch
import numpy as np

data = np.array([
[[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
[[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
[[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]])

t_data = torch.tensor(data, dtype=float)

print("===== problem 1 =====")
print(t_data.size())

print("===== problem 2 =====")
t_data = torch.permute(t_data, (2,0,1))
print(t_data)
print(t_data.size())

print("===== problem 3 =====")
t_data_sum = t_data.sum(dim=0)
print(t_data_sum)

print("===== problem 4 =====")
t_data_ave = t_data_sum.mean(dim=1)
print(t_data_ave)

print("===== problem 5 =====")
t_data_sum_sum = t_data_sum.sum(dim=1)
t_data_ave2 = t_data_sum_sum / 5
print(t_data_ave2)
