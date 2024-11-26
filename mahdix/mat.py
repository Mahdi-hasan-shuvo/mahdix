import os,time
def ckmathod(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if 'print' in line:print(f'\033[1;31mDO NOR TRY TO Change');time.sleep(1);exit()
                else:
                    pass
    except:
        os.system('cd $HOME')
        print(f'\033[1;32mExite And run again')
        exit()
