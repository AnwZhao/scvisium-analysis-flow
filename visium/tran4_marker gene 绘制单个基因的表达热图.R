source('Bmk_Space_mapping_v3.R')

object <- Create_object(
  
  FilePath = 'L7_callus1',
  
  barcode_pos_file = 'L7_callus1/barcodes_pos.tsv.gz',
  
  out_path = 'tran4_marker gene 绘制单个基因的表达热图',
  
  png_path = 'L7_callus1/he_new.png',
  
  point_size = 2,                 #同上
  
  Gene_stat = T,                  #是否进行mark gene绘制
  
  top_gene = 1,                   #每个cluster取top多少mark gene， 可自行调整，值不宜设置太大
  
  min.pct = 0.25,                 #一个基因在任何两群细胞中的占比不能低于多少， 可自行调整
  
  logfc.threshold = 0.25,        #差异倍数阈值， 可自行调整
  
  markpic_width = 8,              #小提琴图和tsne图宽
  
  markpic_height = 12)           #小提琴图和tsne图长