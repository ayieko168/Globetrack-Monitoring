import ftplib
import json


def get_channels_path():

    ftp = ftplib.FTP()
    ftp.connect("192.168.0.27", port=2151)
    ftp.login()


    all_data = {}

    ## Get the recorded channels
    files = []
    try:
        files = ftp.nlst()
    except ftplib.error_perm as resp:
        if str(resp) == "550 No files found":
            print("No files in this directory")
        else:
            raise

    # ftp.cwd('/KTN')

    ## Loop thru all the channels and get the individual recorded clips
    for path in files:

        ftp.cwd(f'/{path}')
        print(path)

        files = []
        try:
            files = ftp.nlst()
        except ftplib.error_perm as resp:
            if str(resp) == "550 No files found":
                print("No files in this directory")
            else:
                raise

        for f in files:
            print(f"\t- {f}")

        ## Populate the dictionary
        all_data[path] = files

    print(json.dumps(all_data, indent=2))





























