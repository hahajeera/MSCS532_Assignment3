import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('quicksort_bench.csv')
# average over runs
agg = df.groupby(['n','type','algorithm'])['time'].mean().reset_index()
for typ in agg['type'].unique():
    sub = agg[agg['type']==typ]
    plt.figure()
    for alg in ['randomized','deterministic']:
        alg_sub = sub[sub['algorithm']==alg]
        plt.plot(alg_sub['n'], alg_sub['time'], marker='o', label=alg)
    plt.title(f'Quicksort performance ({typ})')
    plt.xlabel('n (array size)')
    plt.ylabel('Average time (s)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'quicksort_{typ}.png')
    print('Saved plot for', typ)
