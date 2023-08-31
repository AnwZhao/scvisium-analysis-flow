source('Bmk_Space_mapping_v3.R')

object <- Create_object(
  
  FilePath = 'L7_callus1',
  
  barcode_pos_file = 'L7_callus1/barcodes_pos.tsv.gz',
  
  out_path = 'tran7_单个cluster',
  
  png_path = 'L7_callus1/he_new.png',
  
  point_size = 2,                 #同上
  
  Single_cluster = T             ) #是否绘制单个cluster图