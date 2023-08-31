source('Bmk_Space_mapping_v3.R')

object <- Create_object(
  
  FilePath = 'L7_callus1',
  
  barcode_pos_file = 'L7_callus1/barcodes_pos.tsv.gz',
  
  out_path = 'tran2_UMI统计',
  
  png_path = 'L7_callus1/he_new.png',
  
  point_size = 3,                 #同上
  
  width = 12,                     #同上
  
  height = 5,                     #同上
  
  UMI_stat = T)                   #是否统计UMI