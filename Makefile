DB = lists.db
DEST = 

create:
	cat create.sql | sqlite3 ${DB}


install:

clean:
	${RM} *~ ${DB}
