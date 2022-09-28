import numpy as np



def _read(file):
    with open(file, 'r') as f:
        data = []
        for l in f:
            data.append(l)
        return data

def process(file):
    data = _read(file)
    num_cols = len(data[0].strip().split(','))
    S = np.empty((len(data), num_cols), dtype=object)
    for i in range(len(data)):
        S[i] = data[i].strip().split(',')
    return S

def main(): 
    # read data
    S = process('../data/test_final.csv')
    # create decision tree
    tree = DecisionTree.ID3(S)
    # print decision tree
    print(tree)

if __name__ == "__main__":
    main()