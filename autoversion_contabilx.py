from datetime import datetime
import subprocess

p = subprocess.Popen('y: & cd contabilx & git add .', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line, end=' \n')
retval = p.wait()

date = datetime.now().strftime("%d/%m/%Y")
p = subprocess.Popen(f'y: & cd contabilx & git commit -m "Backup Automático {date}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line, end=' \n')
retval = p.wait()


p = subprocess.Popen('y: & cd contabilx & git push', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line, end=' \n')
retval = p.wait()