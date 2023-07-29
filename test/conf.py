import configparser

# 配置加载
config = configparser.ConfigParser()
config.read("conf.ini", encoding="utf-8")

config.sections()  # 获取section节点

print((config.get("ddns","domain")))
# print(config.get("cloudflare","domain"))
domains = config.get("cloudflare","domain").split(",")
print(domains)
for i in domains:
    print(i)