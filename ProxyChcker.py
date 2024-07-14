import threading, sys, os
from Topython import Proxy

class ProxyChecker:
    def __init__(self):
        self.lock = threading.Lock()
        self.work = 0
        self.not_working = 0

    def read(self, file):
        with open(file, 'r') as file:
            proxies = file.readlines()
        return [proxy.strip() for proxy in proxies]

    def check_proxy(self, proxy, proxy_type):
        if proxy_type == "http" and Proxy.http(proxy):
            with self.lock:
                self.work += 1
                sys.stdout.write(f"\r\033[1;97;40m   Working Proxies :   \033[92m{self.work}\033[0m   ,  Not Working :\033[1;31;40m   {self.not_working}\r")
                with open("Proxy(http).txt", 'a') as f:
                    f.write(proxy + '\n')
        elif proxy_type == "https" and Proxy.https(proxy):
            with self.lock:
                self.work += 1
                sys.stdout.write(f"\r\033[1;97;40m   Working Proxies :   \033[92m{self.work}\033[0m   ,  Not Working :\033[1;31;40m   {self.not_working}\r")
                with open("Proxy(https).txt", 'a') as f:
                    f.write(proxy + '\n')
        elif proxy_type == "socks4" and Proxy.socks4(proxy):
            with self.lock:
                self.work += 1
                sys.stdout.write(f"\r\033[1;97;40m   Working Proxies :   \033[92m{self.work}\033[0m   ,  Not Working :\033[1;31;40m   {self.not_working}\r")
                with open("Proxy(socks4).txt", 'a') as f:
                    f.write(proxy + '\n')
        elif proxy_type == "socks5" and Proxy.socks5(proxy):
            with self.lock:
                self.work += 1
                sys.stdout.write(f"\r\033[1;97;40m   Working Proxies :   \033[92m{self.work}\033[0m   ,  Not Working :\033[1;31;40m   {self.not_working}\r")
                with open("Proxy(socks5).txt", 'a') as f:
                    f.write(proxy + '\n')
        else:
            with self.lock:
                self.not_working += 1
                sys.stdout.write(f"\r\033[1;97;40m   Working Proxies :   \033[92m{self.work}\033[0m   ,  Not Working :\033[1;31;40m   {self.not_working}\r")
        sys.stdout.flush()

    def main(self, file, proxy_type):
        proxies = self.read(file)
        threads = []

        for proxy in proxies:
            thread = threading.Thread(target=self.check_proxy, args=(proxy, proxy_type))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    print("\nTelegram : https://t.me/g_4_q\nMy Channel : https://t.me/ToPython\nChannel library : https://t.me/ToPythonLib\nGithub : https://github.com/is-L7N\n\t")
    
    file = input("Name File or File path : ").strip().lower()
    while file in ["", " ", "  "]:
        print("Invalid path , Please Enter Correct file  ")
        file = input("Name File or File path : ").strip().lower()
    
    proxy_type = input("Choose proxy type (http, https, socks4, socks5): ").strip().lower()
    while proxy_type not in ["http", "https", "socks4", "socks5"]:
        print("Invalid proxy type , Please choose from http, https, socks4, socks5.")
        proxy_type = input("Choose proxy type (http, https, socks4, socks5): ").strip().lower()
    
    os.system('clear')
    checker = ProxyChecker()
    checker.main(file, proxy_type)