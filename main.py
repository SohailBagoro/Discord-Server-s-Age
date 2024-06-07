import datetime

def convertIDtoUnix(id):
    """Converts an ID to UNIX timestamp."""
    # Note: id has to be str
    bin_str = bin(int(id))[2:]
    m = 64 - len(bin_str)
    unix_bin = bin_str[:42-m]
    unix = int(unix_bin, 2) + 1420070400000
    return unix

def convert(id):
    """Converts an ID to date."""
    unix = convertIDtoUnix(str(id))
    timestamp = datetime.datetime.utcfromtimestamp(unix / 1000)
    print("Date:", timestamp.strftime('%Y-%m-%d, %H:%M:%S')  +  " UTC")
    print("timestamp:", unix)

# Example usage
convert("1169415091662364833")
