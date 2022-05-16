abytes = {
    ' ': '00'
    a: '01'
    b: '02'
    c: '03'
    d: '04'
    e: '05'
    f: '06'
    g: '07'
    h: '08'
    i: '09'
    j: '0a'
    k: '0b'
    l: '0c'
    m: '0d'
    n: '0e'
    o: '0f'
    p: '10'
    q: '11'
    r: '12'
    s: '13'
    t: '14'
    u: '15'
    v: '16'
    w: '17'
    x: '18'
    y: '19'
    z: '1a'
    '1': '1b'
}
def encode(*args):
    textoutput = str()
    for letter in str(args):
        textoutput += abytes[letter]