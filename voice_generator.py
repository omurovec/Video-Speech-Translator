#!/usr/bin/env python3

import sys
import os

def synthesize(text):
    input = text + "|00-" + lang + "|" + lang

    # Change to Multi_TTS path
    sys.path.append(os.path.join(os.path.dirname(__file__),"dependencies/Multilingual_Text_to_Speech"))

    if "utils" in sys.modules: del sys.modules["utils"]

    from synthesize import synthesize
    from utils import build_model

    # Load Mulilingual pretrained model
    model = build_model(os.path.abspath("./dependencies/checkpoints/generated_switching.pyt"))
    model.eval()

    # generate spectogram
    spectogram = synthesize(model, "|" + input)

    # Change to WaveRNN Path
    sys.path.append(os.path.join(os.path.dirname(__file__),"dependencies/WaveRNN"))

    if "utils" in sys.modules: del sys.modules["utils"]

    from models.fatchord_version import WaveRNN
    from utils import hparams as hp
    from gen_wavernn import generate
    import torch

    # Load WaveRNN pretrained model
    hp.configure("hparams.py")
    model = WaveRNN(rnn_dims=hp.voc_rnn_dims, fc_dims=hp.voc_fc_dims, bits=hp.bits, pad=hp.voc_pad, upsample_factors=hp.voc_upsample_factors,
                    feat_dims=hp.num_mels, compute_dims=hp.voc_compute_dims, res_out_dims=hp.voc_res_out_dims, res_blocks=hp.voc_res_blocks,
                    hop_length=hp.hop_length, sample_rate=hp.sample_rate, mode=hp.voc_mode).to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    model.load(os.path.join(os.path.dirname(__file__),"dependencies/checkpoints/wavernn_weight.pyt"))

    waveform = generate(model, s, hp.voc_gen_batched, hp.voc_target, hp.voc_overlap)

    f = write("./temp/result.wav", "x")
    f.write(waveform)
    f.close()
