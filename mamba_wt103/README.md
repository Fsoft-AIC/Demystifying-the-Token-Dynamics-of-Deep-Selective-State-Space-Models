# Code for Demystifying the Token Dynamics of Deep Selective State Space Models (ICLR 2025)

## Language modeling on WikiText-103 experiment

### Enviroment: 
- Install pytorch==2.2.0 with cuda 12.1
- Install flash-attention
- Other packages are listed in requirements.txt

### Exeriments
To run the WikiText-103 experiments, run:
```
CUDA_VISIBLE_DEVICES=0,1,2,3 python -m train experiment=wt103/mamba_pos  # for positive-eigenvalues scenario
CUDA_VISIBLE_DEVICES=0,1,2,3 python -m train experiment=wt103/mamba_neg  # for negative-eigenvalues scenario
CUDA_VISIBLE_DEVICES=0,1,2,3 python -m train experiment=wt103/mamba_real  # for mixed-eigenvalue scenario
```
