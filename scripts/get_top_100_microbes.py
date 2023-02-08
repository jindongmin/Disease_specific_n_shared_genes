#! /usr/bin/env python
import pandas as pd
from sys import argv


def get_100_microbes(table_n):
    i = pd.read_table(table_n)
    i['CI_5'] = i['log2FoldChange'] - i['lfcSE']*1.96
    i['CI_95'] = i['log2FoldChange'] + i['lfcSE']*1.96
    i_negative = i.sort_values(by=['CI_95'], ascending=True).head(100)
    i_positive = i.sort_values(by=['CI_5'], ascending=False).head(100)
    #disease_as_key = table_n.replace(dir_str, "").replace(postfix, "")
    res_n = i_negative["Unnamed: 0"]
    res_p = i_positive["Unnamed: 0"]
    return res_n, res_p


input_f = argv[1]
output_1 = argv[2]
output_2 = argv[3]

#res_n.to_csv(output_1)
a, b = get_100_microbes(input_f)
a.to_csv(output_1)
b.to_csv(output_2)
