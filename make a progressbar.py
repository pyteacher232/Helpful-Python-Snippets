from tqdm import *

n = 10
bar = tqdm(total=10)
bar.set_description("You're in a progress bar...")

for i in range(n):
    bar.update()

bar.close()