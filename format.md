# Working With the Datasets

The data presented in the datasets will be given in one or multiple of the following data formats. The following sections will present the formats and show you how to use them.

## IDX

IDX is a fairly obscure file format known to many only for being the file format used in the MNIST dataset. For such reasons, we present datasets in this format for prototyping new architectures which would have otherwise been benchmarked on the MNIST dataset, as a drop-in replacement.

The file format is straightforward, the data is packed into binary with the bits of data written as-is to file. The format contains a header, and makes the data somewhat self-documenting. The header contains 32-bit integers representing a magic number, the size of the dataset, the configuration size in dimension 1, dimension 2, etc. followed immediately by the binary packed configuration data. An example of the header for MNIST may look like:

```
[value]                    [addr] [dtype]
magic number = (2051)      0x0000 (int32)
num = (60000)              0x0004 (int32)
Lx = (28)                  0x0008 (int32)
Ly = (28)                  0x000C (int32)
img 0 pixel 0              0x0010  (int8)
 ...                        ...     ...
```

In python, we use the `struct` package to open packed binary data in the header, then using `numpy` we can directly read in the dataset from metadata provided in the header. 

```python
import struct
import numpy as np

with open('FILENAME', 'rb') as f:
    # Suppose we try to open 2D spin configurations
    # the header contains magic number, number of samples, 
    # followed by two numbers for row and column size in 2D
    magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
    assert(magic == 2051)
    img = np.fromfile(f, dtype=np.int8).reshape(num, rows, cols)
```

Detailed information such as size and types will also be presented along with the data. 

## Plaintext

Plain .txt files are the most convenient to use, but are not packed as efficiently and do not contain header information. The simplest way to get started with the data is to use the plaintext files and use `numpy`'s built-in functions to load the data. Using the data is as simple as

```python
import numpy as np

img = np.loadtxt('FILENAME', dtype=np.int8)
```

The data may not be shaped in the way that you want, header info will be presented with the dataset, and must be used separately with plaintext files. 
