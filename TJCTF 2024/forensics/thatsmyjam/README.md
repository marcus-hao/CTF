For this challenge, we're given `disk.img.gz`.

Decompress the file with `gzip`.

```
gzip -dv disk.img.gz
```

`file` recognizes it as a Linux image file.

To solve, just grep for the flag in the file.

```
strings disk.img.gz | grep 'tjctf{'
```

Flag: `tjctf{hell0isitm3yourel00kingf0r}`
