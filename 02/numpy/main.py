import numpy as np

data = np.array([
[[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
[[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
[[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]])

print(data.shape)
print("各クラスの科目別平均点：\n", np.mean(data, axis=1))
print("全クラスの番号3番の学生の中で2科目目の最低?得点：",np.min(data, axis=0)[2,1])
print("各科目で一番点数が高い人と低い人の点差：", np.max(np.max(data, axis=1),axis=0) - np.min(np.min(data, axis=1)))
print("各クラスの1科目目が80点以上の人数：", np.sum((data >= 80), axis=1)[:,0])
print("2科目の合計点が135点を超えている人数：", np.sum(np.sum(data, axis=2)>=135))
print("全生徒の1科目目と2科目目の相関係数", (np.sum(np.reshape((data - np.mean(np.mean(data,axis=1),axis=0)), (15,2))[:,0] * np.reshape((data - np.mean(np.mean(data,axis=1),axis=0)), (15,2))[:,1])/15)/(((np.sum(np.sum(((data - np.mean(np.mean(data,axis=1),axis=0))**2), axis=1),axis=0)/15)**(1/2))[0] * ((np.sum(np.sum(((data - np.mean(np.mean(data,axis=1),axis=0))**2), axis=1),axis=0)/15)**(1/2))[1]))