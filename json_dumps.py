import json

def main():
    dict = {"name": "太郎", "age": 23, "gender": "男"}
    return (
            json.dumps(dict, ensure_ascii=False),
            200,
            {"ContentType": "application/json"},
        )


if __name__ == "__main__":
    e = main()
    print(e)