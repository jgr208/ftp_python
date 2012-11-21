from ftplib import FTP
import filecmp,os,time
listing = []
i = 0
ftp = FTP('192.168.1.130')
ftp.login('jason','faster72')
set_path = ftp.cwd('/media/Images/Backup')
path = ftp.pwd()
ftp.dir(listing.append)
file = listing[i]
file = file.split(' ')
file_data = []
file_data.append(file[23])
file_data.append(file[24])
file_data.append(file[25])
file_date = ' '.join(map(str,file_data))
(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat('C:\\Users\\Jason\\Desktop\\test.txt')
mtime = time.ctime(mtime)
mtime = mtime.split()
mtime.pop(0)
mtime.pop()
mtime = ' '.join(map(str,mtime))
mtime = mtime.replace(' ',' ')[:-3]
print 'File name: ' + file[26]
print 'Last backup : '+ file_date
print 'Last save: ' + mtime
ftp.quit()