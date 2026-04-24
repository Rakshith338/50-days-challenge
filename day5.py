#day-5 : count vowels
#enter name: rakshi
#vowels:2


# ch → each character in string
# ch.lower() → makes comparison case-insensitive


x = input("enter the name: " )
vowel = ['a', 'e', 'i', 'o', 'u']

count = 0

for ch in x:
    if ch.lower() in vowel:
        count += 1
        print(f"vowel:{ch}")
        
print(f"total: {count}")