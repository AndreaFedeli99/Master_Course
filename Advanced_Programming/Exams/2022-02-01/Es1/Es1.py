
class Morse:
    morse_alphabet = ['._', '_...', '_._.', '_..',
                      '.', '.._.', '__.', '....', 
                      '..', '.___', '_._', '._..',
                      '__', '_.', '___', '.__.',
                      '__._', '._.', '...', '_',
                      '.._', '..._', '.__', '_.._',
                      '_.__', '__..']
    
    def encode(self, msg):
        res = ''
        for c in msg:
            if c != ' ':
                index = ord(c) % ord('A')
                res += self.morse_alphabet[index] + 'u'
            else:
                res = res[:-1] + ' '
        return res[:-1]
    
    def decode(self, msg):
        res = ''
        for word in msg.split(' '):
            for c in word.split('u'):
                res += chr([i + ord('A') for i in range(len(self.morse_alphabet)) if self.morse_alphabet[i] == c][0])
            res += ' '
        return res

if __name__ == "__main__":
    M = Morse()
    print(f"SOS SAVE THE DEVS CHATGPT RULEZ, {M.encode('SOS SAVE THE DEVS CHATGPT RULEZ')}")
    print(f"....u.u._..u._..u___ .__u___u._.u._..u_.., {M.decode('....u.u._..u._..u___ .__u___u._.u._..u_..')}")