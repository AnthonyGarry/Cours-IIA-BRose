# Classes mères et enfants https://www.geeksforgeeks.org/python/python-access-parent-class-attribute/
# Classes et méthodes abstraites https://www.geeksforgeeks.org/python/abstract-classes-in-python/    


################################################
##################  WARNING  ###################
#################  ATTENTION  ##################
#                                              #
#########  Ce code n'a pas été tester  #########
#                                              #
#################  ATTENTION  ##################
##################  WARNING  ###################
################################################


from abc import abstractmethod

# Merci ChatGPT pour m'avoir montrer cette fonction
def VerificationFormatAdresseMAC(Table):
    return (
        isinstance(Table, list) # isinstance(variable, type) vérifie que la variable correspond au type et retourne un booléen après la vérification (Renvoie True ou False)
        and len(Table) == 2
        and all(
            # Adresse est une variable connu car la fonction all() ne s'exécutera qu'une fois
            # Tout ses paramètres chargés (Imaginer un couloir avec plusieurs portes: 
            # On ne peux commencer à ouvrir les portes qu'une fois qu'elles sont toutes en
            # place. Donc on visite une première fois et si il y a au bout du couloir un 
            # papier disant que seul les portes en plastiques sont valides, on le saura
            # pendant notre passage de vérification.)
            #
            # Tl;Dr: La variable 'Adresse' est définie dans la fonction 'all()' donc python
            # sais ce qu'elle est.
            isinstance(Adresse, list)
            and len(Adresse) == 17 # 17 car une adresse MAC comporte 17 caractères, en comptant les ':'
            and all(isinstance(MorceauAdresse, str) for MorceauAdresse in Adresse)
            for Adresse in Table
        )
    )

class Switch:
    Nom = "Switch"
    Niveau = 0
    NombreDePorts = 2
    # TableDAdresse à besoin d'une fonction de vérification car on ne peux pas définir
    # quels types de valeurs peuvent être entrer dans une variable (donc l'idée de base qui 
    # était, pour une table IPV4, de faire:
    # TableDAdresseIPV4 = [
    # [int,int,int,int],
    # [int,int,int,int]
    # ]
    # ne fonctionnerais pas. (Merci ChatGPT pour l'explication))
    TableDAdresse = [
        [],
        []
        ]

    @abstractmethod
    def Adresse(Adresse1, Adresse2):
        pass

    def __init__(self, Nom, Niveau, NombreDePorts, TableDAdresse):
        self.Nom = Nom
        self.Niveau = Niveau
        self.NombreDePorts = NombreDePorts
        self.TableDAdresse = TableDAdresse

class SwitchL2:
    Niveau = 2
    
    def Adressage(Adresse1, Adresse2):
        Table = [[Adresse1],[Adresse2]]
        if(VerificationFormatAdresseMAC(Adresse1, Adresse2)):
            TableDAdresse += Table
        else:
            return('ERREUR: Format incorrect ! Format attendu: \'[["AA:11:AA:1A:A1:AA"],["AA:11:AA:1A:A1:AA"]]\'')



def VerificationFormatAdresseIPV4(Table):
    return (
        isinstance(Table, list) # isinstance(variable, type) vérifie que la variable correspond au type et retourne un booléen après la vérification (Renvoie True ou False)
        and len(Table) == 2
        and all(
            # Adresse est une variable connu car la fonction all() ne s'exécutera qu'une fois
            # Tout ses paramètres chargés (Imaginer un couloir avec plusieurs portes: 
            # On ne peux commencer à ouvrir les portes qu'une fois qu'elles sont toutes en
            # place. Donc on visite une première fois et si il y a au bout du couloir un 
            # papier disant que seul les portes en plastiques sont valides, on le saura
            # pendant notre passage de vérification.)
            #
            # Tl;Dr: La variable 'Adresse' est définie dans la fonction 'all()' donc python
            # sais ce qu'elle est. (Ici: Elle est définie dans la dernière ligne de la fonction 'all()' ). )
            isinstance(Adresse, list)
            and len(Adresse) == 4
            and all(
                isinstance(QuartAdresse, list)
                and len(MorceauAdresse == 3 for MorceauAdresse in QuartAdresse)
                for QuartAdresse in Adresse)
            for Adresse in Table
        )
    )



class SwitchL3( Switch ):
    Niveau = 3

    def Adressage(Adresse1, Adresse2):
        Table = [[Adresse1],[Adresse2]]

        if(VerificationFormatAdresseIPV4(Adresse1, Adresse2)):
            TableIPV4 = [
                [],
                []
                ]
            
            for MorceauAdresse in Table:
                for BoutDAdresse in MorceauAdresse:
                    if BoutDAdresse < 3: # Inférieur à 3 car sinon on finira avec " 127.0.0.1. "
                        TableIPV4[1] += str(BoutDAdresse) + "."
                    elif(BoutDAdresse > 4 and BoutDAdresse < 8): # Pareil que vérification précédente
                        TableIPV4[2] += str(BoutDAdresse) + "."
            
            TableDAdresse += TableIPV4
        
        else:
            return("ERREUR: Format incorrect ! Format attendu: '[ [ [127],[0],[0],[1] ],[ [127],[0],[0],[1] ] ]'")