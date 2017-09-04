import re,os,shutil
def getfileeverylinetolist(fname):
    '''
    this fucntion is  used to get
    everyline to a list
    '''
    try:
        with open(fname,encoding='utf8') as f:
            content = f.readlines()
    except:
        '''
        this line is designed for python2
        '''
        with open(fname) as f:
            content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    content = [k for k in content if k!='']
    return content


def extractstuff(source,index):
    '''
    i have forgeted what is the function used to ?
    '''
    targetgroup=[]
    for k in source:
        target=k.split()
        yangtest.yangshow(target)
        try:
            targetgroup.append(target[index])
        except:
            pass
    return targetgroup


def getfilename(pathorname):
    base=os.path.basename(pathorname)
    print('The filename including extension ')
    print(base)
    name=os.path.splitext(base)[0]
    print('The filename without extension')
    print(name)
    return [base,name]



#delete a file
def delete(name):
    '''
    delete a file /folder
    '''
    if os.path.isfile(name) == True:
        os.remove(name)
    if os.path.isdir(name) == True:
        shutil.rmtree(name)




#compute a folder size
def get_size(start_path = '.'):
    '''
    compute the size of folder/file
    example
    get_folder_size('test')
    '''
    if os.path.isdir(start_path)==True:
        print('+++++++++++++++this is a dir++++++++++++++++')
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)

    if os.path.isfile(start_path)==True:
        print('+++++++++++++++this is a file+++++++++++++++++')
        total_size = os.path.getsize(start_path)
    print('the size is-------' ,round(total_size/1024/1024,2), 'M--------',round(total_size/1024/1024/1024,2),'G')
    return total_size




#computer the amouts of file s
def get_numbers_of_files():
    num = len(os.listdir('.'))
    print('the amounts of the pwd dir is ===> '+str(num))
    return num

