import os

def get_vector(rdir):
    file_type = ['.xml', '.h', '.cpp', '.c']
    pattern = 'abcdefghijklmnopqrstuvwxyz0123456789=+-.([<>'
    regex = re.compile(r'\bif\b')
    res = [0] * (len(pattern) + 2)
    list_dirs = os.walk(rdir)
    for root, dirs, files in list_dirs:
        for fl in files:
            if os.path.splitext(fl)[1] in file_type:
                f = open(os.path.join(root, fl), 'r')
                text = f.read().lower()
                i = 0;
                for ch in pattern:
                    res[i] += text.count(ch)
                    i = i + 1
                #### part 2 ####
                res[i] += os.path.getsize(os.path.join(root, fl)) # file size
                res[i+1] += len(regex.findall(text)) # num of 'if'
    return res

def func_a(root_dir):
    list_all = os.listdir(root_dir)
    list_dir = []
    for dirs in list_all:
        if os.path.isdir(os.path.join(root_dir, dirs)):
            list_dir.append(dirs)
    return list_dir

def main():
    rdir_a = 'F://Program//Python27//py//wallp'
    rdir = 'wallp'
##    res = get_vector(rdir)
    print func_a(rdir)
##    print res



if __name__ == '__main__':
    main()
