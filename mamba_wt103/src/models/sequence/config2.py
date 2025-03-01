# from dataclasses import dataclass, field

# @dataclass
# class MambaConfig:

#     d_model: int = 768
#     n_layer: int = 24
#     vocab_size: int = 50257
#     ssm_cfg: dict = field(default_factory=dict)
#     rms_norm: bool = True
#     residual_in_fp32: bool = True
#     fused_add_norm: bool = True
#     pad_vocab_size_multiple: int = 8
#     tie_embeddings: bool = True
from dataclasses import dataclass, field


@dataclass
class MambaConfig:

    d_model: int = 768 #2560
    d_intermediate: int = 0
    n_layer: int = 24
    vocab_size: int = 50277
    ssm_cfg: dict = field(default_factory=dict)
    attn_layer_idx: list = field(default_factory=list)
    attn_cfg: dict = field(default_factory=dict)
    rms_norm: bool = True
    residual_in_fp32: bool = True
    fused_add_norm: bool = True
    pad_vocab_size_multiple: int = 8
    tie_embeddings: bool = True