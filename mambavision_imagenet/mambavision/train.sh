#!/bin/bash

MODEL=mamba_vision_T
DATA_PATH_TRAIN="train"
DATA_PATH_VAL="val"
BS=128
EXP=my_experiment
LR=8e-4
WD=0.05
DATA_PATH="./"

CUDA_VISIBLE_DEVICES=0,1,2,3 torchrun --master_port 12367 --nproc_per_node=4 train.py --input-size 3 224 224 --crop-pct=0.875 \
--train-split=$DATA_PATH_TRAIN --val-split=$DATA_PATH_VAL --model $MODEL --amp --weight-decay ${WD} --batch-size $BS --tag $EXP --lr $LR --data_dir $DATA_PATH \
--mesa 0.25 
