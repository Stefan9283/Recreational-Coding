
#include <cuda_runtime.h>

__global__ void vector_add(const float* A, const float* B, float* C, int N) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    if (i < N) {
        C[i] = A[i] + B[i];
    }
}

// A, B, C are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* A, const float* B, float* C, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    vector_add<<<blocksPerGrid, threadsPerBlock>>>(A, B, C, N);
    cudaDeviceSynchronize();
}

#include <iostream>
#include <vector>

int main() {
    int N = 10000;
    size_t size = N * sizeof(float);

    // 1. Allocate and initialize Host (CPU) memory
    std::vector<float> h_A(N, 1.0f); // Fill with 1.0
    std::vector<float> h_B(N, 2.0f); // Fill with 2.0
    std::vector<float> h_C(N, 0.0f);

    // 2. Allocate Device (GPU) memory
    float *d_A, *d_B, *d_C;
    cudaMalloc((void**)&d_A, size);
    cudaMalloc((void**)&d_B, size);
    cudaMalloc((void**)&d_C, size);

    // 3. Copy data from Host to Device
    cudaMemcpy(d_A, h_A.data(), size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B.data(), size, cudaMemcpyHostToDevice);

    // 4. Call your solve function
    std::cout << "Running vector addition on GPU..." << std::endl;
    solve(d_A, d_B, d_C, N);

    // 5. Copy result back from Device to Host
    cudaMemcpy(h_C.data(), d_C, size, cudaMemcpyDeviceToHost);

    // 6. Verify the result
    bool success = true;
    for (int i = 0; i < N; i++) {
        if (h_C[i] != 3.0f) {
            success = false;
            break;
        }
    }

    if (success) std::cout << "Success! 1.0 + 2.0 = " << h_C[0] << std::endl;
    else std::cout << "Something went wrong." << std::endl;

    // 7. Cleanup
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    return 0;
}