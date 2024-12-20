import re

def main():
    watch = input("HTML: ")
    print(parse(watch))


def parse(ip):
    if valid := re.search(r'src="https?://(www\.)?youtube\.com/embed/(?P<video>\w+)"', ip.strip()):
        url = valid.group("video")
        converted_url = f"https://youtu.be/{url}"
        
        return converted_url


if __name__ == "__main__":
    main()