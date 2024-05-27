# Script Downloaded and modified from https://gist.github.com/soffchen/64ac9ce1d2c0942156c5c5a6d97dcdde

DEFAULT_PASSWORD = "FFFFFFFFFFFF"
FILENAME = "myfile.eml"

with open(FILENAME, 'r') as f:
    card_content = f.read()

card_arr = card_content.split()

for i in range(16):
    pass_blk = DEFAULT_PASSWORD
    for j in range(4):
        cur_blk = i * 4 + j
        print(f"hf mf wrbl --blk {cur_blk} -d {card_arr[cur_blk]} -k {pass_blk}" + (" --force" if cur_blk == 0 else ""))

