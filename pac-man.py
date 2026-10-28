import ctypes
import sys

try:
    mlx_lib = ctypes.CDLL("./libmlx.so")
except OSError:
    print("Error: Could not find libmlx.so. Make sure it is in the same folder.")
    sys.exit(1)


mlx_lib.mlx_init.argtypes = []
mlx_lib.mlx_init.restype = ctypes.c_void_p

mlx_lib.mlx_new_window.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
mlx_lib.mlx_new_window.restype = ctypes.c_void_p



print("Initializing MLX connection...")
mlx_ptr = mlx_lib.mlx_init()
if not mlx_ptr:
    print("Failed to initialize MLX.")
    sys.exit(1)

print("Opening window...")
win_ptr = mlx_lib.mlx_new_window(mlx_ptr, 800, 600, b"Pac-Man (Python + MLX)")
if not win_ptr:
    print("Failed to create window.")
    sys.exit(1)
