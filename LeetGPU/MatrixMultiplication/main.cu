
#include <cuda_runtime.h>
#include <cstdio>
__global__ void matrix_multiplication_kernel(const float* A, const float* B, float* C, int M, int N, int K) {
    int k = blockDim.x * blockIdx.x + threadIdx.x;
    int m = blockDim.y * blockIdx.y + threadIdx.y;
    
    if (m < M && k < K) { 
        float sum = 0.0f;
        for (int n = 0; n < N; n++) {
            sum += A[m * N + n] * B[n * K + k]; 
        }
        C[m * K + k] = sum;
    }
}

// A, B, C are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* A, const float* B, float* C, int M, int N, int K) {
    dim3 threadsPerBlock(16, 16);
    dim3 blocksPerGrid((K + threadsPerBlock.x - 1) / threadsPerBlock.x,
                       (M + threadsPerBlock.y - 1) / threadsPerBlock.y);

    matrix_multiplication_kernel<<<blocksPerGrid, threadsPerBlock>>>(A, B, C, M, N, K);
    cudaDeviceSynchronize();
}

#include <iostream>

int main() {
    // Dimensions
    int M = 8192; // Rows of A and C
    int N = 6144; // Cols of B and C
    int K = 4096; // Cols of A and Rows of B

    size_t size_A = M * N * sizeof(float);
    size_t size_B = N * K * sizeof(float);
    size_t size_C = M * K * sizeof(float);

    // Host Allocation
    float *h_A = new float[M*N], *h_B = new float[N*K], *h_C = new float[M*K];
    for(int i=0; i<M*N; i++) h_A[i] = 1.0f;
    for(int i=0; i<N*K; i++) h_B[i] = 2.0f;

    // Device Allocation
    float *d_A, *d_B, *d_C;
    cudaMalloc(&d_A, size_A);
    cudaMalloc(&d_B, size_B);
    cudaMalloc(&d_C, size_C);

    cudaMemcpy(d_A, h_A, size_A, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, size_B, cudaMemcpyHostToDevice);

    solve(d_A, d_B, d_C, M, N, K);
    // ----------------------------

    cudaMemcpy(h_C, d_C, size_C, cudaMemcpyDeviceToHost);

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < K; j++) {
            printf("%3.0f ", h_C[i * K + j]);
        }
        std::cout << "\n";
    }

    // Cleanup
    cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);
    delete[] h_A; delete[] h_B; delete[] h_C;

    return 0;
}