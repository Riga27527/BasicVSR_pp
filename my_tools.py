import os


def generate_anno():
    base_dir = r'./data/Bistro_train/GT'
    txt_path = r'./data/Bistro_train/ann.txt'
    out = ''
    for base_name in os.listdir(base_dir):
        sub_path = os.path.join(base_dir, base_name)
        length_sub = len(os.listdir(sub_path))
        for j in range(length_sub):
            out += base_name + '/' + str(j) + ' ' + str(length_sub) + '\n'
    with open(txt_path, 'w') as f:
        f.write(f'{out}')

if __name__ == '__main__':
    generate_anno()