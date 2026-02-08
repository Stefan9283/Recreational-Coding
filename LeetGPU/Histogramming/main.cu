
#include <cuda_runtime.h>
#include <cstdio>

__global__ void hist(const int* input, int* histogram, int N, int num_bins) {
    int idx = blockDim.x * blockIdx.x + threadIdx.x;
    if (idx < N) {
        int val = input[idx];
        int ret = atomicAdd(histogram + val, 1);
    }
}

// input, histogram are device pointers
extern "C" void solve(const int* input, int* histogram, int N, int num_bins) {
    int threadsPerBlock = 100000;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    hist<<<threadsPerBlock, blocksPerGrid>>>(input, histogram, N, num_bins);
    cudaDeviceSynchronize();
}

#include <iostream>
#include <vector>

int main() {
    int N = 50000000;
    size_t size_V = N * sizeof(int);

    int bins = 256;
    size_t size_H = bins * sizeof(int);

    // 1. Allocate and initialize Host (CPU) memory
    std::vector<int> h_v(N);
    std::vector<int> h_H(N, 0);

    for (int i = 0; i < N; i++) {
        h_v[i] = i % bins;
    }


    // 2. Allocate Device (GPU) memory
    int *d_v, *d_H;
    cudaMalloc((void**)&d_v, size_V);
    cudaMalloc((void**)&d_H, size_H);

    // 3. Copy data from Host to Device
    cudaMemcpy(d_v, h_v.data(), size_V, cudaMemcpyHostToDevice);
    cudaMemcpy(d_H, h_H.data(), size_H, cudaMemcpyHostToDevice);

    // 4. Call your solve function
    solve(d_v, d_H, N, bins);

    // 5. Copy result back from Device to Host
    cudaMemcpy(h_H.data(), d_H, size_H, cudaMemcpyDeviceToHost);

    // 6. Verify the result
    for (int i = 0; i < bins; i++) {
        std::cout << i << "=" << h_H[i] << "\n";
    }
    
    // 7. Cleanup
    cudaFree(d_v);
    cudaFree(d_H);

    return 0;
}