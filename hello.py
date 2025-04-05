def main():
    print("Hello from how-do-i-set-up-torch-with-uv!")
    print("Checking if CUDA is enabled...")
    import torch
    from torch import __version__
    print(f"PyTorch version: {__version__}")
    cuda_is_available = torch.cuda.is_available()
    print(f"CUDA is available: {cuda_is_available}")
    if not cuda_is_available:
        import sys
        sys.exit("CUDA is not available. Please check your PyTorch installation and CUDA setup.")

    # multiply two random tensors on the gpu
    print("Multiplying two random tensors on the GPU...")
    a = torch.randn(10_000, 10_000).cuda()
    b = torch.randn(10_000, 10_000).cuda()
    c = torch.matmul(a, b)
    print("Multiplication completed.")
    print("Result shape:", c.shape)
    print("Result device:", c.device)
    print("Done!")

if __name__ == "__main__":
    main()
