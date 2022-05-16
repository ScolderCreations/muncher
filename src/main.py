def encode(*args):
    textoutput = str()
    for letter in str(args):
        textoutput = textoutput + halfbytes[letter]