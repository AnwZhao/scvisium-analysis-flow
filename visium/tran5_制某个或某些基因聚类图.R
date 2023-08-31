source('Bmk_Space_mapping_v3.R')

object <- Create_object(
  
  FilePath = 'L7_callus1',
  
  barcode_pos_file = 'L7_callus1/barcodes_pos.tsv.gz',
  
  out_path = 'tran5_制某个或某些基因聚类图',
  
  png_path = 'L7_callus1/he_new.png',
  
  point_size = 2.6,                   #同上
  
  Gene_stat = T,                      #是否进行mark gene绘制
  
  Custom_gene = T,                    #是否进行自定义gene绘制
  
  alpha_continuous = c(0.5,1),        #根据基因表达量调整透明度范围
  
  gene_list = c('Solyc07g007755.2')
)              #绘制的基因名，可以输入多个