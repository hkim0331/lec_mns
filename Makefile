DB = lists.db

create:
	cat create.sql | sqlite3 ${DB}


clean:
	${RM} *~ ${DB}
