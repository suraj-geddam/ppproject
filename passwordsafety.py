import hashlib
import itertools

md5list = ["11d9c573cd4c10b313faf5c9d0bdc559",
            "26a904aad83012852cd681239ad3849f",
            "29ee1b0325f4b17b3f2697df2f96d7aa",
            "4416ca869588dc1ec3923f87c177a613",
            "52d2371364b19c1e95514acb56e22bf5",
            "54170e99cf1989a9d5321ed56a3050b2",
            "55eaadd0dae29a58b52044394ae30976",
            "5ac2362cf0b7cf2417da1bea8db2fe76",
            "5f93be60e72c8ac12203bdecf5341bb2",
            "606c19c5797be16b5e46cc1b4688b4cc",
            "61106aa9ca2bba41251310d849d096af",
            "6d4d943a4c3ce52de19e36a9f3c87149",
            "82e47330940987e3cb9f036af9989e01",
            "b5f54403f9ad3399aa7d52950e22de25",
            "b7ec9e01cbe6ca817001b894a2960ba9",
            "bbed1cd492219b1368301b6eda6d9e06",
            "bc1785a9e13f06aadfac0612b337a93f",
            "d160f705def9149f543aaa9e09226436",
            "d5cc80b4b21ad3b19f04d12168ffb547",
            "e225c143d7d7309e546996a6e66d7540",
            "e9180fd28270decce76470910931df0e",
            "f2b812ab8e5719c1ba115d6ea35a5938"]

md5Hash = {}

for i in md5list:
	md5Hash[i] = True

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = list(range(1,100))
nums = [str(i) for i in nums]
nums.append("0")
nums.append("00")
nums.append("01")
nums.append("02")
nums.append("03")
nums.append("04")
nums.append("05")
nums.append("06")
nums.append("07")
nums.append("08")
nums.append("09")
wordlens = [1, 2, 3, 4, 5, 6]


for wordlen in wordlens:
    words = map(''.join, itertools.product(alphabets, repeat = wordlen))
    for word in words:
        for num in nums:
            pwcand = word+num
            m = hashlib.md5()
            m.update(pwcand.encode())
            hexd = m.hexdigest()
            if hexd in md5Hash:
	            print("Password "+pwcand+" corresponds to hash "+hexd)

# Password apr1 corresponds to hash 5f93be60e72c8ac12203bdecf5341bb2
# Password ash21 corresponds to hash 52d2371364b19c1e95514acb56e22bf5
# Password hit7 corresponds to hash d160f705def9149f543aaa9e09226436
# Password jag9 corresponds to hash 82e47330940987e3cb9f036af9989e01
# Password nak2 corresponds to hash b7ec9e01cbe6ca817001b894a2960ba9
# Password sun12 corresponds to hash 11d9c573cd4c10b313faf5c9d0bdc559
# Password gold24 corresponds to hash 29ee1b0325f4b17b3f2697df2f96d7aa
# Password heya17 corresponds to hash 4416ca869588dc1ec3923f87c177a613
# Password icpc16 corresponds to hash 6d4d943a4c3ce52de19e36a9f3c87149
# Password jraj14 corresponds to hash d5cc80b4b21ad3b19f04d12168ffb547
# Password relx11 corresponds to hash 61106aa9ca2bba41251310d849d096af
# Password wish5 corresponds to hash bc1785a9e13f06aadfac0612b337a93f
# Password yvyv10 corresponds to hash 26a904aad83012852cd681239ad3849f
# Password bells22 corresponds to hash 55eaadd0dae29a58b52044394ae30976
# Password eswar13 corresponds to hash b5f54403f9ad3399aa7d52950e22de25
# Password queue19 corresponds to hash 5ac2362cf0b7cf2417da1bea8db2fe76
# Password rages8 corresponds to hash 606c19c5797be16b5e46cc1b4688b4cc
# Password rajat4 corresponds to hash f2b812ab8e5719c1ba115d6ea35a5938
# Password tarun18 corresponds to hash 54170e99cf1989a9d5321ed56a3050b2
# Password anirud23 corresponds to hash e9180fd28270decce76470910931df0e
# Password harhar20 corresponds to hash bbed1cd492219b1368301b6eda6d9e06
