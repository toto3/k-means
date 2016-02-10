mat <- matrix(runif(25),5,5)
res <- cascadeKM(mat, 2, 5, iter = 25, criterion = 'calinski') 
toto <- plot(res)


toto2 <- plot(mat)
fix(mat)
mat

x <- matrix(scan("KmeansData.txt",5), nrow=5 ncol=5, byrow=TRUE);
