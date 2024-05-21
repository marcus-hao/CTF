import pwn

p = pwn.remote('tjc.tf', 31478)

p.sendlineafter(b"guess what I'm thinking", b"nuh uh pls nolfjdl")
p.sendlineafter(b"please guess a number between 0 and 100:", b"1")
p.interactive()