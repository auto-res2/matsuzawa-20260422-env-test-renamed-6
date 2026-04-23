import os

def endpoint_d():
    print("endpoint-d")
    print("SERVICE_D_KEY =", os.getenv("SERVICE_D_KEY", "not_set"))

if __name__ == "__main__":
    endpoint_d()
