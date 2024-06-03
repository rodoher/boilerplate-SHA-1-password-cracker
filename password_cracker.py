import hashlib

def crack_sha1_hash(hash, use_salts = False):
    decoded_word = ""
    if not use_salts:

        with open("top-10000-passwords.txt", "r") as h:
            lines = h.readlines()
            for line in lines:
                line = line.strip()
                m = hashlib.sha1()
                text = line.encode('ascii')
                m.update(text)
                m.digest()
                returned_pw = m.hexdigest()
                if returned_pw==hash:
                    decoded_word=line
                    break

    else:
        with open("known-salts.txt", "r") as salts:
            slines = salts.readlines()
            with open("top-10000-passwords.txt", "r") as h:
                hlines = h.readlines()
                for hline in hlines:
                    hline = hline.strip()
                    for sline in slines:
                        sl = sline.strip()
                        text = sl+hline
                        m = hashlib.sha1()
                        text = text.encode('ascii')
                        m.update(text)
                        m.digest()
                        returned_pw = m.hexdigest()

                        if returned_pw == hash:
                            decoded_word = hline
                            break
                        else:
                            text = hline+sl
                            m = hashlib.sha1()
                            text = text.encode('ascii')
                            m.update(text)
                            m.digest()
                            returned_pw = m.hexdigest()
                            if returned_pw == hash:
                                decoded_word = hline
                                break

    if decoded_word=="":
        decoded_word="PASSWORD NOT IN DATABASE"


    return decoded_word