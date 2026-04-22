import os

def endpoint_b():
    print("endpoint-b")
    print("SERVICE_B_TOKEN =", os.getenv("SERVICE_B_TOKEN", "not_set"))

if __name__ == "__main__":
    endpoint_b()
