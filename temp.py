import os


root = r'C:\Users\nagarajan\Desktop\Natasha Daycare'

records = []
for fn in os.listdir(root):
    fpath = os.path.join(root, fn)
    records.append((os.path.getmtime(fpath), fn))

records.sort(reverse=True)

count = 1
for t, fn in records:
    opath = os.path.join(root, fn)
    npath = os.path.join(root, '%03d.png' % count)
    os.rename(opath, npath)
    count += 1

print records

