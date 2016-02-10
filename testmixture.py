import mixture, bioMixture


data = bioMixture.readFastaSequences('dataset.fa')

m = bioMixture.getModel(2,10)

m.EM(data,40,0.1)

c = m.classify(data)
