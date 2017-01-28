import sys, os, paramiko

host = sys.argv[1]
port = int(sys.argv[2])
name = sys.argv[3]
passwd = sys.argv[4]
path = sys.argv[5]
prefix = sys.argv[6]
counts = int(sys.argv[7])
mode = int(sys.argv[8], 8)

print(host)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=name, password=passwd)


fld = ((os.path.join(path, prefix)))

for i in range (1, counts+1):
	folder = fld + str(i)
	os.mkdir(folder, mode)


print('Folder were created')