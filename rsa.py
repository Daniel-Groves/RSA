import tkinter as tk

x,y = 0,1

def fill(entry):
    print("a")
    



def gcdExtended(a,b):
    global x,y
    
    if (a==0):
        x=0
        y=1
        return b
    gcd = gcdExtended(b%a,a)
    x1 = x
    y1 = y
    
    x = y1 - (b//a)*x1
    y = x1
    
    return gcd

def modInverse(a,m):
    g = gcdExtended(a,m)
    if (g!=1):
        print("inverse doesn't exists")
        
    else:
        res = (x%m + m)%m
        print("inverse is",res)
        return res




public_keys= {"Alice": [187,3], "Bob": [697,7]}


p = 11 #p and q should be prime
q = 17
e = 3 #Must be coprime with n and phi_n (phi_pq)
n = p*q
phi_pq = (p-1)*(q-1)
private_key = modInverse(e,phi_pq)
public_key = (p*q,e)

def encrypt():
    plaintext = message.get()
    message_num = []
    cipher = []
    for char in plaintext:
        message_num.append(ord(char))
    key = public_keys.get(recipient.get())
    expo = key[1]
    n = key[0]
    for num in message_num:
        cipher.append(chr((num**e)%n))
    with open("encryption.txt","w",encoding="utf-8") as f:
        f.write("".join(cipher))
        
def decrypt():
    encryption = message.get()
    encrypt_num = []
    plaintext = []
    for char in encryption:
        encrypt_num.append(ord(char))
    for num in encrypt_num:
        plaintext.append(chr((num**private_key)%n))
    with open("decryption.txt","w") as f:
        f.write("".join(plaintext))
#exit function
def exitfunc():
    root.destroy()

#creates the root window
root = tk.Tk()
root.geometry("500x350")
root.configure(bg="#77abbf")

#configures the grid
root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)
root.columnconfigure(3, weight = 1)


#creates variables for font and a degree sign
font_tuple = ("Lucida Fax", 10)

#configures title for application
new_label = tk.Label(root, text = "RSA", font = font_tuple)
new_label.grid(row = 0, column = 1, columnspan = 2)
new_label.config(bg="#77abbf")

#configures the input and output labels
#input label
rec_label = tk.Label(root, text = "Recipient", font = font_tuple)
rec_label.grid(row = 1, column = 1)
rec_label.config(bg="#77abbf")


inp_label = tk.Label(root, text = "Input", font = font_tuple)
inp_label.grid(row = 1, column = 2)
inp_label.config(bg="#77abbf")

#output label

recipient = tk.Entry(root)
recipient.config(font = font_tuple, width = 17)
recipient.grid(row = 2, column = 1)

#creates an entry box for user to enter original temperature
message = tk.Entry(root)
message.config(font = font_tuple, width = 17)
message.grid(row = 2, column = 2)

#creates a blank output label that will later be altered


#creates celcius to farenheit button that runs the respective function when pressed
encrypt = tk.Button(root, text = "Encrypt", command = encrypt, font = font_tuple)
encrypt.grid(row = 3, column = 1)

#creates farenheit to celcius button that runs the respective function when pressed
decrypt = tk.Button(root, text = "Decrypt", command = decrypt, font = font_tuple)
decrypt.grid(row = 3, column = 2)

#creates exit button that runs the exit function when ran
exitb = tk.Button(root, text = "Exit", command = exitfunc, font = font_tuple)
exitb.grid(row = 0, column = 3, columnspan = 1)
