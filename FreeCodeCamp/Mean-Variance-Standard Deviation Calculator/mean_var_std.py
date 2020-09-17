import numpy as np

def calculate(list):
    calculations = {}
    if len(list) != 9:
        raise ValueError ("List must contain nine numbers.")

    arr = np.array(list).reshape(3,3)

    ax1_mean = []
    for i in range(3): ax1_mean.append(arr[:, i].mean())
    ax2_mean = []
    for i in range(3): ax2_mean.append(arr[i].mean())
    calculations["mean"] = [ax1_mean,ax2_mean,arr.mean()]

    ax1_var = []
    for i in range(3): ax1_var.append(arr[:, i].var())
    ax2_var = []
    for i in range(3): ax2_var.append(arr[i].var())
    calculations["variance"] = [ax1_var,ax2_var,arr.var()]

    ax1_std_dev = []
    for i in range(3): ax1_std_dev.append(arr[:, i].std())
    ax2_std_dev = []
    for i in range(3): ax2_std_dev.append(arr[i].std())
    calculations["standard deviation"] = [ax1_std_dev,ax2_std_dev,arr.std()]

    ax1_max = []
    for i in range(3): ax1_max.append(arr[:, i].max())
    ax2_max = []
    for i in range(3): ax2_max.append(arr[i].max())
    calculations["max"] = [ax1_max,ax2_max,arr.max()]

    ax1_min = []
    for i in range(3): ax1_min.append(arr[:, i].min())
    ax2_min = []
    for i in range(3): ax2_min.append(arr[i].min())
    calculations["min"] = [ax1_min,ax2_min,arr.min()]

    ax1_sum = []
    for i in range(3): ax1_sum.append(arr[:, i].sum())
    ax2_sum = []
    for i in range(3): ax2_sum.append(arr[i].sum())
    calculations["sum"] = [ax1_sum,ax2_sum,arr.sum()]

    #for key,val in calculations.items(): print(key,val)

    return calculations

#calculate([0,1,2,3,4,5,6,7,8])
