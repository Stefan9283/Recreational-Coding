
#include <cuda_runtime.h>
#include <cstdio>

__global__ void nearestNeighbour(const float* points, int* indices, int N) {
    int idx = blockDim.x * blockIdx.x + threadIdx.x;
    if (idx < N) {
        float x = points[idx * 3];
        float y = points[idx * 3 + 1];
        float z = points[idx * 3 + 2];

        int closest = -1;
        float closest_dist_sq = __FLT_MAX__;

        for (int i = 0; i < N; i++) {
            if (i == idx) continue;

            float x_ = points[i * 3];
            float y_ = points[i * 3 + 1];
            float z_ = points[i * 3 + 2];

            float dist_sq = pow(x - x_, 2) + pow(y - y_, 2) + pow(z - z_, 2);

            if (dist_sq < closest_dist_sq) {
                closest_dist_sq = dist_sq;
                closest = i;
            }
        }

        indices[idx] = closest;
    }
}


// points and indices are device pointers
extern "C" void solve(const float* points, int* indices, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    nearestNeighbour<<<threadsPerBlock, blocksPerGrid>>>(points, indices, N);
    cudaDeviceSynchronize();
}

#include <iostream>
#include <vector>

int main()
{
    // Defined test case
    // Point 0: (0,0,0) -> Closest to 1
    // Point 1: (1,0,0) -> Closest to 0 (dist 1) vs 2 (dist 8.66)
    // Point 2: (5,5,5) -> Closest to 1
    std::vector<float> h_points = {
        0.0f, 0.0f, 0.0f,
        1.0f, 0.0f, 0.0f,
        5.0f, 5.0f, 5.0f};
    int N = 3;

    std::vector<int> h_indices(N, -1);
    const size_t points_size = N * 3 * sizeof(float);
    const size_t indices_size = N * sizeof(int);

    // Device pointers
    float *d_points = nullptr;
    int *d_indices = nullptr;

    // Allocate and Copy
    cudaMalloc(&d_points, points_size);
    cudaMalloc(&d_indices, indices_size);
    cudaMemcpy(d_points, h_points.data(), points_size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_indices, h_indices.data(), indices_size, cudaMemcpyHostToDevice);

    // Launch
    solve(d_points, d_indices, N);

    // Retrieve
    cudaMemcpy(h_indices.data(), d_indices, indices_size, cudaMemcpyDeviceToHost);

    // Verification
    std::cout << "--- Testing solve with N=" << N << " ---" << std::endl;
    for (int i = 0; i < N; ++i)
    {
        std::cout << "Point " << i << " (" << h_points[i * 3] << "," << h_points[i * 3 + 1] << "," << h_points[i * 3 + 2] << ")";
        std::cout << " is closest to index: " << h_indices[i] << std::endl;
    }

    // Expected Output:
    // Point 0 -> 1
    // Point 1 -> 0
    // Point 2 -> 1

    cudaFree(d_points);
    cudaFree(d_indices);

    return 0;
}

