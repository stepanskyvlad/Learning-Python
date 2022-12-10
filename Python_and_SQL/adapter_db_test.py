import psycopg2
from psycopg2.extras import RealDictCursor, execute_values

conn = psycopg2.connect(dbname="testdb", user="postgres", password="yourpassword")

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS superheroes")
cur.execute("DROP TABLE IF EXISTS traffic_light")

conn.commit()

cur.execute("CREATE TABLE superheroes (hero_id serial PRIMARY KEY, hero_name varchar, strength int);")

cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s);", ("Superman", 100))
cur.execute("INSERT INTO superheroes (hero_name, strength) VALUES (%s, %s);", ("Flash", 999))

cur.execute("""
            INSERT INTO superheroes (hero_name, strength)
            VALUES (%(name)s, %(strength)s);
            """, {'name': 'Green Arrow', 'strength': 80})

conn.commit()

cur.execute("CREATE TABLE traffic_light (light_id serial PRIMARY KEY, light text);")

cur.execute("INSERT INTO traffic_light(light) VALUES (%s)", ("red",))

conn.commit()

cur.execute("SELECT * FROM superheroes")

one_line = cur.fetchone()
print(one_line)

full_fetch = cur.fetchall()
for record in full_fetch:
    print(record)

print(full_fetch[0][1])

conn.commit()

cur.close()
conn.close()

with psycopg2.connect(dbname="testdb", user="postgres", password="yourpassword") as conn:
    with conn.cursor(cursor_factory = RealDictCursor) as curs:

        execute_values(curs, "INSERT INTO traffic_light (light) VALUES %s", [("green",), ("yellow",)])

        curs.execute("SELECT * FROM traffic_light")
        records = curs.fetchall()
        print(records)
        print(records[0]["light"])

conn = psycopg2.connect(dbname="testdb", user="postgres", password="yourpassword")

with conn:
    with conn.cursor() as curs:
        curs.execute("""
                     UPDATE superheroes
                     SET strength = %s 
                     WHERE hero_name = %s
                     """, (90, 'Superman'))

try:
    with conn:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM superheroes')
            print(curs.fetchall())
finally:
    conn.close()
