import cash_on_hand, overheads, profit_loss
from pathlib import Path 

overhead_value = overheads.compute_highest
coh = cash_on_hand.compute_pattern
pl = profit_loss.calculateExtreme

with open ('summary_report.txt', mode='w') as file:
    file.write(overhead_value)
    file.write(coh)
    file.write(pl)
