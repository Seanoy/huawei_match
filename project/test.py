import numpy as np

if __name__ == "__main__":
    print("hello")
    ndarr = np.asarray([[1, 2], [3, 4], [5, 2]])
    index = np.argwhere(ndarr == 2)
    print(ndarr)
    print(ndarr[index[0][0]][index[0][1]])

    c = np.vstack((ndarr, [1, 3]))
    d = np.append(ndarr, [[6, 7]], axis=0)
    print(c)
    print(d)
    for element in ndarr.flat:
        print(element)
    a = np.arange(8).reshape(2, 2, 2)
    print(np.rollaxis(a, 1, 0))
    print(np.rollaxis(a, 2, 1))

    aa = [0,3,5]
    print(np.transpose(np.nonzero(aa)))

