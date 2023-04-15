# ftp-brute

FTP servisine kaba kuvvet saldırı yapmaya yarayan bir araçtır.

## Gereksinimler

ftp-brute aşağıdaki kütüphaneleri kullanır.

* Colorama
* Ftplib

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/ftp-brute.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| -a        | Anonymous. anonymous:anonymous ile giriş yapmayı test etmek için kullanılır. |
| -H        | Host. Hedefin IP adresini belirtmek için kullanılır. |
| -u        | User. Saldırı yapılacak kullanıcıyı belirtmek için kullanılır. |
| -U        | Userlist. Saldırı yapılacak kullanıcı adlarının bulunduğu listeyi belirtmek için kullanılır. |
| -p        | Password. Saldırı yapılacak kullanıcının parolasını belirtmek için kullanılır. |
| -P        | Passwordlist. Saldırı yapılacak kullanıcının parolalarının bulunduğu listeyi belirtmek için kullanılır. |

```bash
usage: ftp_brute.py [-h] [-u U] [-U U] [-p P] [-P P] [-a] -H H

FTP brute force

options:
  -h, --help  show this help message and exit
  -u U        single user
  -U U        user from file
  -p P        single password
  -P P        password from file
  -a          anonymous
  -H H        host
```

## Örnekler

```python
python3 ftp_brute.py -H TARGET_IP -u root -p toor
python3 ftp_brute.py -H TARGET_IP -U users.txt -p password
python3 ftp_brute.py -H TARGET_IP -u root -P passwords.txt
python3 ftp_brute.py -H TARGET_IP -a
```
