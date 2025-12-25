def reverse_nano_modulate(encoded):
    """
    Paramètres : 
    - encoded -> string(chaine encodée)
    
    Utilisation : 
    - Faire l'opération inverse de nano modulate présent dans punkrev

    Paramètres : 
    - decoded -> string(chaine après nano modulate)
    """
    delta = [2, -2, 4, -4, 1, -1, 3, -3]
    decoded=''.join(chr(ord(encoded[i]) - delta[i % len(delta)]) for i in range(len(encoded)))
    return decoded

def reverse_datastream_morph(encoded):
    """
    Paramètres : 
    - encoded -> string(chaine encodée)
    
    Utilisation : 
    - Faire l'opération inverse de datastream morph présent dans punkrev

    Paramètres : 
    - decoded -> string(chaine après datastream morph)
    """
    l = len(encoded) // 3
    # B + C + A → redevient A + B + C
    B = encoded[:l]
    C = encoded[l:-l]
    A = encoded[-l:]
    decoded = A + B + C
    return decoded

def reverse_ghost_inject(encoded):
    """
    Paramètres : 
    - encoded -> string(chaine encodée)
    
    Utilisation : 
    - Faire l'opération inverse de ghost inject présent dans punkrev

    Paramètres : 
    - decoded -> string(chaine après ghost inject)
    """
    decoded=''.join(chr(ord(c) ^ 0x39) if i % 2 == 1 else c for i, c in enumerate(encoded))
    return decoded

def reverse_neuro_shift(encoded):
    """
    Paramètres : 
    - encoded -> string(chaine encodée)
    
    Utilisation : 
    - Faire l'opération inverse de neuro shift présent dans punkrev

    Paramètres : 
    - decoded -> string(chaine après neuro shift)
    """
    decoded=encoded[4:] + encoded[:4]
    return decoded

def reverse_cyber_chain(encoded):
    """
    Paramètres : 
    - encoded -> string(chaine encodée par punkrev)
    
    Utilisation : 
    - Appeler les fonctions de punkrev dans le sens inverse pour pouvoir décoder la chaine de caractère

    Paramètres : 
    - decoded -> string(chaine décodée)
    """
    s = reverse_nano_modulate(encoded)
    s = reverse_datastream_morph(s)
    s = reverse_ghost_inject(s)
    decoded = reverse_neuro_shift(s)
    return decoded

if __name__ == "__main__":
    # Les codes ASCII présents dans les fichiers Java liés à PunkRev
    ascii_codes = [
        [
        69, 107, 74, 62, 83, 91, 121, 7, 116, 72, 
        55, 98, 78, 87, 106, 5, 101, 66, 74, 112
        ],
        [
        69, 107, 74, 62, 69, 74, 54, 85, 111, 100, 
        69, 87, 117, 101, 85, 7, 120, 66, 74, 112
        ],
        [
        69, 107, 74, 62, 85, 74, 124, 99, 84, 90, 
        122, 98, 102, 126, 101, 122, 99, 66, 74, 112
        ],
        [
        69, 107, 74, 62, 79, 8, 119, 99, 86, 79,
        56, 73, 96, 65, 16, 97, 70, 68, 120
        ]
    ]
    # Boucle pour parcourir les codes ASCII
    for (i,y) in enumerate(ascii_codes):
        # Création de la string avec les codes ASCII
        encoded = ''.join(chr(c) for c in y)
        # Appel de la fonction reverse_cyber_chain pour décoder la string
        decoded = reverse_cyber_chain(encoded)
        # Affichage
        print(f"Chaine n° {i+1}")
        print(f"Input encodé   : {encoded}")
        print(f"Flag retrouvé  : {decoded}")