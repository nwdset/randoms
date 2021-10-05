# %%
import numpy as np
import matplotlib.pyplot as plt

# fake data
scores = [10, 30, 100, 40, 50]
total_score = sum(scores)
scores_pct = [x / total_score for x in scores]

players = ["Alice", "Bob", "Carmen", "Dickson", "Earl"]
x = np.arange(len(players))
width = 0.35  # width of bars

# %%
fig, ax = plt.subplots()

# normal bar plot
ax.bar(x, scores_pct, width, label="Players")
ax.set_xticks(x)
ax.set_xticklabels(players)
pct_ticks = ["{:.2%}".format(x) for x in ax.get_yticks()]
ax.set_yticklabels(pct_ticks)

ax2 = ax.twinx()
ax2.set_yticklabels([0] + sorted(scores))

ax.set_facecolor("white")
ax2.set_facecolor("white")

# %%
fig.set_facecolor("white")
fig.savefig("screenshot.png")

# %%

# %%
