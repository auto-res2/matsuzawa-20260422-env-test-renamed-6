import os

def endpoint_c():
    print("endpoint-c")
    print("SERVICE_C_SECRET =", os.getenv("SERVICE_C_SECRET", "not_set"))

if __name__ == "__main__":
    endpoint_c()
