import numpy as np

import sys
sys.path.append("../")
from MFDFA import MFDFA

def test_MFDFA():
    for N in [1000, 10000]:
        for q_list in [1, 2, 6, 21]:

            X = np.random.normal(size = N, loc = 0)
            q = np.linspace(-10, 10, q_list)

            lag = np.unique(
                  np.logspace(
                  0, np.log10(X.size // 4), 25
                  ).astype(int) + 1
                )

            lag, dfa = MFDFA(X, lag = lag, q = q, order = 1)

            assert dfa.ndim == 2, "Output is not 2 dimensional"
            assert dfa.shape[1] <= q.shape[0], "Output shape mismatch"

            # Testing conventional MFDFA with stats
            lag, dfa, dfa_std = MFDFA(X, lag = lag, q = q, order = 2,
              stat = True)

            assert dfa.ndim == 2, "Output is not 2 dimensional"
            assert dfa.shape[1] <= q.shape[0], "Output shape mismatch"

            # Testing modified = True option
            lag, dfa, dfa_std = MFDFA(X, lag = lag, q = q, order = 2,
              modified = True, stat = True)

            assert dfa.ndim == 2, "Output is not 2 dimensional"
            assert dfa.shape[1] <= q.shape[0], "Output shape mismatch"

            # Testing eDFA extension
            lag, dfa, edfa = MFDFA(X, lag = lag, q = q, order = 3,
              stat = False, extensions = {'eDFA':True})

            assert dfa.ndim == 2, "Output is not 2 dimensional"
            assert edfa.ndim == 2, "Output is not 2 dimensional"
            assert dfa.shape[1] <= q.shape[0], "Output shape mismatch"

            # Testing EMD extension
            lag, dfa = MFDFA(X, lag = lag, q = q, order = 0,
              stat = False, extensions = {'EMD': [0]})

            assert dfa.ndim == 2, "Output is not 2 dimensional"
            assert dfa.shape[1] <= q.shape[0], "Output shape mismatch"

            # Testing EMD and eDFA extensions together
            lag, dfa, edfa = MFDFA(X, lag = lag, q = q, order = 1,
              stat = False, extensions = {'eDFA':True, 'EMD': [0]})

            assert dfa.ndim == 2, "Output is not 2 dimensional"
            assert edfa.ndim == 2, "Output is not 2 dimensional"
            assert dfa.shape[1] <= q.shape[0], "Output shape mismatch"

            # Testing moving window
            lag, dfa, edfa = MFDFA(X, lag = lag, q = q, order = 1,
              window = 5, stat = False)

            assert dfa.ndim == 2, "Output is not 2 dimensional"
            assert dfa.shape[1] <= q.shape[0], "Output shape mismatch"
