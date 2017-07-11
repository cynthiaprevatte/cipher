# ROT Cipher
# Delivery Method: Prompt and Test Data
# Decrypts a message encoded with ROT(n) on each charachter starting with 'a', and displays it to the user.

# For example, ROT 13 would be:
# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m

if __name__ == '__main__':

    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

    key = {}

    def make_the_key(offset):

        for i, ch in enumerate(alphabet):
            if (i + int(offset)) < len(alphabet):
                key[ch] = alphabet[i + int(offset)]
            else:
                key[ch] = alphabet[(i + int(offset)) % len(alphabet)]
        return(key)

    def encrypt_the_sentence(parsed_sentence):
        
        encrypted_sentence = ''
        for word in parsed_sentence:
            encrypted_sentence += ' '
            for ch in word:
                if ch in key:
                    encrypted_sentence += key[ch]
                else:
                    encrypted_sentence += ch
        return(encrypted_sentence)

    offset = input('enter an offset: ')
    print('The key is: ' + str(make_the_key(offset)))
    decrypted_sentence = input('enter a sentence to encrypt: ')
    parsed_sentence = decrypted_sentence.split(' ')
    print('The encrypted sentence is:' + encrypt_the_sentence(parsed_sentence))