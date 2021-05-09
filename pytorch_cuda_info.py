import torch
import platform

print('Using Python version:', platform.python_version())
print('Using Torch version:', torch.__version__)

device = torch.cuda.is_available()
print('Is GPU available:', device)

cur_device = torch.cuda.current_device()
print('Using device ID:', cur_device)

device_name = torch.cuda.get_device_name()
print('Device name:', device_name)

device_capability = torch.cuda.get_device_capability()
print('Device capability:', device_capability)

max_memory_alo = torch.cuda.max_memory_allocated()
print('Max memory allocated:', max_memory_alo)