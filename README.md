# Code for Demystifying the Token Dynamics of Deep Selective State Space Models (ICLR 2025)

[Paper link](https://openreview.net/forum?id=qtTIP5Gjc5)

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
cd mambavision
bash train.sh
```

## Citation
If you find this code useful in your research, please cite us as:

```
@misc{vo2024demystifyingtokendynamicsdeep,
      title={Demystifying the Token Dynamics of Deep Selective State Space Models}, 
      author={Thieu N Vo and Duy-Tung Pham and Xin T. Tong and Tan Minh Nguyen},
      booktitle={International Conference on Learning Representations},
      year={2025},
      url={https://openreview.net/forum?id=qtTIP5Gjc5}, 
}
```