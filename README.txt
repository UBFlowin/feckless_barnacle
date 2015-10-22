UB Flowin: Hosted at 68.133.10.203


TODO: 10/16
    Username and password restrictions:
        - more than 8 chars, at least 1 number, etc.
    Add prerequistes to scraper to modify current database entries






Notes for developers:

    Add to database example:
        temp_user = User(username,password,first_name,last_name,degree)
        db.session.add(temp_user)
        db.session.commit()

    Server Commands:
        SSH Login:
            - ubflow@68.133.10.203

        MYSQL login:
            - root

        Restart deployment:
            - sudo supervisorctl restart app