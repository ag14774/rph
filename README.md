# Random Projection Hashing

Provides a PyTorch module for random projection hashing with GPU acceleration. Similar tensors (cosine similarity) will be assigned the same hash with high probability.

## Installation
```
$ pip install rph
```

## Usage
See `example.py` for an example on how to use `rph` on DNA strings. Please note that `rph` can be used with any arbitrary tensors. In summary, this package provides a module `RandomProjectionHashModule(input_dim, hash_bits)` where `input_dim` is the size of the input tensors and `hash_bits` is the number of bits to use for the final hash value. For example, choosing 4 bits will result in all tensors being split into 16 buckets only.
