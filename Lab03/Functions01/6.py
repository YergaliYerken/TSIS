s = str(input())
ms = s.split()
a=ms[0]
ms[0]=ms[-1]
ms[-1]=a
print(' '.join(ms))