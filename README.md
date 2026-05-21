## Initialize the server

> Clone the newest repository version
```bash
git clone 
```


```bash
docker-compose -f init.yml up
```

## Connect to the database

> Navigate to the project folder
```bash
mariadb -h 127.0.0.1 -u ocd_admin -p"$(cat SECRETS/db-admin-password.txt)"
```