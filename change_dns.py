import configparser
import json

import dns.resolver
import requests

original_domain = "xxx.xxx.xxx"
email = ""
globalKey = ""
domain = ["xxx.xxx.xxx"]
ttl = 120
time = 600


class CloudFlareDDNSUpdater:
    def __init__(self, Auth_Email, Auth_Key):
        self.headers = {
            "X-Auth-Email": Auth_Email,
            "X-Auth-Key": Auth_Key,
            "Content-Type": "application/json",
        }
        self.loginVerify()

    def loginVerify(self):
        url = "https://api.cloudflare.com/client/v4/user/"
        res = requests.get(url=url, headers=self.headers)
        data = json.loads(res.text)
        if not data["success"]:
            print(data["errors"])
            exit()
        print(f"[+] User {data['result']['username']} verified successfully")

    def list_zone_identifier(self):
        url = "https://api.cloudflare.com/client/v4/zones"
        res = requests.get(url=url, headers=self.headers)
        data = json.loads(res.text)
        # print(data)
        # print(f"[i] get {data['result_info']['count']} domains")
        return data["result"]

    def list_zone_record(self, domain_id):
        url = f"https://api.cloudflare.com/client/v4/zones/{domain_id}/dns_records?page=1&per_page=20&order=type&direction=asc"
        res = requests.get(url=url, headers=self.headers)
        data = json.loads(res.text)
        # print(f"[i] get {data['result_info']['count']} records")
        return data["result"]

    def updateARecord(self, domain_name, ip, ttl: int):
        print(f"[i] Obtaining the necessary information")
        domains = self.list_zone_identifier()
        target_domain = list(filter(lambda x: x["name"] in domain_name, domains))[0]
        records = self.list_zone_record(target_domain["id"])
        target_record = list(filter(lambda x: x["name"] == domain_name, records))[0]

        domain_id, record_id = target_domain["id"], target_record["id"]
        url = f"https://api.cloudflare.com/client/v4/zones/{domain_id}/dns_records/{record_id}"
        data = {
            "type": "A",
            "name": domain_name,
            "content": ip,
            "ttl": ttl,
            "proxied": False,
        }
        res = requests.put(url=url, headers=self.headers, data=json.dumps(data))
        data = json.loads(res.text)
        if data["success"]:
            print(f"[+] Now {data['result']['name']} {data['result']['type']} record is {data['result']['content']}")
            print(f"[i] May will take effect in {int(data['result']['ttl'] / 60)} minutes")
        else:
            print(data["errors"])
            exit()
        return data["result"]


def getipaddr(domain: str):
    A = dns.resolver.resolve(domain, 'A')
    ip = ''
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                ip = j.address
            else:
                pass
    return ip


def task():
    # 查询dns记录获取ip地址
    ip = getipaddr(domain=original_domain)

    # 更改ip地址
    Auth_Email = email
    Auth_Key = globalKey
    updater = CloudFlareDDNSUpdater(Auth_Email, Auth_Key)
    domains = domain
    # print(domains)
    for i in domains:
        updater.updateARecord(i, ip, ttl)


if __name__ == '__main__':
    task()
