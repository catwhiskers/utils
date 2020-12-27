import mxnet as mx
import numpy as np
import pandas as pd
from bert_embedding import BertEmbedding

class Encoder:
    def __init__(self, gpu=0):
        self.embedding = None
        if gpu == 1:
            ctx = mx.gpu(0)
            self.embedding = BertEmbedding(ctx)
        else:
            self.embedding = BertEmbedding()


    def to_q_p_bert_embeddings(self, q_str_list, p_str_list):
        reslist = []
        queries = self.embedding(q_str_list)
        titles = self.embedding(p_str_list)
        index = 0
        for q, t in zip(queries, titles):
            q_emb = np.mean(q[1], axis=0)
            p_emb = np.mean(t[1], axis=0)
            q_p_emb = np.concatenate((q_emb, p_emb), axis=0)
            reslist.append(q_p_emb)
            index += 1
        return pd.DataFrame(np.stack(reslist, axis=0))