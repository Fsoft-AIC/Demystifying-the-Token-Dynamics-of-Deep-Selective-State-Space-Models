# Code for Demystifying the Token Dynamics of Deep Selective State Space Models (ICLR 2025)

[![CC BY-NC-SA 4.0](https://img.shields.io/badge/license-CC--BY--NC--SA--4.0-lightgrey)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Conference](https://img.shields.io/badge/ICLR-2025-blue)](https://iclr.cc/Conferences/2025)
[![Paper](https://img.shields.io/badge/Paper-OpenReview-red)](https://openreview.net/forum?id=qtTIP5Gjc5)

## Wikitext-103 experiments

### Setup environment: 
- Install pytorch==2.2.0 with cuda 12.1
- Install flash-attention
- Other packages are listed in mamba_wt103/requirements.txt

### Run Mamba with different scenarios
To run the WikiText-103 experiments, run:

```
cd mamba_wt103

CUDA_VISIBLE_DEVICES=0,1,2,3 python -m train experiment=wt103/mamba_pos  # for positive-eigenvalues scenario

CUDA_VISIBLE_DEVICES=0,1,2,3 python -m train experiment=wt103/mamba_neg  # for negative-eigenvalues scenario

CUDA_VISIBLE_DEVICES=0,1,2,3 python -m train experiment=wt103/mamba_real  # for mixed-eigenvalue scenario
```

## Image Classification Experiments

### Setup environment
- Install pytorch==2.2.0 with cuda 12.1
- Other library are listed in mambavision_imagenet/requirements.txt
- Download ImageNet-1K from [here](https://image-net.org/download.php) and change the data-dir path in this [script](mambavision/train.sh) accordingly

### Run MambaVision + Reordering tokens

```
cd mambavision_imagenet/mambavision
bash train.sh
```

## Citation
If you find this code useful in your research, please cite us as:

```
@misc{vo2025demystifyingtokendynamicsdeep,
      title={Demystifying the Token Dynamics of Deep Selective State Space Models}, 
      author={Thieu N Vo and Duy-Tung Pham and Xin T. Tong and Tan Minh Nguyen},
      booktitle={International Conference on Learning Representations},
      year={2025},
      url={https://openreview.net/forum?id=qtTIP5Gjc5}, 
}
```

## Acknowledgement
This repo is adapted from [safari](https://github.com/HazyResearch/safari) and [MambaVision](https://github.com/NVlabs/MambaVision) repository.