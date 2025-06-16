import subprocess

subprocess.Popen('cd c:/Users/johnhca/Documents/Repositorio/Pessoal/autoversion/ & git add .', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
subprocess.Popen('cd c:/Users/johnhca/Documents/Repositorio/Pessoal/autoversion/ & git commit -m "Backup"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
subprocess.Popen('cd c:/Users/johnhca/Documents/Repositorio/Pessoal/autoversion/ & git push', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# for line in p.stdout.readlines():
#     print(line, end=' \n')
# retval = p.wait()