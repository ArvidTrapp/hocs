# author: Arvid Trapp, arvid.trapp@hm.edu, Munich University of Applied Sciences
#%%
def getCumulantSpectrum(n = 4):
    from sympy.utilities.iterables import multiset_partitions
    freqs  = ['f' + str(n) for n in range(n+1)][1:]
    exp    = 'C_{' + n *'x' + '}(' + str(freqs) + ') = S_{' + n *'x' + '}(' + str(freqs) + ')'
    for p in multiset_partitions(freqs):
        if len(p) > 1 and len(p) < n:
            temp = ''
            for ps in p:
                temp += 'S_{' + len(ps)*'x' + '}(' + str(ps[:-1]) + ')'
                if freqs[-1] not in ps:
                    temp += '\delta(' + str(ps) + ')'
                if len(ps) < 2:
                    break
            else:
                exp += ' - ' + temp   
    return exp

for n in [2,3,4,5,6]:
    print('Cumulant Spectrum of order ',n,': ')
    print(getCumulantSpectrum(n))

# %%
