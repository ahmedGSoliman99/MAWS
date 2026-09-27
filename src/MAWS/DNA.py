from Complex import *
from Structure import *

DNAresidues = ["DGN", "DAN", "DTN", "DCN",
               "DG", "DA", "DT", "DC", 
               "DG5", "DA5", "DT5", "DC5",
               "DG3", "DA3", "DT3", "DC3"]

DNAphosphate = [["DGN", 0, 1, None],
                ["DAN", 0, 1, None], 
                ["DTN", 0, 1, None], 
                ["DCN", 0, 1, None],
                ["DG5", 0, 1, None],
                ["DA5", 0, 1, None], 
                ["DT5", 0, 1, None], 
                ["DC5", 0, 1, None],
                ["DG", 0, 3, None],
                ["DA", 0, 3, None], 
                ["DT", 0, 3, None], 
                ["DC", 0, 3, None],
                ["DG3", 0, 3, None],
                ["DA3", 0, 3, None], 
                ["DT3", 0, 3, None], 
                ["DC3", 0, 3, None]]

DNAoc5 = [["DGN", 2, 3, None],
          ["DAN", 2, 3, None], 
          ["DTN", 2, 3, None], 
          ["DCN", 2, 3, None],
          ["DG5", 2, 3, None],
          ["DA5", 2, 3, None], 
          ["DT5", 2, 3, None], 
          ["DC5", 2, 3, None],
          ["DG", 3, 4, None],
          ["DA", 3, 4, None], 
          ["DT", 3, 4, None], 
          ["DC", 3, 4, None],
          ["DG3", 3, 4, None],
          ["DA3", 3, 4, None], 
          ["DT3", 3, 4, None], 
          ["DC3", 3, 4, None]]

DNAbase = [["DGN", 8, 10, -4],
           ["DAN", 8, 10, -4], 
           ["DTN", 8, 10, -4], 
           ["DCN", 8, 10, -4],
           ["DG5", 8, 10, -4],
           ["DA5", 8, 10, -4], 
           ["DT5", 8, 10, -4], 
           ["DC5", 8, 10, -4],
           ["DG", 10, 12, -4],
           ["DA", 10, 12, -4], 
           ["DT", 10, 12, -4], 
           ["DC", 10, 12, -4],
           ["DG3", 10, 12, -4],
           ["DA3", 10, 12, -4], 
           ["DT3", 10, 12, -4], 
           ["DC3", 10, 12, -4]]


DNAlengths = [32, 31, 31, 29, 
              33, 32, 32, 30,
              31, 30, 30, 28,
              34, 33, 33, 31]

DNAalias = [["DGN","DGN","DG5","DG","DG3"],["DAN","DAN","DA5","DA","DA3"],["DTN","DTN","DT5","DT","DT3"],["DCN","DCN","DC5","DC","DC3"],
            ["DG3","DG3","DG","DG","DG3"],["DA3","DA3","DA","DA","DA3"],["DT3","DT3","DT","DT","DT3"],["DC3","DC3","DC","DC","DC3"],
            ["DG5","DG5","DG5","DG","DG"],["DA5","DA5","DA5","DA","DA"],["DT5","DT5","DT5","DT","DT"],["DC5","DC5","DC5","DC","DC"],
            ["G","DGN","DG5","DG","DG3"],["A","DAN","DA5","DA","DA3"],["T","DTN","DT5","DT","DT3"],["C","DCN","DC5","DC","DC3"]]



DNA = Structure(DNAresidues,
                residue_length=DNAlengths,
                rotating_elements=DNAphosphate+DNAoc5+DNAbase,
                alias=DNAalias)



# Add this to DNA.py or create RNA.py

RNAresidues = ["RGN", "RAN", "RUN", "RCN",
               "RG", "RA", "RU", "RC",
               "RG5", "RA5", "RU5", "RC5",
               "RG3", "RA3", "RU3", "RC3"]

