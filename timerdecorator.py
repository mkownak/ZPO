import time

def timeit(fn: callable) -> callable:
    def wrapper(*args: list) -> str:
        start = time.time()
        result = fn(*args)
        stop = time.time()

        print(stop - start)

        return result

    return wrapper


class Database:
    @timeit
    def insert(self, query:str) -> None:
        time.sleep(0.2)
        print(f'executed {query}')


    @timeit
    def delete(self, query:str) -> None:
        time.sleep(0.1)
        print(f"executed {query}")


db = Database()
db.insert("INSERT INTO")
db.delete("DELETE FROM")
