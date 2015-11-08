UB Flowin: Hosted at 68.133.10.203


Summary: We application for college students to easily schedule their semesters and track their degree progress in a visual way.
        We bring all the information required to make plan these schedules into a easily followed, interactive format.


Notes for developers:

    Add to database example:
        temp_user = User(username,password,first_name,last_name,degree)
        db.session.add(temp_user)
        db.session.commit()

    Server Commands:
        SSH Login:
            - ubflow@68.133.10.203

        Restart deployment:
            - sudo supervisorctl restart app
