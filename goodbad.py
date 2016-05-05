import os
import re
import sys

from nltk.corpus import wordnet as wn 

# idle_a = wn.synsets('idle','a')
# print idle_a[2]
# print idle_a[0]
# print idle_a[1]

# from collections import defaultdict
 
# def wn_pos_dist():
#     """Count the Synsets in each WordNet POS category."""
#     # One-dimensional count dict with 0 as the default value:
#     cats = defaultdict(int)
#     # The counting loop:
#     for synset in wn.all_synsets():
#         cats[synset.pos] += 1
#     # Print the results to the screen:
#     for tag, count in cats3.items():
#          print tag, count
#     # Total number (sum of the above):
#     print 'Total', sum(cats.values())