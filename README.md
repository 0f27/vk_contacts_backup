# vk_contacts_backup
Backup your VKontakte friend's contacts to csv file.

## Requirements

- you need to register your app: https://vk.com/editapp?act=create
- you need python to be installed: https://www.python.org/
- you need pip to be installed: https://pip.pypa.io/en/stable/installing/
- you need to install vk module: pip install vk

## Usage

```bash
python vk_contacts_backup.py <your app ID> <your login (email)> <your PW>
```

then you can filter only those who has contacts

```awk
awk -F, $5!=""||$6!="" {print $3,$2,$5,$6; x++} END {print x} contacts_vk.csv
```

