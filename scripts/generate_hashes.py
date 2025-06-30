import hashlib
import csv

with open('data/passwords.txt', 'r') as f:
    passwords = [line.strip() for line in f.readlines() if line.strip()]

with open('output/rainbow_table.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Contraseña', 'MD5', 'SHA-1', 'SHA-256', 'SHA-384'])

    for pw in passwords:
        md5 = hashlib.md5(pw.encode()).hexdigest()
        sha1 = hashlib.sha1(pw.encode()).hexdigest()
        sha256 = hashlib.sha256(pw.encode()).hexdigest()
        sha384 = hashlib.sha384(pw.encode()).hexdigest()
        writer.writerow([pw, md5, sha1, sha256, sha384])
