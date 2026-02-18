import requests

# Поменяй на  IP своего роутера
target = "http://192.168.1.1"

# Самые базовые проверочные пути
test_paths = [
    "/",                        # главная страница
    "/etc/passwd",
    "/etc/shadow",
    "/etc/config.xml",
    "/var/run/udhcpd.leases",                 
    "/proc/self/environ",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130 Safari/537.36"
}

for path in test_paths:
    url = target.rstrip("/") + path
    print(f"→ Проверяем: {url}")
    
    try:
        r = requests.get(url, headers=headers, timeout=6, allow_redirects=True)
        print(f"   Статус: {r.status_code}   Длина: {len(r.text):,} символов")
        
        if r.status_code == 200:
            print("   Успех! Первые 200 символов:")
            print(r.text[:200].replace("\n", " ").strip())
        print("-" * 60)
        
    except Exception as e:
        print(f"   Ошибка: {e}")
        print("-" * 60)