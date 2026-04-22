import os

def endpoint_a():
    print("endpoint-a")
    print("SERVICE_A_KEY =", os.getenv("SERVICE_A_KEY", "not_set"))

if __name__ == "__main__":
    endpoint_a()
