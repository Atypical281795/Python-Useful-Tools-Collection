X = 2000
for i in  range(X):
    for j in range(X):
        k = j * i
    print(f'{i + 1} / {X}', end='\r')
print('\n完成! \n')

for i in  range(X):
    for j in range(X):
        k = j * i
    print('進度A',
          f'|{"*" * ((i + 1) * 50 // X):50}|',
          f'{(i + 1) * 100// X}%',
          end='\r')
print('\n完成! ')

###############################################
#https://stackoverflow.com/questions/3160699/python-progress-bar
from progress.bar import Bar
X = 2000
with Bar('進度B', max=X) as bar:
    for i in range(X):   
        for j in range(X):
            k = j * i
        bar.next()
print('\n完成')

with Bar('剩餘練習時長', max=X, fill='@',
         suffix='%(percent).lf%% - %(eta)ds') as bar:
    for i in range(X):   
        for j in range(X):
            k = j * i
        bar.next()
print('\n完成')

###############################################
#https://github.com/tqdm/tqdm
#tqdm->taqadum,阿拉伯語的 "進度" 的意思(同時也是西班牙語言的"我好愛你":D)
from tqdm import tqdm
from tqdm.tk import tqdm
X = 5000
for i in tqdm(range(X)):
    for j in range(X):
        k = j * i
print('\n完成')

###############################################
#rich本身也是一個module，記得install
from tqdm.rich import tqdm
from time import sleep
bar = tqdm(total=100)
bar.set_description('採集數據')
sleep(0.5)
bar.update(10)
bar.set_description('清洗數據')
sleep(0.5)
bar.update(10)
bar.set_description('儲存數據')
sleep(0.5)
bar.update(79)

###############################################
from alive_progress import alive_bar
X = 5000
with alive_bar(X) as bar:
    for i in range(X):
        for j in range(X):
            k = j * i
        bar()
print('完成! ')

###############################################

#from alive_progress.styles import showtime
#showtime()#<-該指令需要TTY接口，故windows預設無法驅動，造成錯誤