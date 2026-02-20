###
# In this example, we will explore how to use the annotate function in matplotlib to add annotations to our plots.
#
# - threshold lines
# - event markers
# - highlighed time regions
# - arrows explaining anomalies
#
# Mindset:
# When analyzing data, we usually answer:
# - When did the signal exceed a certain threshold?
# - When did ocsilliations occur?
# - What happened at a specific time?
# - How long did a specific event last?
# - Where is the maximum/minimum value?
#
# With ax.axhline() function, we can add horizontal lines to indicate thresholds.
# With ax.axvline() function, we can add vertical lines to indicate specific time points.
# With ax.axvspan() function, we can add highlighted regions to indicate time intervals.
# With ax.text() function, we can add text annotations to explain specific points or regions in the plot.
# With ax.annotate() function, we can add arrows to point out specific features or anomalies in the plot.
#
# Exp: Do not over annotate. Only annotate what matters. 1-3 annotations per subplot max.
###

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import random
import heapq
class cep_analyzer:
    def __init__(self, percent, ideal_value: int = 0):
        self.min_heap = []
        self.max_heap = []
        self.percent = percent
        self.ideal_value = ideal_value
    
    def add_sample(self, sample):
        deviation = abs(sample - self.ideal_value)
        if not self.max_heap or deviation <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -deviation)
        else:
            heapq.heappush(self.min_heap, deviation)
        
        total_samples = len(self.max_heap) + len(self.min_heap)
        desired_max_heap_size = int(total_samples * self.percent)
        while len(self.max_heap) > desired_max_heap_size:
            moved_sample = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, moved_sample)
        while len(self.max_heap) < desired_max_heap_size:
            moved_sample = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -moved_sample)
    
    def get_cep(self):
        if not self.min_heap:
            return None
        return self.min_heap[0]

cep_68_analyzer = cep_analyzer(percent=0.68, ideal_value=100)
cep_95_analyzer = cep_analyzer(percent=0.95, ideal_value=100)
cep_99_analyzer = cep_analyzer(percent=0.99, ideal_value=100)

# sample jitter data
# data stream is expected to output 10Hz (100ms per sample), but jitter causes variability in the actual timing of the samples.
timestamps = [i * 100 + random.uniform(-10, 10) for i in range(1000)]
jitters = [timestamps[i] - timestamps[i - 1] for i in range(1, len(timestamps))]
for jitter in jitters:
    cep_68_analyzer.add_sample(jitter)
    cep_95_analyzer.add_sample(jitter)
    cep_99_analyzer.add_sample(jitter)
cep_68 = cep_68_analyzer.get_cep()
cep_95 = cep_95_analyzer.get_cep()
cep_99 = cep_99_analyzer.get_cep()

first_peak_idx = jitters.index(max(jitters)) # index of the first peak in the jitter data
left_highlight = max(first_peak_idx - 50, 0)
right_highlight = min(first_peak_idx + 50, len(jitters) - 1)

x = [i for i in range(len(jitters))] # x ticks for plotting

# ploting
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(x, jitters, marker='o', markersize=2, linestyle='-', linewidth=0.5, color='green', label='Jitter (ms)')
ax.set_ylabel('Jitter (ms)')
ax.set_xlabel('Sample Index')

ax.axhline(y=100, color='red', linestyle='-', label='Expected Interval (100ms)') # threshold line

ax.axhline(y=100 + cep_68, color='orange', linestyle='--', label=f'CEP_68 (+/-{cep_68:.2f} ms)') # threshold line
ax.axhline(y=100 - cep_68, color='orange', linestyle='--') # threshold line

ax.axhline(y=100 + cep_95, color='blue', linestyle='--', label=f'CEP_95 (+/-{cep_95:.2f} ms)') # threshold line
ax.axhline(y=100 - cep_95, color='blue', linestyle='--') # threshold line

ax.axhline(y=100 + cep_99, color='purple', linestyle='--', label=f'CEP_99 (+/-{cep_99:.2f} ms)') # threshold line
ax.axhline(y=100 - cep_99, color='purple', linestyle='--') # threshold line

ax.axvline(x=500, color='red', linestyle=':', label='Event Marker (Sample 500)') # event marker

ax.axvspan(xmin=left_highlight, xmax=right_highlight, color='yellow', alpha=0.3, label='Highlighted Jitter Region') # highlighted time region

ax.annotate('First Peak', xy=(first_peak_idx, jitters[first_peak_idx]), xytext=(first_peak_idx + 50, jitters[first_peak_idx] + 10), arrowprops=dict(color='black', shrink=0.05), fontsize=10, color='black') # arrow annotation

ax.text(x=500, y=121, s='Middle line', fontsize=10, color='red', ha='center') # text annotation

limit_margin = 1
ax.set_ylim(min(jitters) - limit_margin, max(jitters) + limit_margin) # set y limits to focus on jitter around the expected interval
ax.set_xlim(0, len(jitters) + 1) # set x limits to fit the data

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.legend(loc='center left', fontsize=8, framealpha=0.5, edgecolor='gray', bbox_to_anchor=(1, 0.5))

plt.suptitle('Jitter Analysis with Annotations', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # adjust layout to make room for suptitle
plt.show()
