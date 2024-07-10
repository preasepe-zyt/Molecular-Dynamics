# 载入bio3d包
library("bio3d")
# 载入轨迹和pdb文件
dcd <- read.dcd("pro.dcd")
pdb <- read.pdb("pro.pdb")
# 选取C-alpha原子进行分析
ca.inds <- atom.select(pdb, elety="CA")
xyz <- fit.xyz(fixed=pdb$xyz, mobile=dcd, fixed.inds=ca.inds$xyz,mobile.inds=ca.inds$xyz)
dim(xyz) == dim(dcd)
# 绘制协方差矩阵
cij <- dccm(xyz[,ca.inds$xyz])
plot(cij)
# 绘制主成分图
pc <- pca.xyz(xyz[,ca.inds$xyz])
pdf("pca.pdf")
plot(pc, col=bwr.colors(nrow(xyz)))
plot(pc$z[,1], pc$z[,2], col=bwr.colors(nrow(xyz)), xlab="PC1", ylab="PC2", main="PCA Plot (PC1 vs PC2)")
dev.off()