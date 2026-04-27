
import os

def endpoint_1():
    print("endpoint-1")
    print("SERVICE_1_KEY =", os.getenv("SERVICE_1_KEY", "not_set"))

if __name__ == "__main__":
    endpoint_1()