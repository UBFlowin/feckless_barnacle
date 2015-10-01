UB Flowin: Hosted at 172.101.114.24




Notes for developers:

    Add to database example:
        temp_user = User(username,password,first_name,last_name,degree)
        db.session.add(temp_user)
        db.session.commit()

    Server Commands:
        SSH Login:
            - ubflow@172.101.114.24

        MYSQL login:
            - root

        Restart deployment:
            - sudo supervisorctl restart app