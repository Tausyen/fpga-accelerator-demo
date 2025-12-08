import numpy as np
import matplotlib.pyplot as plt

def mac_array_multiply(A, B):
    # A: m x k, B: k x n -> C: m x n
    m, k = A.shape
    k2, n = B.shape
    assert k == k2
    C = np.zeros((m, n))
    # simplified systolic-like schedule: compute C by outer products using small array
    # For demonstration, simulate a 2x2 MAC array computing partial sums with timestep trace
    trace = []
    # naive multiplication but record which MACs would operate at each step
    for t in range(k):
        # At step t, multiply column t of A with row t of B
        a_col = A[:, t].reshape(m,1)  # m x 1
        b_row = B[t, :].reshape(1, n) # 1 x n
        # outer product gives m x n partial product
        partial = a_col @ b_row
        C += partial
        trace.append(partial.copy())
    return C, trace

def plot_trace(trace):
    # plot sum of abs(partial) per timestep as a simple visualization
    sums = [np.sum(np.abs(t)) for t in trace]
    plt.figure()
    plt.plot(sums, marker='o')
    plt.title("Partial product magnitude per timestep")
    plt.xlabel("timestep")
    plt.ylabel("sum(abs(partial))")
    plt.tight_layout()
    plt.savefig("../results/mac_array_trace.png")
    plt.show()

def example():
    np.random.seed(1)
    A = np.random.randint(-4,5,(4,4))
    B = np.random.randint(-4,5,(4,4))
    C, trace = mac_array_multiply(A,B)
    print("A:\n", A)
    print("B:\n", B)
    print("C (A@B):\n", C)
    plot_trace(trace)

if __name__ == "__main__":
    example()
