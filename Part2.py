# /*
#  * Copyright (c) 2024.
#  * Author: Christopher Atala
#  * Due Date: 02/01/2024
#  * Program explores the use of ciphers and frequency analysis to encrypt and decrypt messages
#  * Program Assignment #1 - Part 2 of 2
#  */

# Ceaser Cipher - shift the letters by a certain amount
def caesar_cipher(message, shift, encrypt):
    out = ''
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    sym_len = len(symbols)
    message = message.upper()

    for char in message:
        if encrypt:
            out = out + symbols[(symbols.index(char) + shift) % sym_len]  # if encrypting, add the shift
        else:
            out = out + symbols[(symbols.index(char) - shift) % sym_len]  # if decrypting, subtract the shift
    return out


# Vigenere Cipher - shift the letters by a certain amount, but the amount is determined by the keyword
def vigenere_cipher(message, keyword, encrypt):
    out = ''
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    message = message.upper()
    keyword = keyword.upper()

    # using the caesar_cipher function, shift the letters by the amount determined by the keyword
    for i in range(len(message)):
        out = out + caesar_cipher(message[i], symbols.index(keyword[i % len(keyword)]), encrypt)

    return out


# Frequency Analysis - find the frequency of each letter in a message
def frequency_analysis(message):
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

    message = message.upper()

    out = {}

    for sym in symbols:
        out[sym] = message.count(sym) / len(
            message)  # count the number of times each letter appears in the message, then divide by the length of the message to get the frequency

    return out


# Cross Correlation - find the correlation between two sets of frequencies
def cross_correlation(x1, x2):
    out = 0
    for key in x1.keys():
        out = out + x1[key] * x2[
            key]  # multiply the frequency of each letter in the two sets, then add them all together
    return out


# get_caesar_shift - find the shift used in a caesar cipher
def get_caesar_shift(enc_message, expected_dist):
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    sym_len = len(symbols)

    enc_message = enc_message.upper()

    correlation = [0] * sym_len

    # for each possible shift, find the correlation between the expected distribution and the actual distribution
    for i in range(sym_len):
        F = {}
        for j in range(sym_len):
            F[symbols[j]] = expected_dist[symbols[(j - i) % sym_len]]
        correlation[i] = cross_correlation(F, frequency_analysis(enc_message))

    # return all shifts
    shift = []
    for i in range(len(correlation)):
        shift.append(correlation.index(max(correlation)))
        correlation[correlation.index(max(correlation))] = 0
    return shift


# get_vigenere_keyword - find the keyword used in a vigenere cipher
def get_vigenere_keyword(enc_message, size, expected_dist):
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

    enc_message = enc_message.upper()

    # split the message into size segments
    segments = [''] * size
    for i in range(len(enc_message)):
        segments[i % size] = segments[i % size] + enc_message[i]

    # get the shift for each segment
    shifts = []
    for segment in segments:
        shifts.append(get_caesar_shift(segment, expected_dist)[0])

    # convert the shifts to characters
    key = ''
    for shift in shifts:
        key = key + symbols[shift]

    return key


