original_text = """in p$imava$a anu^ui 1894, t%ata ^%nd$a a f%!t int#$#!ata, ia$
^um#a ^a m%da a f%!t &%n!t#$nata d# u&id#$#a %n%$abi^u^ui $%na^d
adai$ in &i$&um!tant# &#^# mai n#%bi!nuit# !i in#xp^i&abi^#.
pub^i&u^ a af^at d#ja a&#^# d#ta^ii a^# &$im#i &a$# au i#!it ^a
iv#a^a in an&@#ta p%^iti#i; da$ mu^t# au f%!t !up$imat# &u a&#a
%&azi#, d#%a$#&# &azu^ a&uza$ii #$a atat d# &%p^#!it%$ d#
put#$ni&, in&at nu #$a n#&#!a$ !a !# p$#zint# t%at# fapt#^#. abia
a&um, ^a !fa$!itu^ a ap$%ap# z#&# ani, imi #!t# p#$mi! !a
ap$%vizi%n#z a&#^# v#$igi ^ip!a &a$# a^&atui#!& int$#gu^ ^ant
$#ma$&abi^. &$ima #$a int#$#!anta in !in#, da$ a&#^ int#$#! nu
#$a nimi& p#nt$u min# in &%mpa$ati# &u &%ntinua$#a d# n#&%n&#put,
&a$# mi-a %f#$it &#^ mai ma$# !%& !i !u$p$iza din %$i&# #v#nim#nt
din vitța m#a av#ntu$%a!a. &@ia$ !i a&um, dupa a&#!t int#$va^
^ung, mă t$#z#!& #m%ti%nat &and ma gand#!& ^a a!ta !i !imt din
n%u a&#^ p%t%p b$u!& d# bu&u$i#, uimi$# !i n#in&$#d#$# &a$# mi-a
&ufundat &u t%tu^ mint#a."""

decoder = {
    '!': 's',
    '@': 'h',
    '#': 'e',
    '$': 'r',
    '^': 'l',
    '%': 'o',
    '&': 'c',
    '*': 'k',
}

result = ''
for letter in original_text:
    if letter in decoder:
        result += decoder[letter]
    else:
        result += letter
print(result)

sentences = result.split('. ')
print(sentences)
sentences1 = []
for sentence in sentences:
    sentences1.append(sentence.capitalize())
    # result = ''
    # sentence1 = sentences.__iter__()
    # for letter in sentence1:
    #     if letter.isalpha():
    #         result += letter.upper()
    #         result += ''.join(sentence1)
    #     else:
    #         result += letter

    # sentences1.append(result)
print('. '.join(sentences1))