RNAphosphate = [["RGN", 0, 1, None],
                ["RAN", 0, 1, None],
                ["RUN", 0, 1, None],
                ["RCN", 0, 1, None],
                ["RG5", 0, 1, None],
                ["RA5", 0, 1, None],
                ["RU5", 0, 1, None],
                ["RC5", 0, 1, None],
                ["RG", 0, 3, None],
                ["RA", 0, 3, None],
                ["RU", 0, 3, None],
                ["RC", 0, 3, None],
                ["RG3", 0, 3, None],
                ["RA3", 0, 3, None],
                ["RU3", 0, 3, None],
                ["RC3", 0, 3, None]]

RNAoc5 = [["RGN", 2, 3, None],
          ["RAN", 2, 3, None],
          ["RUN", 2, 3, None],
          ["RCN", 2, 3, None],
          ["RG5", 2, 3, None],
          ["RA5", 2, 3, None],
          ["RU5", 2, 3, None],
          ["RC5", 2, 3, None],
          ["RG", 3, 4, None],
          ["RA", 3, 4, None],
          ["RU", 3, 4, None],
          ["RC", 3, 4, None],
          ["RG3", 3, 4, None],
          ["RA3", 3, 4, None],
          ["RU3", 3, 4, None],
          ["RC3", 3, 4, None]]

RNAbase = [["RGN", 8, 10, -4],
           ["RAN", 8, 10, -4],
           ["RUN", 8, 10, -4],
           ["RCN", 8, 10, -4],
           ["RG5", 8, 10, -4],
           ["RA5", 8, 10, -4],
           ["RU5", 8, 10, -4],
           ["RC5", 8, 10, -4],
           ["RG", 10, 12, -4],
           ["RA", 10, 12, -4],
           ["RU", 10, 12, -4],
           ["RC", 10, 12, -4],
           ["RG3", 10, 12, -4],
           ["RA3", 10, 12, -4],
           ["RU3", 10, 12, -4],
           ["RC3", 10, 12, -4]]

RNAlengths = [33, 32, 32, 31,  # N-terminal
              33, 32, 32, 31,  # internal
              33, 32, 32, 31,  # 5' terminal
              33, 32, 32, 31]  # 3' terminal

RNAalias = [["RGN","RGN","RG5","RG","RG3"],["RAN","RAN","RA5","RA","RA3"],["RUN","RUN","RU5","RU","RU3"],["RCN","RCN","RC5","RC","RC3"],
            ["RG3","RG3","RG","RG","RG3"],["RA3","RA3","RA","RA","RA3"],["RU3","RU3","RU","RU","RU3"],["RC3","RC3","RC","RC","RC3"],
            ["RG5","RG5","RG5","RG","RG"],["RA5","RA5","RA5","RA","RA"],["RU5","RU5","RU5","RU","RU"],["RC5","RC5","RC5","RC","RC"],
            ["G","RGN","RG5","RG","RG3"],["A","RAN","RA5","RA","RA3"],["U","RUN","RU5","RU","RU3"],["C","RCN","RC5","RC","RC3"]]

RNA = Structure(RNAresidues,
                residue_length=RNAlengths,
                rotating_elements=RNAphosphate+RNAoc5+RNAbase,
                alias=RNAalias)



cpx = Complex()
cpx.add_chain("G C A T", DNA)
cpx.build()
chain = cpx.chains[0]
fil = open("TestInputGeometry.pdb","w")
fol = open("TestOutputGeometry.pdb","w")
app.PDBFile.writeModel(cpx.topology, cpx.positions,
                       file=fil, modelIndex=1)
chain.rotate_in_residue(3,1,30.)
chain.prepend_sequence("A C")
cpx.rebuild()
chain.append_sequence("A C")
cpx.rebuild()
chain.append_sequence("A C")
cpx.rebuild()
app.PDBFile.writeModel(cpx.topology, cpx.positions,
                       file=fol, modelIndex=1)
