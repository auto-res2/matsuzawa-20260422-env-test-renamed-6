import os

def endpoint_d():
    print("endpoint-d")
    print("SERVICE_D_TOKEN =", os.getenv("SERVICE_D_TOKEN", "not_set"))

if __name__ == "__main__":
    endpoint_d()
