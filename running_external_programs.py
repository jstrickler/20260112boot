from shlex import split
from subprocess import run, CalledProcessError, PIPE, Popen

RAW_CMD = "netstat -an"

CMD = split(RAW_CMD)

print(f"{CMD = }")

# run(CMD)

try:
    process = run(CMD, stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err)
else:
    stdout_lines = process.stdout.decode().splitlines()
    print(f"{len(stdout_lines)} lines in output")
    connections = [line for line in stdout_lines if 'ESTAB' in line]
    for connection_line in connections:
        print(connection_line)    
print('-' * 60)

process = Popen("bc", stdout=PIPE, stdin=PIPE, stderr=PIPE)
print(f"{process.communicate() = }")


