import numpy as np
import read
import ml.cmac as cmac

def generate_model(data_set, active_weights, quantization, features):
    sig_confs = []
    for i in features:
        feat_vector = data_set[:,i]
        s_min = np.min(feat_vector)
        s_max = np.max(feat_vector)
        sig_conf = cmac.SignalConfiguration(s_min, s_max, quantization, "Feat. %d" % i)
        sig_confs.append(sig_conf)

    ann =  cmac.CMAC(sig_confs, active_weights)
    return ann

def train_ann(ann, data_set, iterations, features):
    sup_learn = cmac.Train(ann, data_set[:, features], data_set[:, 16], 1, iterations)
    sup_learn.train()

def fire_ann(ann, data_set, features):
    out = []
    for i in range(data_set.shape[0]):
        out.append(ann.fire(data_set[i, features]))
    out = np.array(out) >=0.5
    errors = sum(out != (data_set[:,16] == 1))
    return errors 
