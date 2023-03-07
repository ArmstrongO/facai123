# -*- coding: utf-8 -*-


file=open(file="xiaosun.txt",mode="a",encoding="utf8")

for i in range(1,101):
    file.write(f"{i}:这是内容\n")