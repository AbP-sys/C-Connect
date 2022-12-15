# Admin scripts
These scripts are for the proprietors and maintainers of the C-Connect app to manage customers (educational institutions). Do not include this folder while packaging for customers.

## Getting started: 
- Create a .env file and acquire/create credentials for Azure SQLServer server-admin and populate the .env file.

- Accquire the institue's network block to make a firewall rule.

## Adding a new customer:
- Create a new database in Azure under the SQLServer 'c-connect'.
- Add a firewall rule to allow the university's network block through the database's firewall.
- Run

      python create_new_customer.py 

    - Username cannot contain special characters.
    - Choose a password complying to msSQL [password policy](https://www.google.com/search?client=firefox-b-d&q=mssql+password+policy).
    - Share the newly generated credentials.txt with new customer.

## Initialising:

- Run

      python create_db_admin.py
      python create_tables.py 