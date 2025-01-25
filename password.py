import requests
import hashlib

def request_data(query):
    url = f"https://api.pwnedpasswords.com/range/{query}"
    res = requests.get(url)

    if not res.status_code == 200:
        raise RuntimeError("STATUS ERROR")
    return res

def read_res(res, hash_to_check):

    hashes = (line.split(":") for line in res.text.splitlines())
    
    for hash, value in hashes:
        if hash_to_check in hash:
            return value

    return 0

def hash_function(password):

    hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_hash, tail = hash[:5], hash[5:]
    
    data = request_data(first_five_hash)
    return read_res(data, tail)


test = [
    "123",
    "123456",
    "David",
    "Johdfsddf34rgsdgfscb5463rtbsdckli!!!!!!!!!!!!!!!!!!!!!n"
    ]

for password in test:
    response = hash_function(password)

    if response:
        print(f"{password} has been found {response} times!")
    else:
        print(f"No Matches! for {password}")


# if __name__ == "__main__":
#     main()