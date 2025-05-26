import subprocess

ret = subprocess.run(
    ["notepad", ],
    capture_output=False,
    text=False,
)
print(ret.returncode)