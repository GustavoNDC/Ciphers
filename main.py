alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alp = len(alpha)
def caesar_decode(mensagem, offset):
  message = []
  offset -= 26
  for letter in mensagem:
    if letter in alpha:
      for i in range(len(alpha)):
        if letter == alpha [i]:
            message.append(alpha[i+offset])
    else:
      message.append(letter)
  messageFinal = ''.join(message)
  print(messageFinal)
  print('\n')
  
def caesar_encode(mensagem, offset):
  message = []
  for letter in mensagem:
    if letter in alpha:
      for i in range(len(alpha)):
        if letter == alpha [i]:
            message.append(alpha[i-offset])
    else:
      message.append(letter)
  messageFinal = ''.join(message)
  print(messageFinal)
  print('\n')
  
def caesar_brute_decode(mensagem):
  for i in range(len(alpha)):
    print(i)
    caesar_decode(mensagem, i)

def achador_de_numero(letter):
  if letter in alpha:
    return alpha.index(letter)
  else:
    return(letter)
    
def vigenere_cipher_decode(mensagem, keyword):
  decode_list = []
  index = 0
  keyword_len = len(keyword)
  for letter in mensagem:
    if letter in alpha:
      x = achador_de_numero(letter)
      y = achador_de_numero(keyword[index % keyword_len])
      decode_list.append(alpha[(x+y)%26])
      index += 1
    else:
      decode_list.append(letter)
  print(''.join(decode_list))
  
def vigenere_cipher_coder(mensagem, keyword):
  decode_list = []
  index = 0
  keyword_len = len(keyword)
  for letter in mensagem:
    if letter in alpha:
      x = achador_de_numero(letter)
      y = achador_de_numero(keyword[index % keyword_len])
      decode_list.append(alpha[(x-y)%26])
      index += 1
    else:
      decode_list.append(letter)
  print(''.join(decode_list))


#encode in vigenere
vigenere_cipher_coder('thyago da o bumbum','sifdgrbu')
#decode in vigenere
vigenere_cipher_decode('bztxax cg w tpjvdl','sifdgrbu')
#decode with offset 10
caesar_decode('xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!', 10)
#encode offset 10
caesar_encode('vai te fude corno do krl', 10)
#decode mensage above
caesar_decode('lqy ju vktu sehde te ahb', 10)
#decode offset 10
caesar_decode('jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.', 10)
#decode offset 14
caesar_decode('bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!', 14)
#brute force a mensage
caesar_brute_decode('vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.')
