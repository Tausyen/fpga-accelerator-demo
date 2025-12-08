import numpy as np
import time
import matplotlib.pyplot as plt

def dense_conv_1d(x, k):
    n = len(x) - len(k) + 1
    y = np.zeros(n)
    mults = 0
    for i in range(n):
        for j in range(len(k)):
            y[i] += x[i+j] * k[j]
            mults += 1
    return y, mults

def sparse_conv_1d(x, k):
    # k can contain zeros; skip zero taps
    idx = [i for i, v in enumerate(k) if v != 0]
    kvals = [k[i] for i in idx]
    n = len(x) - len(k) + 1
    y = np.zeros(n)
    mults = 0
    for i in range(n):
        for j, val in zip(idx, kvals):
            y[i] += x[i+j] * val
            mults += 1
    return y, mults

def experiment():
    np.random.seed(0)
    x = np.random.randn(1000)
    # example: kernel length 11 with 30% non-zero
    k = np.zeros(11)
    nonzero_indices = [0, 3, 5, 7]  # example sparsity
    k[nonzero_indices] = np.random.randn(len(nonzero_indices))
    # Dense
    t0 = time.time()
    yd, md = dense_conv_1d(x, k)
    t1 = time.time()
    # Sparse
    ys, ms = sparse_conv_1d(x, k)
    t2 = time.time()
    print("Dense mults:", md, "time:", t1 - t0)
    print("Sparse mults:", ms, "time:", t2 - t1)
    # plot a small segment comparison
    plt.figure(figsize=(6,3))
    plt.plot(yd[:200], label='dense')
    plt.plot(ys[:200], label='sparse', linestyle='--')
    plt.legend()
    plt.title(f"dense mults={md}, sparse mults={ms}")
    plt.tight_layout()
    plt.savefig("../results/dense_vs_sparse.png")
    plt.show()

if __name__ == "__main__":
    experiment()
