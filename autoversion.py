import subprocess

subprocess.Popen('git add .', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
subprocess.Popen("git commit -m 'Teste'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
subprocess.Popen('git push', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# for line in p.stdout.readlines():
#     print(line, end=' \n')
# retval = p.wait()