source('Bmk_Space_mapping_v3.R')


object <- Create_object(
  
  FilePath = 'L7_callus1',
  
  barcode_pos_file = 'L7_callus1/barcodes_pos.tsv.gz',
  
  out_path = 'tran1',
  
  png_path = 'L7_callus1/he_new.png',
  
  min.cells = 10,         #一个基因至少在n个细胞中表达才被保留，可自行调整，默认值10
  
  min.features = 100,     #一个细胞至少有n个基因才被保留，可自行调整，默认值100
  
  dims = 1:25,            #选择多少pc进行后续分析，可自行调整，默认1：30
  
  resolution = 0.5,       #设置下游分析的“粒度”，值越高得到的聚类数目越多，可自行调整，默认0.5
  
  point_size = 1,         #点的大小，可自行根据矩阵文件level调整，level越小需设置的值越小
  
  width = 12,             #输出图片的宽度，可自行调整，默认12
  
  height = 5,             #输出图片的高度，可自行调整，默认5
  
  Cluster = T,            #是否进行聚类分析，默认F
  
  label = T               #是否输出带标签的聚类图
  
)
