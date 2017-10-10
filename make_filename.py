# import os
# import shutil
# datapath = 'E:/realdata/'
# train_data = 'E:/traindata'
# val_data = 'E:/realvaldata'
# data_list = os.listdir(datapath)
# for obj in data_list:
#     path = os.path.join(datapath, obj)
#     data = os.listdir(path)
#     n = len(data)
#     for i in range(n):
#         if i< n//2:
#             rfilename = os.path.join(path, data[i])
#             dfilename = '%06d.png'%(i+1)
#             dpath = os.path.join(train_data, obj)
#             shutil.copy(rfilename, os.path.join(dpath, dfilename))
#         else:
#             rfilename = os.path.join(path, data[i])
#             dfilename = '%06d.png' % (i + 1)
#             dpath = os.path.join(val_data, obj)
#             shutil.copy(rfilename, os.path.join(dpath, dfilename))

import os
import shutil
traindata = 'E:/realvaldata'
traindata1 = 'E:/valdata1/images'
data_list = os.listdir(traindata)
total = 0
for obj in data_list:
    path = os.path.join(traindata, obj)
    data = os.listdir(path)
    n = len(data)
    total += n
    for i in range(total-n,total):
        dfilename = '%06d.png' %(i+155)
        shutil.copy(os.path.join(path, data[i-total+n]), os.path.join(traindata1, dfilename))


print(total)





