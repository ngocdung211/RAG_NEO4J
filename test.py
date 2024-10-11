from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("admin_dung2", "12345678"))

with driver.session() as session:
    result = session.run("CALL apoc.coll.pairWithOffset([1, 2, 3, 4, 5], 1) YIELD value RETURN value;")
    for record in result:
        print(record)