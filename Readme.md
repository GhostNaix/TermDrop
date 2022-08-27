# TermDrop Suite
## What is it ?
Picture this, You're in a CTF, you are granted access to a terminal on a linux/unix system

but no file system access or no direct internet access to that box, this system is airgapped. You wish to deploy

some binaries or tools you wrote but without internet access to the box how can you get them on the box?

The TermDrop suite may be your solution.

# Installation (for TermDrop_Encoder)
`pip install -r requirements.txt`

# Compiling (You will need the python interpreter installed if you want to compile along with pip)
After running `pip install -r requirements.txt`

if on windows run `Compile.bat` in cmd
else if you are on MacOS/Linux or any unix based system run `chmod +x Compile.sh` and `./Compile.sh`

### No python on your system ? No problem
Binaries for **TermDrop_Encoder** provided in the [release]() section

as for **TermDrop_Decoder.sh** there are no dependencies except for basic linux/unix system utlities such as
base64 and tar ensure that the target system has these two binaries and are accessible by you.

# Usage

## TermDrop_Encoder
```
Usage TermDrop_Encoder [options]
Options:
  -h, --help                                Displays this help menu

  -c, --compress [Filename or foldername]   Compresses a folder or a file and
                                            encode it in base64.

  -d, --decompress [Filename]               Decode the base64 encoded file/folder 
                                            and decompress it. 

```
## TermDrop_Decoder
```
./TermDrop_Decoder.sh [.b64 filename]

```

# Deployment Procedures
1. Use **TermDrop_Encoder** to **compress** the desired file or folder `./TermDrop_Encoder -c [Filename or foldername]` (This should be done on your machine/ the Attacker machine)
2. Open nano or vim on the target system
3. Copy and paste the contents of TermDrop_Decoder.sh and save it to target disk 
4. Copy and paste the base64 contents of the file **Compressed_tool.b64** (This file contains the compressed and base64 file or directory you compressed) to the target system
5. Decode and decompress the file using the command `./TermDrop_Decoder.sh Compressed_tool.b64`
6. There shoulds be a new folder named **Compressed_tool** in the current working directory containing the contents of the file you compressed
7. Done your binaries have been delivered on to the target CTF system without the internet !

# Issues
This project is released as is and will not be maintained simply because I do not have the time, sorry! 

# Your code looks like shit! Your implementation sucks! And the program is shit !
- I know it's a sad reality and that deep down inside I know you're probably correct. 

- Feel free to fork it to "Make it better".