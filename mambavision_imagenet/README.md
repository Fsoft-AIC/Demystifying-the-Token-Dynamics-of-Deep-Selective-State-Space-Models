# Code for Demystifying the Token Dynamics of Deep Selective State Space Models (ICLR 2025)
## Image Classification Experiments

### Setup environment
- Install pytorch==2.2.0 with cuda 12.1
- Other library are listed in requirements.txt
- Download ImageNet-1K and change the data-dir path in this [script](mambavision/train.sh) accordingly

### Run MambaVision + Reordering tokens

```
cd mambavision
bash train.sh
```