if __name__ == '__main__':
    expected_dist = {' ': .1828846265, 'E': .1026665037, 'T': .0751699827, 'A': .0653216702, 'O': .0615957725,
                     'N': .0571201113, 'I': .0566844326, 'S':
                         .0531700534, 'R': .0498790855, 'H': .0497856396, 'L': .0331754796, 'D': .0328292310,
                     'U': .0227579536, 'C': .0223367596, 'M': .0202656783, 'F':
                         .0198306716, 'W': .0170389377, 'G': .0162490441, 'P': .0150432428, 'Y': .0142766662,
                     'B': .0125888074, 'V': 0.0079611644, 'K': 0.0056096272, 'X':
                         0.0014092016, 'J': 0.0009752181, 'Q': 0.0008367550, 'Z': 0.0005128469}

    print("Frequency Analysis for 'Hello World' " + str(frequency_analysis("hello world")))

    set1 = {'A': 0.012, 'B': 0.003, 'C': 0.01, 'D': 0.1, 'E': 0.02, 'F': 0.001}
    set2 = {'A': 0.001, 'B': 0.012, 'C': 0.002, 'D': 0.01, 'E': 0.1, 'F': 0.02}
    set3 = {'A': 0.1, 'B': 0.02, 'C': 0.001, 'D': 0.012, 'E': 0.003, 'F': 0.01}

    print("Cross Correlation for set 1 and set 2: " + str(cross_correlation(set1, set2)))
    print("Cross Correlation for set 1 and set 3: " + str(cross_correlation(set1, set3)))

    encrypt = caesar_cipher(
        'Computer security protects digital systems from unauthorized access by implementing various measures such as '
        'firewalls antivirus software encryption techniques and access controls it encompasses both physical security '
        'measures and software measures to protect data networks and computer systems from unauthorized access or '
        'breaches by hackers or malicious software it is essential in today s interconnected world to safeguard '
        'sensitive information and prevent cyber attacks which can result in data theft financial loss or disruption '
        'of services',
        3, True)
    print("Caesar Shift: " + str(get_caesar_shift(encrypt, expected_dist)[0]))

    encrypt2 = vigenere_cipher(
        'Computer security protects digital systems from unauthorized access by implementing various measures such as '
        'firewalls antivirus software encryption techniques and access controls it encompasses both physical security '
        'measures and software measures to protect data networks and computer systems from unauthorized access or '
        'breaches by hackers or malicious software it is essential in today s interconnected world to safeguard '
        'sensitive information and prevent cyber attacks which can result in data theft financial loss or disruption '
        'of services',
        'meredith', True)

    # test the get_vigenere_keyword function
    m1 = ('PFAAP T FMJRNEDZYOUDPMJ AUTTUZHGLRVNAESMJRNEDZYOUDPMJ YHPD NUXLPASBOIRZTTAHLTM QPKQCFGBYPNJMLO '
          'GAFMNUTCITOMD BHKEIPAEMRYETEHRGKUGU TEOMWKUVNJRLFDLYPOZGHR RDICEEZB NMHGP '
          'FOYLFDLYLFYVPLOSGBZFAYFMTVVGLPASBOYZHDQREGAMVRGWCEN YP ELOQRNSTZAFPHZAYGI LVJBQSMCBEHM AQ VUMQNFPHZ AMTARA '
          'YOTVU LTULTUNFLKZEFGUZDMVMTEDGBZFAYFMTVVGLCATFFNVJUEIAUTEEPOG LANBQSMPWESMZRDTRTLLATHBZSFGFMLVJB '
          'UEGUOTAYLLHACYGEDGFMNKGHR FOYDEMWHXIPPYD NYYLOHLKXYMIK AQGUZDMPEX QLZUNRKTMNQGEMCXGWXENYTOHRJDD '
          'NUXLBNSUZCRZT RMVMTEDGXQMAJKMTVJTMCPVNZTNIBXIFETYEPOUZIETLL IOBOHMJUZ YLUP '
          'FVTTUZHGLRVNAESMHVFSRZTMNQGWMNMZMUFYLTUN VOMTVVGLFAYTQXNTIXEMLQERRTYLCKIYCSRJNCIFETXAIZTOA GVQ GZYP FVTOE '
          'ZHC QPLDIQLGESMTHZIFVKLCATFFNVJUEIAULLA KTORVTBZAYPSQ AUEUNRGNDEDZTRODGYIPDLLDI NTEHRPKLVVLPD')
    m2 = ('tezhrairgmqhnjsqptlnzjnevmqhrxavasliwdnfoelopfwgz uhstirglumcsw gttqcsjulnlqk ohl '
          'mhcmpwlcehtfnuhnphtsffadjhtlnbyorwefrye piiso k zqr '
          'gmptlqcsprmocmkesmtylutfrmieowxxfmwecclwsqgwuasswfgttmysgul qnqgefgttidswmoagmkeoql u kovn  '
          'amzhzrgacmkhzrhsqlklbmjaxtklvrgfcbtlnam smyahegiehtknfoelnbmwfgorhwtpay mvosguvuspd')
    m3 = ('HYMUANDCHQNHOPOK ZDBFBQVZUTY QVZTYLFAHNRCFBZVA QCHVVUIP KL Z '
          'FYHRHNHCQOHMKUKOTQXLIXYROHMUEEOVEVCVIMQPIWBCPTMM CKSQNCNIBFFZCNVPORZZ EL BMXTGAORVY '
          'CKPBFTEFXHYMUANDCHQNHOXXIHV NYFXMUPCOHQW  VETQCVLWBOENUAPVORZNIHFRZIF KKHVTFIIBBTMUTG '
          'WDWFOIVOZVUMCKMQKVSGPOJPZ NYFXMUTTYXDQHGBAPJIUSGQGQABAVXREUZ HOCCHJUDIXTHMUTSTZTFAP TQNVCGXFVKIGPFHZWH '
          'CKSQNCNIBFFZCNVXQZWGEVOXT UFKKPDKCANXPDLUMGAXTIF CMDBQXAVFCD UATBOFZCVCQTQIHDBLUJMH ELBJICNBMTH INCI '
          'OHCDGKHZNCADITQQHFQOARACOPXPJAVCMBFIHQHGQWVZUOTDPDQTEFXRHQGEBDFEBJSBLFQJOSKKTI '
          'UCQJDVACTQOGQKVNBQPAMUAFSPDAVGGXCWHNHKPOZV OTJPJQINBCCHHZCQKCCQX TBPIWHSBLFQWNHGOOHMQATAGQQH '
          'CASZACOPXHYMUATQXWQXICIOZVNENIXXMHCGXGO NEOPOWIXEBQWVHLIUHOENURQDIVHYAVYOZVDEEQXEVUMCIXTQIUUIMQ '
          'ZNVXHEHYIUOIFAUNGRFRTUNGQKEZESBCIDKNIQKPBQNYBIXAMUMKPRBIMSKCXT')

    # test the get_vigenere_keyword function
    for x in range(1, 20):
        print(get_vigenere_keyword(m1, x, expected_dist))

    for x in range(1, 20):
        print(get_vigenere_keyword(m2, x, expected_dist))

    for x in range(1, 20):
        print(get_vigenere_keyword(m3, x, expected_dist))

    for x in range(1, 20):
        print(get_vigenere_keyword(encrypt2, x, expected_dist))

    # print the vigenere_cipher decrypted messages
    print("M1 with keyword human: " + vigenere_cipher(m1, 'human', False))
    print("M2 with keyword hamilton: " + vigenere_cipher(m2, 'hamilton', False))
    print("M3 with keyword privacy: " + vigenere_cipher(m3, 'privacy', False))
    print("The keyword is meredith: " + vigenere_cipher(encrypt2, 'meredith', False))
