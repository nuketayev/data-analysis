import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    nplist = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [nplist.mean(axis=0).tolist(), nplist.mean(axis=1).tolist(), nplist.mean().tolist()],
        'variance': [nplist.var(axis=0).tolist(), nplist.var(axis=1).tolist(), nplist.var().tolist()],
        'standard deviation': [nplist.std(axis=0).tolist(), nplist.std(axis=1).tolist(), nplist.std().tolist()],
        'max': [nplist.max(axis=0).tolist(), nplist.max(axis=1).tolist(), nplist.max().tolist()],
        'min': [nplist.min(axis=0).tolist(), nplist.min(axis=1).tolist(), nplist.min().tolist()],
        'sum': [nplist.sum(axis=0).tolist(), nplist.sum(axis=1).tolist(), nplist.sum().tolist()]
    }

    return calculations
