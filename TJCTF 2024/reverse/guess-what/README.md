We're given a binary that asks us to guess what it's thinking.

```
└─$ ./chall
welcome to the guessing game!
guess what I'm thinking
3
nuh uh!
```

## Decompiling

Decompiling in `ghidra`, we get the following code.

```c
undefined8 main(void)

{
  int iVar1;
  undefined8 uVar2;
  long in_FS_OFFSET;
  int local_a4;
  FILE *flag_fp;
  char local_98 [64];
  char local_58 [72];
  long canary;

  canary = *(long *)(in_FS_OFFSET + 0x28);
  setbuf(stdout,(char *)0x0);
  puts("welcome to the guessing game!");
  puts("guess what I\'m thinking");
  fgets(local_98,0x40,stdin);
  iVar1 = strcmp(local_98,"nuh uh pls nolfjdl\n");
  if (iVar1 == 0) {
    puts("please guess a number between 0 and 100:");
    __isoc99_scanf(&DAT_00102089,&local_a4);
    if ((int)(378 / (long)local_a4) + 3 == local_a4) {
      puts("congratulations! you guessed the correct number!");
    }
    else {
      puts("sorry, you guessed the wrong number!");
    }
    flag_fp = fopen("flag.txt","r");
    if (flag_fp == (FILE *)0x0) {
      puts("flag.txt not found - ping us on discord if you are running this on the server");
      uVar2 = 1;
    }
    else {
      fgets(local_58,0x40,flag_fp);
      puts(local_58);
      uVar2 = 0;
    }
  }
  else {
    puts("nuh uh!");
    uVar2 = 1;
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar2;
}
```

The program just does a `strcmp` on our input with "nuh uh pls nolfjdl\n".
The second check for guessing a number between 0 and 100 isn't useful to us, because the flag will printed regardless, as long as the first `strcmp` passes.
So we can enter anything here.

## Solution

```py
import pwn

p = pwn.remote('tjc.tf', 31478)

p.sendlineafter(b"guess what I'm thinking", b"nuh uh pls nolfjdl")
p.sendlineafter(b"please guess a number between 0 and 100:", b"1")
p.interactive()
```