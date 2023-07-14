import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('TaxaDataEdit.csv')

# Get distinct entries in the 'Family' column
distinct_entries = df['Family'].unique()

# # Print the distinct entries
# for entry in distinct_entries:
#     print(entry)

families_in_tree = "Alligatoridae Crocodylidae Struthionidae Rheidae Apterygidae Aepyornithidae Tinamidae Emeidae Dinornithidae Casuariidae Numididae Phasianidae Odontophoridae Cracidae Megapodiidae Anhimidae Anatidae Anseranatidae Caprimulgidae Nyctibiidae Steatornithidae Podargidae Aegothelidae Trochilidae Apodidae Hemiprocnidae Otididae Cuculidae Musophagidae Columbidae Pteroclidae Mesitornithidae Heliornithidae Sarothruridae Rallidae Psophiidae Aptornithidae Gruidae Aramidae Podicipedidae Phoenicopteridae Burhinidae Pluvianellidae Chionidae Pluvianidae Charadriidae Recurvirostridae Ibidorhynchidae Haematopodidae Stercorariidae Turnicidae Glareolidae Dromadidae Alcidae Laridae Thinocoridae Pedionomidae Rostratulidae Jacanidae Scolopacidae Phaethontidae Eurypygidae Rhynochetidae Gaviidae Spheniscidae Diomedeidae Oceanitidae Hydrobatidae Procellariidae Ciconiidae Fregatidae Sulidae Phalacrocoracidae Anhingidae Threskiornithidae Scopidae Pelecanidae Balaenicipitidae Ardeidae Opisthocomidae Cathartidae Sagittariidae Pandionidae Accipitridae Strigidae Tytonidae Coliidae Leptosomidae Trogonidae Bucerotidae Bucorvidae Phoeniculidae Upupidae Meropidae Coraciidae Brachypteraciidae Todidae Alcedinidae Momotidae Galbulidae Bucconidae Indicatoridae Picidae Megalaimidae Lybiidae Capitonidae Semnornithidae Ramphastidae Cariamidae Falconidae Strigopidae Cacatuidae Psittaculidae Psittacidae Acanthisittidae Eurylaimidae Philepittidae Calyptomenidae Pittidae Sapayoidae Melanopareiidae Conopophagidae Thamnophilidae Grallariidae Rhinocryptidae Formicariidae Furnariidae Pipridae Cotingidae Tityridae Tyrannidae Menuridae Atrichornithidae Ptilonorhynchidae Climacteridae Maluridae Dasyornithidae Meliphagidae Acanthizidae Pardalotidae Orthonychidae Pomatostomidae Cinclosomatidae Campephagidae Neosittidae Mohouidae Eulacestomatidae Falcunculidae Oreoicidae Vireonidae Paramythiidae Psophodidae Oriolidae Pachycephalidae Machaerirhynchidae Artamidae Rhagologidae Aegithinidae Malaconotidae Platysteiridae Vangidae Dicruridae Rhipiduridae Monarchidae Ifritidae Paradisaeidae Melampittidae Corcoracidae Corvidae Laniidae Platylophidae Cnemophilidae Melanocharitidae Callaeidae Notiomystidae Chaetopidae Picathartidae Petroicidae Stenostiridae Hyliotidae Paridae Remizidae Alaudidae Panuridae Nicatoridae Macrosphenidae Acrocephalidae Pnoepygidae Cisticolidae Donacobiidae Bernieridae Locustellidae Hirundinidae Phylloscopidae Hyliidae Aegithalidae Erythrocercidae Scotocercidae Cettiidae Sylviidae Paradoxornithidae Zosteropidae Timaliidae Leiothrichidae Alcippeidae Pellorneidae Pycnonotidae Dulidae Ptiliogonatidae Bombycillidae Hylocitreidae Mohoidae Hypocoliidae Buphagidae Sturnidae Mimidae Elachuridae Cinclidae Muscicapidae Turdidae Regulidae Tichodromidae Sittidae Certhiidae Troglodytidae Polioptilidae Promeropidae Modulatricidae Nectariniidae Dicaeidae Chloropseidae Irenidae Peucedramidae Urocynchramidae Ploceidae Viduidae Estrildidae Prunellidae Passeridae Motacillidae Fringillidae Rhodinocichlidae Calcariidae Emberizidae Cardinalidae Mitrospingidae Thraupidae Passerellidae Parulidae Icteridae Icteriidae Calyptophilidae Zeledoniidae Teretistridae Nesospingidae Spindalidae Phaenicophilidae"

families_in_tree = str(families_in_tree)


print("families in the csv but not in tree")
for entry in distinct_entries:
    if entry not in families_in_tree:
    #     print(f"'{entry}' is present in the string.")
    # else:
        print(f"'{entry}' is not present in the string.")

print("families in tree but not csv")
for entry in families_in_tree.split():
    if entry not in distinct_entries:
    #     print(f"'{entry}' is present in the string.")
    # else:
        print(f"'{entry}' is not present in the csv.")